#!/usr/bin/env python
# coding: UTF-8 

import rospy
from std_msgs.msg import String
from nav_msgs.msg import Odometry


class Main:
    def __init__(self, name):
        rospy.init_node(name, anonymous=True)
        self.pub = rospy.Publisher('/test1', String, queue_size=10)
        self.pub.publish('dddd')
        rospy.Subscriber('/tf', Odometry, self.call)

    def call(self, agv):
        x = agv.data


if __name__ == '__main__':
    try:
        Main('name')
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
