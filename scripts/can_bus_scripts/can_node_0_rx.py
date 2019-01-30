#!/usr/bin/env python
import can
import rospy
from std_msgs.msg import String
from can_bus_ids import *
from can_bus_network.msg import *

bustype = 'socketcan_native'  #Using socketcans virtual can network
can_interface = 'canrx'     #Receiving can bus channel
bus = can.interface.Bus(can_interface, bustype = 'socketcan_native')

gps_pub = None
imu_pub = None

def drive(message):
    rospy.loginfo(data.data[0])
    gps_pub.publish(data.data[0])

def arm(message):
    arm_id = message.arbitration_id
    rospy.loginfo(str(data.data[0]))
    imu_pub.publish(data.data[0])

switcher = {SENSOR_GPS_1_ID: gps, SENSOR_GPS_2_ID: gps, SENSOR_GPS_3_ID: gps, SENSOR_IMU_1_ID: imu, SENSOR_IMU_2_ID: imu, SENSOR_IMU_3_ID: imu}  #Dictionary of function calls


def setup():
   rospy.loginfo("test1")
   #Set up publisher nodes for all can_bus reports and sensor data
   global gps_pub
   global imu_pub
   drive_pub = rospy.Publisher('canrx/motors/drive', String, queue_size=10)
   arm_pub = rospy.Publisher('canrx/motors/arm', String, queue_size=10)
   print(gps_pub)
   rospy.init_node('can_node_rx', anonymous=True)  #Create the ros node (publishing) 
   rate = rospy.Rate(10) #10Hz
   while not rospy.is_shutdown():
       message = bus.recv()   #Wait until receiving message over can bus
       func = switcher[message.arbitration_id](message)   #Call function dependent on the id of the can message
       rate.sleep()



if __name__ == '__main__':
    rospy.loginfo("test")
    try:
        setup()
    except rospy.ROSInterruptException:
        pass
