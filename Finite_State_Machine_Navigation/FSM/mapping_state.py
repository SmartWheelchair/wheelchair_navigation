import os
from os import path

class MappingState:
    def __init__(self):
        self.name = "mapping"

    def run(self):
        """
        Code to be executed when in start state
        """
	Exist = true

	for File in os.listdir('~/Navigation/'):
		if File.endswith('.yaml'):
		print("map exists")
		break
	else:
		print("map does not exist")
		Exist = false
	if not Exist: 
		print("starting mapping software")
		os.system("roslaunch robot_setup_tf convert.launch")
	else: 
		pub = rospy.Publisher("goal_received", Float32, queue_size=1)
                pubOff = rospy.Publisher("map_built", Float32, queue_size=1)
                rate = rospy.Rate(10)
		pubOff.publish(0.0)
                pub.publish(1.0)
                rate.sleep()
        print("mapping_state::body")
	
    def next_state(self, data):
        # decompose the data tuple
        (start_mapping,
        start_logging,
        map_built,
        goal_received,goal_reached) = data
        if map_built:
            return "navigation_ready"
        else:
            return self.name
