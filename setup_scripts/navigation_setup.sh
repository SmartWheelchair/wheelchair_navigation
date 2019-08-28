#!/bin/bash
sudo apt-get install ros-kinetic-navigation 
sudo apt-get install ros-kinetic-depthimage-to-laserscan
sudo apt-get install ros-kinetic-gmapping
sudo apt-get install ros-kinetic-kobuki ros-kinetic-kobuki-core
git clone https://github.com/YuliangCai/gmapping_navigation.git
cd gmapping_navigation
mkdir include
cd ..
catkin_make
