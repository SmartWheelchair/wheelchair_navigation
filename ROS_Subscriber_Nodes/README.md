![alt text](https://github.com/SmartWheelchair/Systems/blob/master/Wheelchair%203D%20Part%20Images/UCSD_Wheelchair_Team_Logo.png "Logo")


# The Navigation Team

## Overview

These .py files receive the information that the Embedded Team is sending over to ROS. Using these files we are able to get
 the sensor data of the wheelchair. We are currently receiving data from the IMU, time of flight (ToF) sensor, encoder, and 
 odometry. We are currently using the odometry message for 3D mapping. We hope to use the rest of the data to make logical 
 decision when navigating to avoid objects that do not appear in the 3D map.
