#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32
#include <ros/console.h>

def callback(data):
    rospy.loginfo(rospy.get_caller_id()+ " Data recieved -- %s", data.data)

def listener():
    rospy.init_node('subscriberNode', anonymous=True)
    rospy.Subscriber("/homework2/total", Float32, callback)
    rospy.spin()


if __name__ == '__main__':
    listener()
