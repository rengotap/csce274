#!/usr/bin/env python3

import rospy

class LaneFollow():
    def __init__(self):
        self.wheelPub = rospy.Publisher('/duck16/wheels _ driver_node/wheels_cmd', WheelsCmd, queue_size=10)  # not sure what to publish yet
        rospy.Subscriber('/duck16/lane_filter_node/lane_pose', LanePose, self.guidance)  # same from project 3
        self.angle = 0
        self.error = 0
        self.errorPrev = 0

        # thresholds
        self.aP = .1
        self.oversteer = 1

    def guidance(self, data):
        self.angle = data.phi
        self.error = data.d
        rospy.loginfo("angle is -- %s error is -- %s", self.angle, self.error) # log input
        l  = 0;
        r = rospy.get_param(vel_max);  # robot will turn left
        # projAngle = 0;  # the angle we think the robot is going to go

        if abs(self.error) >= self.aP:
             # insert good and clean pid code here
             deriv = (error-errorPrev)/2
             r = rospy.get_param(p)*self.error + rospy.get_param(d)*deriv

        self.wheelPub.publish(vel_left = l, vel_right = r)
        rospy.loginfo("Duck -- %s vel_min -- %s vel_Max -- %s vel_left -- %s vel_right -- %s p --%s i --%s d -- %s", rospy.get_param('duck'), rospy.get_param('vel_min'), rospy.get_param('vel_max'), rospy.get_param('p'), rospy.get_param('i'), rospy.get_param('d')) 
        errorPrev = error

if __name__ == '__main__':
    rospy.init_node('follower')
    follower = LaneFollow()
    rospy.spin()
