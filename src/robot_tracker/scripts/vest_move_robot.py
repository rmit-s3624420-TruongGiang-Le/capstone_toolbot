#!/usr/bin/env python
import rospy
import numpy as np
from geometry_msgs.msg import Twist
from robot_tracker.msg import VestData

cmd_vel = '/safebase/cmd_vel'
cmd_vel = 'turtle1/cmd_vel'
# cmd_vel = 'cmd_vel'
win_size = 10


def moving_average(x, n=win_size):
    ret = np.cumsum(x, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n


def log(object_area, frame_area, coverage, object_x_center, frame_x_center, linear_velocity):
    # rospy.loginfo(rospy.get_name() + ":\n\t face_height = %f, linear_velocity = %f"
    #               % (face_height, linear_velocity))
    rospy.loginfo(rospy.get_name() + ":\n\t object_area = %s, frame_area = %s\n\t coverage = %s%%\n\t"
                                     " object_x_center = %s,\n\t\t frame_x_center -10%% = %s, frame_x_center +10%% = %s"
                                     "\n\t linear_velocity = %f"
                  % (object_area, frame_area, coverage, object_x_center, frame_x_center * 0.9, frame_x_center * 1.1,
                     linear_velocity))


def callback(data):
    global window
    frame_area = data.cam_height * data.cam_width
    frame_x_center = data.cam_width / 2
    object_area = data.area
    object_x_center = data.x_center
    coverage = object_area / frame_area * 100

    new_vel = 0.0
    # if (object_x_center > frame_x_center * 0.9) and (object_x_center < frame_x_center * 1.1):
    #     if coverage >= 30:
    #         msg_twist_out.linear.x = 0.0
    #         current_vel = msg_twist_out.linear.x
    #     elif (coverage >= 20) and (coverage < 30):
    #         msg_twist_out.linear.x = 0.1
    #         current_vel = msg_twist_out.linear.x
    #     elif (coverage >= 10) and (coverage < 20):
    #         msg_twist_out.linear.x = 0.15
    #         current_vel = msg_twist_out.linear.x
    #     elif (coverage >= 5) and (coverage < 10):
    #         msg_twist_out.linear.x = 0.2
    #         current_vel = msg_twist_out.linear.x
    #     elif (coverage >= 2.5) and (coverage < 5):
    #         msg_twist_out.linear.x = 0.25
    #         current_vel = msg_twist_out.linear.x
    #     elif (coverage >= 1.25) and (coverage < 2.5):
    #         msg_twist_out.linear.x = 0.3
    #         current_vel = msg_twist_out.linear.x
    #     elif (coverage >= 0.635) and (coverage < 1.25):
    #         msg_twist_out.linear.x = 0.35
    #         current_vel = msg_twist_out.linear.x
    #     else:
    #         msg_twist_out.linear.x = 0.0
    if (object_x_center > frame_x_center * 0.9) and (object_x_center < frame_x_center * 1.1):
        if coverage >= 30:
            new_vel = 0.0
        elif (coverage >= 20) and (coverage < 30):
            new_vel = 0.1
        elif (coverage >= 10) and (coverage < 20):
            new_vel = 0.15
        elif (coverage >= 5) and (coverage < 10):
            new_vel = 0.2
        elif (coverage >= 2.5) and (coverage < 5):
            new_vel = 0.25
        elif (coverage >= 1.25) and (coverage < 2.5):
            new_vel = 0.3
        elif (coverage >= 0.635) and (coverage < 1.25):
            new_vel = 0.35
        else:
            new_vel = 0.0
            # log(object_area, frame_area, coverage, object_x_center, frame_x_center, msg.linear.x)

        # pub_twist.publish(msg_twist_out)
    window = np.delete(window, 0)
    window = np.append(window, new_vel)
    print(window)
    current_vel = moving_average(window)
    msg_twist_out.linear.x = current_vel
    log(object_area, frame_area, coverage, object_x_center, frame_x_center, current_vel)


def timer_callback(data):
    pub_twist.publish(msg_twist_out)


def listener():
    global pub_twist
    pub_twist = rospy.Publisher(cmd_vel, Twist, queue_size=10)

    global msg_twist_out
    msg_twist_out = Twist()

    global window
    # window = np.array(np.zeros(win_size,))
    window = np.zeros(win_size, )

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('vest_move_robot', anonymous=True)
    rospy.Subscriber('vest_data', VestData, callback)
    rospy.Timer(rospy.Duration(0.1), timer_callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    listener()
