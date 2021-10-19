#!/usr/bin/env python3

import rospy
import time
from duckietown_msgs.msg import Twist2DStamped

def pentagon():
    pentapub = rospy.Publisher('/duck16/car_cmd_switch_node/cmd',Twist2DStamped, queue_size=10)
    rospy.init_node('pentagon')
    rate = rospy.Rate(10)  # 10hz

    for i in range(5):  # loop 5x b/c pentagon
        # drive straight for .25m
        msg = Twist2DStamped(v=.25, omega=0)  # start
        pentapub.publish(msg)
        time.sleep(1.7)  # sleep for x sec
        msg = Twist2DStamped(v=0, omega = 0) # stop
        pentapub.publish(msg)

        # turn 108 degrees
        msg = Twist2DStamped(v=0.1, omega = -5.7)  #turn
        pentapub.publish(msg)
        time.sleep(1)
        msg = pentapub.publish(v=0, omega = 0) #stop

        time.sleep(1)

    rate.sleep()

if __name__ == '__main__':
    try:
        pentagon()
    except rospy.ROSInterruptException:
        pass
