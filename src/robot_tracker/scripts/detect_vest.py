#!/usr/bin/env python
import cv2
import numpy as np
import rospy
from sensor_msgs.msg import CompressedImage
from robot_tracker.msg import VestData
from collections import deque
import argparse

debug = False


def image_callback(ros_data):

    hsv_lower = (0, 145, 130)
    hsv_upper = (80, 255, 255)

    np_arr = np.fromstring(ros_data.data, np.uint8)
    image_np = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    cam_height = image_np.shape[0]
    cam_width = image_np.shape[1]

    msg_vest_data.cam_height = cam_height
    msg_vest_data.cam_width = cam_width

    hsv = cv2.cvtColor(image_np, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, hsv_lower, hsv_upper)
    kernel = np.ones((3, 18), np.float32)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    mask = cv2.filter2D(mask, -1, kernel)
    (_, cnts, _) = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    center = None
    if len(cnts) > 0:
        cnts = max(cnts, key=cv2.contourArea)
        msg_vest_data.area = cv2.contourArea(cnts)

        M = cv2.moments(cnts)
        x = int(M["m10"] / M["m00"])
        y = int(M["m01"] / M["m00"])
    else:
        x = cam_width/2
        y = cam_height/2
        msg_vest_data.area = 0

    center = (x, y)
    distance_from_center = cam_width/2 - x
    distance_per_degree = 4
    rotation_angle = distance_from_center / distance_per_degree
    msg_vest_data.x_center = x
    msg_vest_data.y_center = y
    msg_vest_data.rotation_angle = rotation_angle
    pub.publish(msg_vest_data)
    rospy.loginfo(rospy.get_name() + '\n\t:Center point of detected object: x=%d y=%d' % center)

    if debug:
        displayvideo(image_np, mask, cnts, center)


def displayvideo(image_np, mask, cnts, center):
    pts = deque(maxlen=64)

    if len(cnts) > 0:
        cv2.drawContours(image_np, [cnts], -1, (0, 255, 0), 3)
        epsilon = 0.08 * cv2.arcLength(cnts, True)
        approx = cv2.approxPolyDP(cnts, epsilon, True)
        cv2.drawContours(image_np, [approx], -1, (255, 255, 0), 3)
        ((x, y), radius) = cv2.minEnclosingCircle(cnts)
        if radius > 10:
            cv2.circle(image_np, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(image_np, center, 5, (0, 0, 255), -1)

    pts.appendleft(center)
    for i in xrange(1, len(pts)):
        if pts[i - 1] is None or pts[i] is None:
            continue
        thickness = int(np.sqrt(64 / float(i + 1)) * 2.5)
        cv2.line(image_np, pts[i - 1], pts[i], (0, 0, 255), thickness)
    img_con = cv2.hconcat((image_np, cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)))
    win_name = 'Video'
    cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
    cv2.imshow(win_name, img_con)
    cv2.waitKey(25)

    # msg_vid = CompressedImage()
    # msg_vid.header.stamp = rospy.Time.now()
    # msg_vid.format = "jpeg"
    # msg_vid.data = np.array(cv2.imencode('.jpg', image_np)[1]).tostring()
    # pub.publish(msg_vid)


if __name__ == '__main__':
    msg_vest_data = VestData()
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("-d", "--debug", help="debug will display video feed", required=False)
        args = parser.parse_args(rospy.myargv()[1:])
        print ('debug: %s' % args.debug)
        if args.debug.upper() == "True".upper():
            debug = True
            # pub_debug_vid = rospy.Publisher("/debug_detect_vest/image_raw/compressed", CompressedImage)
        rospy.init_node('detect_vest', anonymous=True)
        pub = rospy.Publisher('vest_data', VestData, queue_size=1)
        sub = rospy.Subscriber("/usb_cam/image_raw/compressed", CompressedImage, image_callback, queue_size=1)
        print('OpenCV ver: %s' % cv2.__version__)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
