#!/usr/bin/env python3

import rospy
from duckietown_msgs.msg import Twist2DStamped

def circle():
    circpub = rospy.Publisher('duck16/car_cmd_switch_node/cmd',Twist2D, queue_size=10)  # may not be publishing correctly?
    rospy.init_node('circle', anonymous=True)
    rate = rospy.Rate(10)  # 10hz
    msg = Twist2DStamped(header=None, v=1, omega=0)

    circpub.publish(msg)
    rate.sleep()

if __name__ == '__main__':
    try:
        circle()
    except rospy.ROSInterruptException:
        pass
    
