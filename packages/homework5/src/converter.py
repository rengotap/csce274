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
           # print("testing 02")
            self.pub.publish(self.conversion())
            time.sleep(1)

    def listener(self, data):
        #print('listening')
        self.input = data.data
        rospy.loginfo("getting -- %s, converted -- %s", self.input, self.conversion())
        self.unit = rospy.get_param('unit')

    def conversion(self):
        #print("converting 03")
        unit = rospy.get_param('unit')
        #print(unit)
        if unit == 'meter':
            msg = self.input*0.3048
        elif unit == 'feet':
            msg = self.input
        elif unit == 'smoot':
            msg = self.input*0.179104
        return msg


if __name__ == '__main__':
        rospy.init_node('converter')
        #print("initialized 01")
        converter = Converter()
        converter.talker()

