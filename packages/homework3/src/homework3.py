#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32
class Homework3:
    def __init__(self):
        rospy.Subscriber("subscribe", Float32, self.callback)
        self.pub = rospy.Publisher("publish", Float32, queue_size=10)
        self.publish = 0

    def callback(self, data):
        self.publish += data.data
        self.pub.publish(self.total)

if __name__ == '__main__':
    rospy.init_node('homework3')
    Homework3()

    rospy.spin()
