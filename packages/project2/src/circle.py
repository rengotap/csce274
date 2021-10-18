#!/usr/bin/env python3

import rospy
from duckietown_msgs.msg import Twist2DStamped

def circle():
    circpub = rospy.Publisher('duck16/car_cmd_switch_node/cmd',Twist2DStamped, queue_size=1)  # may not be publishing correctly
    rospy.init_node('circle', anonymous=True)
    rate = rospy.Rate(10)  # 10hz

    while not rospy.is_shutdown():
        msg = Twist2DStamped(header=none, v=1.0, omega=0)

        circpub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        circle()
    except rospy.ROSInterruptException:
        pass
    
