#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32

def debug():
    pub= rospy.Publisher("debug",Float32,queue_size=10)
    rospy.init_node("debug")
    rate = rospy.Rate(10)
    msg = 8492
    pub.publish(msg)
    rate.sleep()

if __name__ == '__main__'
    try:
        debug()
    except rospy.ROSInterruptException:
        pass
