#!/usr/bin/env python3

import rospy
from duckietown_msgs.msg import Twist2DStamped, LanePose    

class LaneFollow():
    def __init__(self):
        self.pub = rospy.Publisher('/duck16/car_cmd_switch_node/cmd', Twist2DStamped, queue_Size=10)  # send corrective commands to wheels
        rospy.Subscriber('/duck16/lane_filter_node/lane_pose', LanePose, self.guidance) # take in the location of the robot
        self.angle = 0  # current angle default 0
        self.error = 0  # current error default 0
        self.velocity = .75  # const speed

        # thresholds
        self.aP = 3  # acceptable path (width that the robot can stay in)
        self.overSteer = 4 # pulling too hard in direction

    def guidance(self.data):
        self.angle = data.phi  # current angle
        self.error = data.d  # current error
        rospy.loginfo("angle is -- %s error is -- %s" self.angle, self.error)  # log inputs

        cc = self.angle  # default to no change
        if self.error >= self.aP: 
            # PID goes here
            cc = self.angle+self.error  # math i don't understand yet but will definitely get to by the end of the day

        self.pub.publish(v=self.velocity, omega=cc)  # send corrective command to wheels


if __name__ == '__main__':
    rospy.init_node('follower')
    follower = LaneFollow()
    rospy.spin()  # loop the code
