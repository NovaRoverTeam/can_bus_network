#!/usr/bin/env python
import can
import rospy
from std_msgs.msg import String
from can_bus_ids import *
from can_bus_network.msg import *

bustype = 'socketcan_native'  #Using socketcans virtual can network
can_interface = 'can1'     #Receiving can bus channel
bus = can.interface.Bus(can_interface, bustype = 'socketcan_native')

gps_pub = None
imu_pub = None

def gps(data):
    rospy.loginfo(data.data[0])
    gps_pub.publish(data.data[0])

def imu(data):
    message_data = data.data
    imu_message = sensors_imu()
    imu_message.euler_x = (message_data[0] << 8) + message_data[1]
    imu_message.euler_y = (message_data[2] << 8) + message_data[3]
    imu_message.euler_z = (message_data[4] << 8) + message_data[5]
    rospy.loginfo(imu_message)
    imu_pub.publish(imu_message)

switcher = {SENSOR_GPS_ID: gps, SENSOR_IMU_ID: imu}  #Dictionary of function calls


def setup():
   rospy.loginfo("test1")
   #Set up publisher nodes for all can_bus reports and sensor data
   global gps_pub
   global imu_pub
   gps_pub = rospy.Publisher('canrx/sensors/gps', String, queue_size=10)
   imu_pub = rospy.Publisher('canrx/sensors/gps', sensors_imu, queue_size=10)
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
