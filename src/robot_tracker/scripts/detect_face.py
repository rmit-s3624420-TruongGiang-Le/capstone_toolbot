#!/usr/bin/env python
import argparse
import cv2
import numpy as np
import rospy
from std_msgs.msg import Float32
from sensor_msgs.msg import CompressedImage
import sys

sys.path.append('/opt/ros/kinetic/lib/python2.7/dist-packages')


def image_callback(ros_data):
    np_arr = np.fromstring(ros_data.data, np.uint8)
    image_np = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(image_np, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30),
                                          flags=cv2.CASCADE_SCALE_IMAGE)

    print("Faces = " + str(faces))
    face = [[0, 0, 0, 0]]
    for temp_face in faces:
        print("Face_temp = " + str(temp_face))
        if np.less(face[0][1], temp_face[1]):
            face = [temp_face]
            print("Face = " + str(face))

    for (x, y, w, h) in face:
        cv2.rectangle(image_np, (x, y), (x + w, y + h), (255, 0, 0), 2)
        distance_from_center = (x + w / 2) - 320
        distance_per_degree = 4
        rotation_angle = distance_from_center / distance_per_degree
        pub_rotationAngle.publish(rotation_angle)
        pub_height.publish(h)
        pub_x_center.publish(x + w/2)
        rospy.loginfo("/detect_face:\n\t rotation_angle = %f\n\t X: %d, width: %d\n\t dist from center: %d height: %d"
                      % (rotation_angle, x, w, distance_from_center, h))
        # cv2.imshow('Video', image_np)
        cv2.waitKey(2)


if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("-hc", "--haarcascade", help="haarcascade file to be used", required=True)
        args = parser.parse_args(rospy.myargv()[1:])
        rospy.init_node('detect_face', anonymous=True)
        pub_rotationAngle = rospy.Publisher('rotation_angle', Float32, queue_size=1)
        pub_height = rospy.Publisher('face_height', Float32, queue_size=1)
        pub_x_center = rospy.Publisher('face_x_center', Float32, queue_size=1)
        # face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        face_cascade = cv2.CascadeClassifier(args.haarcascade)
        sub = rospy.Subscriber("/usb_cam/image_raw/compressed", CompressedImage, image_callback, queue_size=1)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
