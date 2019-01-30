cmake_minimum_required(VERSION 2.8.3)
project(can_bus_network)
find_package(catkin REQUIRED 
    roscpp
    std_msgs
    rospy
    message_generation )

#Generate messages
add_message_files(
  FILES
  #GPS.msg #Contains 3 x,y,z co-ordinates
  #IMU.msg #Containers 3 messages, gyro, accel and positional
  cantx/motors_arm.msg #Contains both the absolute and incremental angular message types
  cantx/motors_drive.msg #The talon SXR messages for RPM and angle\
  cantx/motors_camera_gimbal.msg #Utilising the already Nova made gimbal message on Github
  canrx/sensors_gps.msg
  canrx/sensors_imu.msg
  canrx/sensors_accelerometer.msg
)

#Services
  #Todo

generate_messages(
  DEPENDENCIES
  std_msgs   #Add the standard messages
  
 # geometry_msgs #Add geometric messages
)

catkin_package(
  CATKIN_DEPENDS message_runtime
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

