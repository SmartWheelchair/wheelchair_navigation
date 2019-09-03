![alt text](https://github.com/SmartWheelchair/Systems/blob/master/Wheelchair%203D%20Part%20Images/UCSD_Wheelchair_Team_Logo.png "Logo")


# About the Program

![images](https://github.com/SmartWheelchair/wheelchair_navigation/blob/master/Images/fsm.png "images")
The finite state machine is meant to handle the entire Navigation Stack and have different states: start, logging, mapping, navigation ready, and Navigating.

![images](https://github.com/SmartWheelchair/wheelchair_navigation/blob/master/Images/start_state.png "images")
The start state's task is to check whether all of the sensors are online (IMUs, ToF, etc), whether the RGB-D and microphone is connected. 

![images](https://github.com/SmartWheelchair/wheelchair_navigation/blob/master/Images/logging_state.png "images")
The logging state's task is to run rosbag so we can record all of the odometry, TcW, and any other data that is being sent from the microphone, camera, or sensors.

![images](https://github.com/SmartWheelchair/wheelchair_navigation/blob/master/Images/mapping_state.png "images")
The mapping state's task is to check whether a map exists on the single board computer (for the Navigation stack to use), if not, it would ask the user whether or not they would want to create a map of their house. If they agree to it, the state would run a script that would execute all the required utilities to map using the camera and wheelchair. 

![images](https://github.com/SmartWheelchair/wheelchair_navigation/blob/master/Images/navigating_ready_state.png "images")
The navigating_ready state's task is to grab the user's command of what they want to do. Specifically, the navigating_ready state will run the google speech python scripts in order to grab the user's command and handle what they want to do. If the user wants to go to a certain location, then the handler will grab the location's coordinates/data and send it to the navigation_state (navigation stack) for path planning and navigation. 

![images](https://github.com/SmartWheelchair/wheelchair_navigation/blob/master/Images/navigating_state.png "images")
The navigating state's task is to run the navigation stack and create a path to the desired location. After traveling to the location successfully it will go back to the navigating_ready_state. 

