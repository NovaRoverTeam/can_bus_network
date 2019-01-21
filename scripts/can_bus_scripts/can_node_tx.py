#!/usr/bin/env python
import rospy
import can
from std_msgs.msg import String
from can_bus_ids import *
from can_bus_network.msg import * #motor_arm

bustype = 'socketcan_native'
channel = 'cantx' #cantx is set virtual can, can set up by running the run_can.batch file in sim
bus = can.interface.Bus(channel=channel, bustype=bustype)  #Define the can bus interface to transmit on. 

def drive_send(data):  #Commands for driving the rover. Will either be taken out completely or integrated with the talon libraries. 
    rospy.loginfo("drive_cmd_received")
    msg = can.Message(arbitration_id=MOTOR_DRIVE_ID, data=[data.RPM, int(data.steer)], extended_id = False) 
    can_bus_send(msg)

def arm_send(data):   #Commands for moving the arm with 7 different ID's
    rospy.loginfo("arm_cmd_received")
    msg = can.Message(arbitration_id=MOTOR_ARM_ID[data.id-1], data=[data.x,data.y,data.z], extended_id = False)
    can_bus_send(msg)

def gimbal_send(data):
    rospy.loginfo("gimbal_cmd_received")
    msg = can.Message(arbitration_id=CAMERA_GIMBAL_ID, data=[data.x,data.y,data.z], extended_id = False)
    can_bus_send(msg)

def can_bus_send(msg):
    bus.send(msg)


def setup():
    rospy.init_node('can_node_tx', anonymous=True)
#Subscribe to all topics that need to transmit onto the can_bus
    rospy.Subscriber("cantx/motors/arm",motor_arm, arm_send)
    rospy.Subscriber("cantx/motors/drive",motor_drive, drive_send)
    rospy.Subscriber("cantx/cameras/gimbal",camera_gimbal,gimbal_send)
    rospy.spin()

if __name__ == '__main__':
    setup()
