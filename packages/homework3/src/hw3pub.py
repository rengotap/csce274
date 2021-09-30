#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32

def hw3pub():
    pub = rospy.Publisher("/homework2/topic", Float32, queue_size=10);
    rospy.init_node('hw3pub', anonymous=True)
    rate = rospy.Rate(10)  # 10hz

    while not rospy.is_shutdown():
        pub.publish(8492)
        rate.sleep()

if __name__ == '__main__':
    try:
        hw3pub()
    except rospy.ROSInterruptException:
        pass
