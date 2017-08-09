#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Int32

def talker():
    pub = rospy.Publisher('just_one', Int32, queue_size=10)
    rospy.init_node('just_one_talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "just one publisher is live %s" % rospy.get_time()
        #rospy.loginfo_once(hello_str)
        pub.publish(1)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
