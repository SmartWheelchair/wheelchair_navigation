![alt text](https://github.com/SmartWheelchair/Systems/blob/master/Wheelchair%203D%20Part%20Images/UCSD_Wheelchair_Team_Logo.png "Logo")


# The Navigation Team

## Overview

These ROS scripts receive the information that the Embedded Team is sending over to ROS. Using these files we are able to unpack the sensor data from the wheelchair and display it onto the terminal for the user to see and utilize. We are currently receiving data from the IMU, time of flight (ToF) sensor, encoder, and odometry. We are currently using the odometry message for localization and path planning. On top of that, we hope to use the rest of the data to make logical decision when navigating to avoid objects that do not appear in the 3D map.
