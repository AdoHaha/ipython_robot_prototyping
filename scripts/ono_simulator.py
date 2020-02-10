#!/usr/bin/python3
# license removed for brevity
import rospy
from std_msgs.msg import Int32



from sensor_msgs.msg import JointState

from std_msgs.msg import String
import random



def simulator():
    pub = rospy.Publisher('just_one', Int32, queue_size=10)
    ono_state=rospy.Publisher("Ono/joint_state",JointState,queue_size=10)


    secret_publisher = rospy.Publisher('Ono/secret_message', String, queue_size=10)
    super_secret_publisher = rospy.Publisher('Ono/tfdsfu_nfttbhf_2', String, queue_size=10)
    super_secret="wow, you have even found the super secret one, 	dpohsbuvmbujpot ;)"
    
    rospy.init_node('just_one_talker', anonymous=True)
    rate = rospy.Rate(5) # 10hz
 
    
    while not rospy.is_shutdown():
    
        # creating joints message
        joints=JointState()
        joints.position=[random.uniform(0,10) for x in range(5)] 
        joints.name=["eye","eye_lid","hand","right_leg","left_leg"]
        
        secret_message = "This is a secret message from Ono. If you have read it, congratulations! %s" % rospy.get_time()
        
        
        hello_str = "just one publisher is live %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(1)
        secret_publisher.publish(secret_message)
        super_secret_publisher.publish(super_secret)
        
        ono_state.publish(joints)
        rate.sleep()

if __name__ == '__main__':
    try:
        simulator()
    except rospy.ROSInterruptException:
        pass
