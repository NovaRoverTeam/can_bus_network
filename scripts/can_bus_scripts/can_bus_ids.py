
#The can_bus ids for CAN communication.
#The Lower the number, the higher its priority over CAN.
#All ID's are utilised on both TX and RX CAN bus's

MOTOR_DRIVE_ID = 0x10     #1 ID for talon SXR

MOTOR_ARM_ID = [0x21, 0x22, 0x23, 0x24, 0x25, 0x26, 0x27]  #ID's for all 7 joints of the arm


SENSOR_GPS_ID = 0x31   #3 messages for GPS locating device


SENSOR_IMU_ID = 0x41   #3 messages for IMU


CAMERA_GIMBAL_ID = 0x51
