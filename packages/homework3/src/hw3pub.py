#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32

def hw3pub():
    pub = rospy.Publisher("/homework2/delta", Float32, queue_size=10);
    rospy.init_node("hw3pub", anonymous=True)
    rate = rospy.Rate(100)  # 10hz

    while not rospy.is_shutdown():
        dataToPub = 8492
        rospy.loginfo("sending data")
        pub.publish(dataToPub)
        rate.sleep()

if __name__ == '__main__':
    try:
        hw3pub()
    except rospy.ROSInterruptException:
        pass
