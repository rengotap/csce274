#!/usr/bin/env python3

import rospy
import std_msgs.msg import String

def hw3pub():
    pub = rospy.publisher('mumble', String, queue_size=10);
    rospy.init_node('hw3pub')
    rate = rospy.Rate(10)  # 10hz
    
    while not rospy.is_shutdown():
        pub.publish('change me later')
        rate.sleep()

if __name__ == '__main__':
    try:
        hw3pub()
    except rospy.ROSInterruptException:
        pass
