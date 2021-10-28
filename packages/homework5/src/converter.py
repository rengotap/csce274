#!/usr/bin/env python3

import rospy
import time
from std_msgs.msg import Float32

class Converter:
    def __init__(self):
        self.pub = rospy.Publisher("talker",Float32, queue_size=10)
        rospy.Subscriber("/homework2/total", Float32, self.listener)  # listening to hw2 total
        self.input = 0

    def talker(self):
        while True:
            self.pub.publish(self.conversion())
            time.sleep(1)  # to make it readable

    def listener(self, data):
        self.input = data.data
        rospy.loginfo("getting -- %s, converted -- %s", self.input, self.conversion())
        self.unit = rospy.get_param('unit')

    def conversion(self):
        unit = rospy.get_param('unit')
        if unit == 'meter':
            msg = self.input*0.3048
        elif unit == 'feet':
            msg = self.input
        elif unit == 'smoot':
            msg = self.input*0.179104
        return msg


if __name__ == '__main__':
        rospy.init_node('converter')
        converter = Converter()
        converter.talker()

