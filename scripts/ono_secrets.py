#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('Ono/secret_message', String, queue_size=10)
    pub2 = rospy.Publisher('Ono/tfdsfu_nfttbhf_2', String, queue_size=10)
    rospy.init_node('ono_secrets', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    super_secret="wow, you have even found the super secret one, 	dpohsbuvmbujpot ;)"
    while not rospy.is_shutdown():
        hello_str = "This is a secret message from Ono. If you have read it, congratulations! %s" % rospy.get_time()
        
        
        #rospy.loginfo_once(hello_str)
        pub.publish(hello_str)
        pub2.publish(super_secret)
        rate.sleep()



if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
