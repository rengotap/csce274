#!/usr/bin/env python3

import rospy
from duckietown_msgs.msg import Twist2DStamped, LanePose    

class LaneFollow():
    def __init__(self):
        self.pub = rospy.Publisher('/duck16/car_cmd_switch_node/cmd', Twist2DStamped, queue_size=10)  # send corrective commands to wheels
        rospy.Subscriber('/duck16/lane_filter_node/lane_pose', LanePose, self.guidance) # take in the location of the robot
        self.angle = 0  # current angle default 0
        self.error = 0  # current error default 0
        self.velocity = .5  # const speed

        #pid vars
        self.kp = 1
        self.ki = 1
        self.kd = 1
        self.bias = 0
        self.derErr = 0
        self.intErr = 0
        self.prevErr = 0

        # thresholds
        self.aP = .1  # acceptable path (width that the robot can stay in)
        self.overSteer = 1 # pulling too hard in direction

    def guidance(self, data):
        self.angle = data.phi  # current angle Kp
        self.error = data.d  # current error
        rospy.loginfo("angle is -- %s error is -- %s", self.angle, self.error)  # log inputs
        rospy.loginfo("LANE FOLLOWING CODE BY REN")

        cc = 0  # default to no change (stay the course)

        if abs(self.error) >= self.aP: 
            # PID goes here
            p = kp*data.phi
            i = ki
            integral = intErr+data.d*data.dt
            intErr = integral
            d = kd * ((data.d-prevErr)/data.dt)
            prevErr = data.d
            cc = p+i+d+bias
            # cc = self.angle-self.error  # placeholder p control
        if cc > self.oversteer:
            rospy.loginfo("Correcting oversteer at --%s", cc)
            cc = self.oversteer

        self.pub.publish(v=self.velocity, omega=cc)  # send corrective command to wheels


if __name__ == '__main__':
    rospy.init_node('follower')
    follower = LaneFollow()
    rospy.spin()  # loop the code
