#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist

msg = Twist()


def log(face_height, linear_velocity):
    rospy.loginfo(rospy.get_caller_id() + ":\n\t face_height = %f, linear_velocity = %f"
                  % (face_height, linear_velocity))


def callback(data):
    # rospy.loginfo(rospy.get_caller_id() + ":\n\t face_height = %f" % data.data)
    pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
    if data.data >= 200:
        msg.linear.x = 0.0
        log(data.data, msg.linear.x)
    elif (data.data >= 150) and (data.data < 200):
        msg.linear.x = 0.25
        log(data.data, msg.linear.x)
    elif (data.data >= 100) and (data.data < 150):
        msg.linear.x = 0.5
        log(data.data, msg.linear.x)
    else:
        msg.angular.x = 0.0
        log(data.data, msg.linear.x)
    pub.publish(msg)


def listener():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('move_robot', anonymous=True)

    rospy.Subscriber('face_height', Float32, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    listener()
