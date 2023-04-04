#!/usr/bin/env python
import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
import json

def jsonw(msg,a):
    dictionary = msg
    json_object = json.dumps(dictionary, indent = 4)
    with open(a, "w") as outfile:
        outfile.write(json_object)

def callback(msg):
    rospy.loginfo("d: %s",msg.position)
    dict = {
        "name": msg.name,
        "position": msg.position,
        "velocity": msg.velocity,
        "effort": msg.effort,
    }
    jsonw(dict,"sample2.json")

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('joint_listener', anonymous=True)
    rospy.Subscriber("/joint_states", JointState , callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
    