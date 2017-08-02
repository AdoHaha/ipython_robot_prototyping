"""Moving the turtle and publishing its position

This module moves the turtlesim turtle1 in a roomba-like fashion, ie 
it moves towards some wall and when it reaches it, rotates by certain degree and goes on. 

"""
import rospy
import roslib
roslib.load_manifest('ipython_robot_prototyping')
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

import numpy as np

import random

from numpy.linalg.linalg import LinAlgError

from sensor_msgs.msg import Range
from std_msgs.msg import Header


walls=[([0,0],[1,0]),([0,0],[0,1]),([10,10],[-1,0]),([10,10],[0,-1])]

    
       
def measure_single_wall(robot_vector,wall):
        """Measures (in a simulated way) turtle distance from the wall he is heading to

        Args:
            robot_vector: [x,y,theta] vector of turtle position and orientation
            wall: ([xw,yw],[wx,wy]) position of the start of the wall and its heading (unit vector)
        Returns:
            (float,boolean): The distance from the wall and info if it is a valid distance
        """
        x0,y0,theta=robot_vector[0:3]
        
        (xw,yw),(wx,wy) = wall
        robot_matrix=np.array([[np.cos(theta), - wx],[np.sin(theta),-wy]])
        
        difference_vector=np.array([[xw],[yw]])-np.array([[x0],[y0]])
        
        if(not np.any(difference_vector)): #on one of the edges
            return 0,True
        
        try:
            lambda_vector=np.dot(np.linalg.inv(robot_matrix),difference_vector)
        except LinAlgError: 
            return None,False
        l1,l2=lambda_vector
        
        
        return l1,(l1>=0 and l2>=0 and l2<=10)

        
                   
def measure_distance_front(robot_vector):
        """Measures (in a simulated way) turtle distance from the wall he is heading to

        Args:
            robot_vector (numpy vector): [x,y,theta] vector of turtle position and orientation

        Returns:
            float: The distance from the wall he is heading to
        """
        distances = []
        for wall in walls:
            l,valid =measure_single_wall(robot_vector,wall)
            distances.append(l) 
            if valid:
                return l
        return 0 
        



        
    
class RoombaComm():
    """Communiction of our simulator with ROS"""

    def __init__(self,turtle_name="turtle1"):
        
        turtle_name=rospy.get_param('turtle_name', 'turtle1')
        self.position_subscriber=rospy.Subscriber(turtle_name+"/pose",Pose,self.read_pose)
        self.speed_publisher = rospy.Publisher(turtle_name+"/cmd_vel",Twist,queue_size=10)
        self.distance_publisher= rospy.Publisher(turtle_name+"/distance",Range,queue_size=10)
        
        self._latch=False
        
    def latching_generator(self,value,n):
        ''' Gives n times a value and then 0 for the rest of time
        
        Args:
            value: the value on which to latch the angular speed
            n: for how many generations to latch
            
        Yields:
            the stream of touples x_speed, angular_speed, when latched -0.5, value else: 1,0'''
        self._latch=True
        for x in range(n):
            yield -0.5,value
        self._latch=False
        
        while(True):
            yield 1,0
        

                 
    def latching_controller(self,distance):
        '''The controler for turle. Will rotate for some time when distance is less then 1
        drive stright otherwise.
        '''
        
        cmd_message=Twist()


        if(distance<=1):
            if( not self._latch):
                self.latcher=self.latching_generator(random.uniform(1,10),10)
        try:
            linear,angular=next(self.latcher)       
        except:
            linear,angular=1,0
                
        cmd_message.linear.x=linear
        cmd_message.angular.z=angular    
        self.speed_publisher.publish(cmd_message)



            
    def read_pose(self,pos):
        '''Callback when new pose topic has come. Updates distance and control signals'''
        distance=measure_distance_front((pos.x,pos.y,pos.theta)) 
        
  
        
        range_message=Range()
        
        range_message.header.stamp = rospy.Time.now()
        
        range_message.field_of_view=0.1
        range_message.min_range=0
        range_message.max_range=10
        range_message.range=distance
        
        self.distance_publisher.publish(range_message)
        
        
        self.latching_controller(distance)


####
