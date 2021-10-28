#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32

class Converter:
    def __init__(self):
        rospy.Subscriber("/homework2/total", Float32, self.callback)  # listening to hw2 total
        self.pub = rospy.Publisher("converter", Float32, queue_size=10)  # publishing
        #self.output = 0

    def callback(self, data):
        converted = 0  # converted default to 0
        convertTo = rospy.get_param('convertTo') # data in feet default to meter
        if(convertTo == "meter"):  # meter
                converted = data.data*0.3048
        elif(feet == "feet"):  # feet
                converted = data.data
        elif(smoot == "smoot"):  # smoot
                converted = data.data*0.179104

        self.pub.publish(converted)
        rospy.loginfo(rospy.get_caller_id() + "Data recieved -- %s", converted)

if __name__ == '__main__':
    rospy.init_node('converter')
    rospy.spin()
    try:
        Converter()
    except rospy.ROSInterruptException:
        pass
