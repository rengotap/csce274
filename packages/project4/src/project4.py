#!/usr/bin/env python3

import rospy
from duckietown_msgs.msg import WheelsCmdStamped, LanePose

class LaneFollow():
    def __init__(self):
        self.wheelPub = rospy.Publisher('/duck16/wheels_driver_node/wheels_cmd', WheelsCmdStamped, queue_size=10)  # not sure what to publish yet
        rospy.logwarn("LaneFollow node has initlized: buh moment (for internal use only)")
        rospy.Subscriber('/duck16/lane_filter_node/lane_pose', LanePose, self.guidance)  # same from project 3
        self.angle = 0
        self.error = 0
        self.errorPrev = 0

        # thresholds
        self.aP = 0
        self.oversteer = 1

    def guidance(self, data):
        self.angle = data.phi
        self.error = data.d
        # Error, d, is negative if too far right. Is positive if too far left.
        rospy.logwarn("\nangle is: %s error is: %s\n", self.angle, self.error) # log input
        l  = rospy.get_param('/duck16/project4/vel_max')
        r = rospy.get_param('/duck16/project4/vel_max')
        # projAngle = 0;  # the angle we think the robot is going to go

        if abs(self.error) >= self.aP:
             # insert good and clean pid code here
            deriv = (abs(self.error)-abs(self.errorPrev))/2
             # Adjust direction as needed
           # if self.error > 0:
           #      l = rospy.get_param('/duck16/project4/vel_max')
           #      r = rospy.get_param('/duck16/project4/p')*self.error + rospy.get_param('/duck16/project4/d')*deriv
            if self.error < 0: # Too close to right side, turn left.
                r = rospy.get_param('/duck16/project4/vel_max')
                l = rospy.get_param('/duck16/project4/p')*abs(self.error) + rospy.get_param('/duck16/project4/d')*deriv
                #l = 0.0

        self.wheelPub.publish(vel_left = l, vel_right = r)
        # Printing legible info:
        rospy.logwarn("\nDuck: %s vel_min: %s vel_Max: %s vel_left: %s vel_right: %s p:%s i:%s d: %s\n", rospy.get_param('/duck16/project4/duck'), rospy.get_param('/duck16/project4/vel_min'), rospy.get_param('/duck16/project4/vel_max'), l, r, rospy.get_param('/duck16/project4/p'), rospy.get_param('/duck16/project4/i'), rospy.get_param('/duck16/project4/d'))
        self.errorPrev = self.error

if __name__ == '__main__':
    rospy.init_node('project4')
    project4 = LaneFollow()
    rospy.spin()
