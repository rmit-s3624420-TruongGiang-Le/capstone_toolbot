#!/usr/bin/env python

import rospy
from math import fabs
from geometry_msgs.msg import Twist
from geometry_msgs.msg import TwistStamped
import math

######



######

pub = rospy.Publisher('/mirsim/cmd_vel', Twist, queue_size=1)

def cmd_callback(data):
    print data.twist
    print '---'
    pub.publish(data.twist);

######

def relay():
    rospy.init_node('relaycmdvel', anonymous=False)
    rospy.Subscriber('/mobility_base/twist', TwistStamped, cmd_callback)
    print 'Relay ready'
    rospy.spin()

if __name__ == '__main__':
    try:
        relay()
    except rospy.ROSInterruptException:
        pass
