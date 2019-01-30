#!/usr/bin/env python
import rospy
import time
import can

#This code will spam IMU ID with message for euler angles in 16 bits  

bustype = 'socketcan_native'
channel = 'can1'

def producer(id):
    """:param id: Spam the bus with messages including the data id."""
    bus = can.interface.Bus(channel=channel, bustype=bustype)
    for i in range(10):
	data=[id, i, 0, 1, 3, 1, 4, 1]
	value1 = bin(0xFE68)
	data[0]=int(value1[2:10],2)
	data[1]=int(value1[10:],2)

	value2 = bin(0xFE69)
	data[2]=int(value2[2:10],2)
	data[3]=int(value2[10:],2)

	value3 = bin(0xFE70)
	data[4]=int(value3[2:10],2)
	data[5]=int(value3[10:],2)


	msg = can.Message(arbitration_id=0x41, data=[data[0],data[1],data[2],data[3],data[4],data[5]], extended_id=False)
        bus.send(msg)
    time.sleep(1)

producer(10)
