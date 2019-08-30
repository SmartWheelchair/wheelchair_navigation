![alt text](https://github.com/SmartWheelchair/Systems/blob/master/Wheelchair%203D%20Part%20Images/UCSD_Wheelchair_Team_Logo.png "Logo")

# The Navigation Team

## Our Mission
  
  Our goal is to build a processor-efficient program to allow for autonomous navigation throughout a user's house. We use Simultaneous Localization and Mapping (SLAM) to map and navigate through a room using only a RGB-D Camera. We aim to keep it easy to install and able to run on an inexpensive Single-Board Computer. Implementing autonomous navigation allows the users to easily navigate to various preset locations within their house while avoiding any obstacles.
  
## Implementation
  We are currently using a finite state machine which is meant to handle and organize the entire Navigation Stack and have different states:     start, logging, mapping, navigation ready, and navigating.

  <img src="https://github.com/SmartWheelchair/wheelchair_navigation/blob/master/Images/fsm.png" width="500">
  
  We are currently using the UDOO x86 Advanced Plus Single-Board Computer 
  
  <img src="https://github.com/SmartWheelchair/wheelchair_navigation/blob/master/Images/x86_advplus_f.png" width="500">

  We are using the ASUS Xtion Pro Live for our RGB-D Camera

  <img src="https://github.com/SmartWheelchair/wheelchair_navigation/blob/master/Images/ASUS_xtion.png" width="500"> 
  
  The result of gmapping we get 
  
  <img src="https://github.com/SmartWheelchair/wheelchair_navigation/blob/master/Images/gmapping.png" width="500">
  
  The navigation result we get

  <img src="https://github.com/SmartWheelchair/wheelchair_navigation/blob/master/Images/path_planning.png" width="500">
  
## Contact
**Website:** http://smartwheelchair.eng.ucsd.edu/  
**Phone:** (619) 836-8052  
**Email:** smartwheelchair.eng.ucsd.edu  
