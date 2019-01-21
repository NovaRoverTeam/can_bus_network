#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from can_bus_network.msg import *

#This is just for testing purposes, in integration other nodes will publish directly onto the topics for the can_bus to interperate. 
def talker():

    drive_pub = rospy.Publisher('cantx/motors/drive', motor_drive, queue_size=10)
    arm_pub = rospy.Publisher('cantx/motors/arm', motor_arm, queue_size=10)

    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():

        arm_message = motor_arm()
        arm_message.id = 3
        arm_message.x = 1
	arm_message.y = 2
	arm_message.z = 3
        arm_pub.publish(arm_message)

	drive_message = motor_drive()
	drive_message.RPM = 10
	drive_message.steer = 15
	drive_pub.publish(drive_message)

        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
