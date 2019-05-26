#!/usr/bin/env python
import cv2

import numpy as np
import rospy
from sensor_msgs.msg import CompressedImage


def showvideo(winname, image_np):
    cv2.namedWindow(winname, cv2.WINDOW_NORMAL)
    cv2.imshow(winname, image_np)
    cv2.waitKey(2)


def callback(data):
    np_arr = np.fromstring(data.data, np.uint8)
    image_np = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    showvideo("debug_detect_vest", image_np)


def listener():
    rospy.init_node('debug_vid_detect_vest', anonymous=True)
    rospy.Subscriber("/debug_detect_vest/image_raw/compressed", CompressedImage, callback, queue_size=1)

    rospy.spin()


if __name__ == '__main__':
    listener()
