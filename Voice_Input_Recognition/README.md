![alt text](https://github.com/SmartWheelchair/Systems/blob/master/Wheelchair%203D%20Part%20Images/UCSD_Wheelchair_Team_Logo.png "Logo")

# Voice Input Recognition
 **Implementation of Google Speech in order to obtain voice input commands from the user; uses Robot Operating System (ROS) in order to publish information (Location Name, Coordinates) to the navigation stack.**

## Requirements
#### Hardware
- Microphone
- Internet Connection 
#### Software
- Robot Operating System
- Speech Recognition Package
- PyAudio Package
- Pip or Pip3
- Recommended to update Python to latest Version (3.7)

## Installation
install SpeechRecognition Package
```
sudo pip install SpeechRecognition 
```
install PyAudio Package
```
sudo apt-get install python-pyaudio python3-pyaudio
```
Change Permissions of files to make it executable
```
chmod +x google_speech_input.py
```
```
chmod +x google_speech_handler.py
```
```
chmod +x Create_Dictionary.py
```
Create Dictionary in order to store Location and Odometry Information
```
./Create_Dictionary.py
```



