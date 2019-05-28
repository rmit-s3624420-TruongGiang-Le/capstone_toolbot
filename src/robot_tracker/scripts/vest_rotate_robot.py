#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist
from robot_tracker.msg import VestData

cmd_vel = '/safebase/cmd_vel'
# cmd_vel = 'turtle1/cmd_vel'
# cmd_vel = 'mir_100/cmd_vel'


def deg2rad(deg):
    deg2rad_ratio = 0.0174533
    return deg * deg2rad_ratio


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + ":\n\t rotation_angle = %f" % data.rotation_angle)
    rotation_angle = data.rotation_angle
    if rotation_angle > 30:
        msg.angular.z = deg2rad(30)
    elif rotation_angle < -30:
        msg.angular.z = deg2rad(-30)
    else:
        msg.angular.z = deg2rad(rotation_angle)
    pub.publish(msg)


def listener():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('rotate_robot', anonymous=True)
    rospy.Subscriber('vest_data', VestData, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    msg = Twist()
    pub = rospy.Publisher(cmd_vel, Twist, queue_size=10)
    listener()
