![alt text](https://github.com/SmartWheelchair/Systems/blob/master/Wheelchair%203D%20Part%20Images/UCSD_Wheelchair_Team_Logo.png "Logo")

# The Navigation Team

## Our Mission
  
  Our goal is to use latest affordable, efficient sensors to create power kits that can be mounted on electric wheelchairs to give our
  users assistive autonomy. Moreover, we aim to deliver a fully functional sensor-integrated affordable modular design that can be replicated by others in a feasable manner. Our kit will allow users to have a low-level autonomous system feature to help navigate through tight spaces such as a narrow hallway or a narrow entrance. Moreover, with our safety feature implementations, we make sure our users stay safe and have full control of their electric chair while using our system.
  
## Implementation
  
  We create our autonomous system by using an STM32 Nucleo-F767ZI board for real time operation in conjunction with distance sensors, an
  intertial measurement unit, encoders, and emergency stop button. 
  
  <img src="https://github.com/SmartWheelchair/Systems/blob/master/Wheelchair%203D%20Part%20Images/STM32_Nucleo_F767ZI.PNG" width="500">

  We are currently using the VL53L1X time of flight distance sensors to aid with safety features. The sensors return the distance that an object is from the wheelchair and based on this information, the wheelchair slows down and halts if necessary. The sensors are also used to avoid running over a ledge, and to stop the chair from colliding with a wall or object in front of it. We also use the distance sensors to help our users navigate in a straight line if they are in a narrow hallway or to aid with entering a narrow entrances.

<p align="left">
  <img src="https://github.com/SmartWheelchair/Systems/blob/master/Wheelchair%203D%20Part%20Images/ToF_Sensors_VL53L1X_Image.PNG" width="250"/>
  <img src="https://github.com/SmartWheelchair/Systems/blob/master/Wheelchair%203D%20Part%20Images/ToF_Sensors_Working.PNG" width="500">
</p>

  Moreover, we use the Bosch-Hillcrest Lab BNO080 IMU (inertial measurement unit) to stablize linear motion, reduce drift, avoid collisions while turning, and send linear and angular data to our Navigation team counterpart. We use this specific IMU due to its dynamic sensor calibration feature and its precise measurements compared to the previous IMU that we used; BNO055. 
  
  <p align="left">
  <img src="https://github.com/SmartWheelchair/Systems/blob/master/Wheelchair%203D%20Part%20Images/Imu_BNO080_Image.PNG" width="350">
  <img src="https://github.com/SmartWheelchair/Systems/blob/master/Wheelchair%203D%20Part%20Images/IMU_Degrees_of_Freedom.PNG" width="350"/>
</p>


## Contact
**Website:** http://smartwheelchair.eng.ucsd.edu/  
**Phone:** (619) 836-8052  
**Email:** smartwheelchair.eng.ucsd.edu  
