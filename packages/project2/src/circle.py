#!/usr/bin/env python3

import rospy
import time
from duckietown_msgs.msg import Twist2DStamped

def circle():
    circpub = rospy.Publisher('/duck16/car_cmd_switch_node/cmd',Twist2DStamped, queue_size=10)  # may not be publishing correctly?
    rospy.init_node('circle')
    rate = rospy.Rate(10)  # 10hz
    msg = Twist2DStamped(v=0.4, omega=-3)
    circpub.publish(msg)
    time.sleep(22)
    msg = Twist2DStamped(v=0,omega=0)
    circpub.publish(msg)
    rate.sleep()

if __name__ == '__main__':
    try:
        circle()
    except rospy.ROSInterruptException:
        pass
    
