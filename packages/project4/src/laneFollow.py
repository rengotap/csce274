#!/usr/bin/env python3

import rospy

class LaneFollow():
    def __init__(self):
        self.leftPub = rospy.Publisher('/duck16/????', msgType, queue_size=10)  # not sure what to publish yet
        self.rightPub = rospy.Publisher('duck16/????',msgType, queue_size=10)
        rospy.Subscriber('/duck16/lane_filter_node/lane_pose', LanePose, self.guidance)  # same from project 3
        self.angle = 0
        self. error = 0

        # thresholds
        self.aP = .1
        self.oversteer = 1

    def guidance(self, data):
        self.angle = data.phi
        self.error = data.d
        rospy.loginfo("angle is -- %s error is -- %s", self.angle, self.error) # log input
        vLeft = 0;
        vRight = 0;
        projAngle = 0;  # the angle we think the robot is going to go

        if abs(self.error) >= self.aP:
             # insert good and clean pid code here

        self.leftPub.publish()
        self.rightPub.publish()

if __name__ == '__main__':
    rospy.init_node('follower')
    follower = LaneFollow()
    rospy.spin()
