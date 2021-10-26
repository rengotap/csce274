#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32

class Converter:
    def __init__(self):  # 
        rospy.Subscriber("/homework2/total", Float32, self.callback)  # listening to hw2 total
        self.pub = rospy.Publisher("/homework3/hw3sub", Float32, queue_size=10)  # publishing to hw3 subscriber
        self.output = 0

    def callback(self, data):
        # convert to meters
        self.output = data/3.218
        self.pub.publish(self.output)
        # convert to feet
        self.output = data
        self.pub.publish(self.output)
        # convert to smoot
        self.output = data/5.583
        self.pub.publish(self.output)

if __name__ = '__main__':
    rospy.init_node('converter')
    Converter()
    rospy.spin()
