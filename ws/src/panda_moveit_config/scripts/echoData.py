#!/usr/bin/env python
import rospy
from sensor_msgs.msg import JointState
# dale
def callback(data):
    rospy.loginfo(data.position)
    rospy.loginfo(data.velocity)
    
def listener():
    rospy.init_node('echo_joint_data', anonymous=True)
    rospy.Subscriber("/joint_states", JointState, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()