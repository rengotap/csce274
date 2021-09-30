#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32

def callback(data):
    rospy.loginfo(data.data)

def hw3sub():
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("delta", Float32, callback)

    rospy.spin()

if __name__ == '__main__':
    hw3sub()
