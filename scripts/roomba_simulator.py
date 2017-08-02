#!/usr/bin/env python
import rospy

import roslib
roslib.load_manifest('ipython_robot_prototyping')

import ipython_robot_prototyping.move_turtle

if __name__ == '__main__':
    rospy.init_node('roomba_simulator', anonymous=True)
    
    roomba_simulator= ipython_robot_prototyping.move_turtle.RoombaComm()
    
    rospy.spin()      
        
    
