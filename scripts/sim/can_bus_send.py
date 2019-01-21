#!/usr/bin/env python
import rospy
import time
import can

#This code will spam GPS_1 id'd messages onto the canrx bus.  

bustype = 'socketcan_native'
channel = 'canrx'

def producer(id):
    """:param id: Spam the bus with messages including the data id."""
    bus = can.interface.Bus(channel=channel, bustype=bustype)
    for i in range(10):
        msg = can.Message(arbitration_id=0x32, data=[id, i, 0, 1, 3, 1, 4, 1], extended_id=False)
        bus.send(msg)
    time.sleep(1)

producer(10)
