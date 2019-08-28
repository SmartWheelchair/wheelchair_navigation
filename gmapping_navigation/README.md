# gmapping_navigation
#### The code is to implement 2-D navigation based on ROS navigation_stack, kobuki robot, and Asus proxion live RGB-D camera.The code will implement a fake-laser with the depth image data of camera.

## Prerequisite
#### hardware 
- robot which provide odom message to ROS
- RGB-D camera
#### software 
- ROS kinetic (should also works on other version)
- ROS navigtion_stack 
- openni2
- kuboki robot package 
- depthimage_to_laser package

## Install
install navigation stack
```
sudo apt-get install ros-kinetic-navigation 
```
install depthimage_to_laser package
```
sudo apt-get install ros-kinetic-depthimage-to-laserscan
```
install install gmapping package
```
sudo apt-get install ros-kinetic-gmapping
```
install kobuki package 
```
sudo apt-get install ros-kinetic-kobuki ros-kinetic-kobuki-core
```
in kobuki package, we need to add a new parameter
```
roscd kobuki_node
cd launch
nano minimal.launch
```
then add the line under the second node
```
<param name="base_frame" value="base_link" />
```
install gmapping_navigation package, go to /gmapping_navigation create an empty include package
```
git clone https://github.com/YuliangCai/gmapping_navigation.git
cd gmapping_navigation
mkdir include
cd ..
catkin_make
```
create new yaml file follow the guidance
http://wiki.ros.org/navigation/Tutorials/RobotSetup

## Run 
open a new terminal 
```
roscd gmapping_navigation
source devel/setup.bash
```
to map the room, run:
```
roslaunch gmapping_navigation convert.launch
```
after mapping, use the map server to save the map: 
```
rosrun map_server map_saver -f <your_map_name>
```
close the launch file and start the navigation (keep it running), and don't forget to chage the argument of map_server node in mobile.launch to the map you want to load.
```
roslaunch gmapping_navigation mobile.launch
```
to mark the location:
```
roslaunch gmapping_navigation mark.launch
```
type in the name with double quotation eg. "bedroom"

to start navigation :
```
roslaunch gmapping_navigation goal.launch
```
type in the destination with double quotation eg. "bedroom"
