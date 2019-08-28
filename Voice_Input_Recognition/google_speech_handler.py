##################################################################
# Utilizes google speech in order to receive voice input
# reads commands go to ..., mark location ..., delete location ...
# etc. and handles these commands to see whether we need to
# store the information, publish Odometry information, or 
# delete information.
##################################################################
#!/usr/bin/env python
import rospy
import numpy as np
import time
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal, MoveBaseResult, MoveBaseFeedback
from std_msgs.msg import String
from nav_msgs.msg import Odometry

#global variables for storage
x = 0.0 
y = 0.0 
z = 0.0 
ox = 0.0
oy = 0.0
oz = 0.0
ow = 0.0

#publisher to publish Odometry information to Odometry topic
pub = rospy.Publisher('/newOdom', Odometry, queue_size = 1)

def feedback_callback(feedback):
	print('[feedback] Going to Goal Pose...')

def callbackParticle(data):
	global x
	global y
	global z
	global ox
	global oy
	global oz
	global ow
	for x in data.poses:
		x += data.poses.position.x
		y += data.poses.position.y
		z += data.poses.position.z
		ox += data.poses.orientation.x
		oy += data.poses.orientation.y
		oz += data.poses.orientation.z
		ow += data.poses.orientation.w
	x = x/len(data.poses)
	y = y/len(data.poses)
	z = z/len(data.poses)
	ox = oy/len(data.poses)
	oy = oy/len(data.poses)
	oz = oz/len(data.poses)
	ow = ow/len(data.poses)
	
	
#method to initialize global variables
def callbackOdom(data):
        global x
        global y
        global z
        #accesses embedded's odometry topic to get x,y,z
        x = data.pose.pose.position.x
        y = data.pose.pose.position.y   
        z = data.pose.pose.position.z   

#method to make use of the string
def callbackString(data):
        #loads the dictionary for stored locations or locations to be stored
        location = np.load("Dictionary.npy").item()
        text = ""
        textArr = []
        #grabs the text from the ros chatter topic and lowercases it
        text = data.data
        text = text.lower()
        #initialize to an array for easy access of each word
        textArr = text.split(" ")
        mark = ["mark", "mike", "marked", "add", "set"]
        #if uttterance is longer than 3 words
        if len(textArr) > 3:
                i=3
                #loops through the array and combines everything after index 3
                while i < len(textArr):
                        textArr[2] = textArr[2] + textArr[i]
                        i += 1
        
        #edge case for sentences longer than 3 words
        if len(textArr) < 3:
                print 'Length of command not 3'
        #detects if the command is go
        elif textArr[0] == 'go' or textArr[0] == 'move':
                #checks if the location is in the dictionary
                if textArr[2] in location:
                        print "going to location " + textArr[2]
			#create the connection to the action server
			client = actionlib.SimpleActionClient('/move_base', MoveBaseAction)
			#waits until the action server is up and running
			client.wait_for_server()
                        #sets the array stored in location to array
                        array = location[textArr[2]]
                        #grabs location data x,y,z to publish to newOdom topic
			goal = MoveBaseGoal()
			goal.target_pose.header.frame_id = 'map'
			goal.target_pose.pose.position.x = array[0]
			goal.target_pose.pose.position.y = array[1]
			goal.target_pose.pose.position.z = array[2]
			goal.target_pose.pose.orientation.x = array[3]
			goal.target_pose.pose.orientation.y = array[4]
			goal.target_pose.pose.orientation.z = array[5]
			goal.target_pose.pose.orientation.w = array[6]
			client.send_goal(goal, feedback_cb=feedback_callback)
			client.wait_for_result()
			
                else:
                        print "Location not in Dictionary"
        #handles marking locations
        elif textArr[0] in mark:
                if textArr[2] in location:
                        print "Location already marked"
                else:
                        print "marking location " + textArr[2]
                        #stores current location to arrOdom
                        arrOdom = [x,y,z,ox,oy,oz,ow]
                        #stores it in location
                        location[arr[2]] = arrOdom
                        #saves location to numpy for future use
                        np.save("Dictionary.npy", location)
        #handles removing a location
        elif textArr[0] == 'remove' or textArr[0] == 'delete' :
                #checks if location is in the dictionary
                if textArr[2] in location:
                        print "Location " + textArr[2] + " removed"
                        #removes it
                        location.pop(textArr[2])
                        #saves again
                        np.save("Dictionary.npy", locationMap)
                else:
                        print "Location not found"

def listener():
        #creates a new listener node
        rospy.init_node('move_base_action_client', anonymous=True)
        #subscribes to topic
        rospy.Subscriber("/odom", Odometry, callbackOdom)
        rospy.Subscriber("chatter", String, callbackString)
	rospy.Subscriber("particlecloud", PostArray, callbackParticle)
        rospy.spin()

if __name__ == '__main__':
        listener()
