#!/usr/bin/env python3

import rospy
import Twist2d
import numpy as np

from duckietown_msgs.msg import WheelsCmdStamped

def circle():
    circpub = rospy.Publisher('????',wheelCmds, queue_size=1)  # not sure what to publish to yet
    rospy.init_node('circle', anonymous=True)
    rate = rospy.Rate(10)  # 10hz

    while not rospy.is_shutdown():
        msg = wheelCmds()
        # Ignore this we're going to use twist2D
        msg.vLeft = np.random.random()  # temporary left speed
        msg.vRight = np.random.random()  # temporary right speed
        # end ignore

        #right_wheel_voltage = (gain + trim) * (linearVelocity + angularVelocity * 0.5 * baseline)
        #left_wheel_voltage = (gain-trim) * (linearVelocity - angularVelocity * 0.5 * baseline)


        circpub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        circle()
    except rospy.ROSInterruptException:
        pass
    
