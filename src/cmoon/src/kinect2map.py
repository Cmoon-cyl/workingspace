#!/usr/bin/env python
# coding: UTF-8 

import rospy
from nav_msgs.msg import Odometry
from std_msgs.msg import String


class Transformer:
    def __init__(self):
        rospy.Subscriber('/odom', Odometry, self.callback)
        self.pub = rospy.Publisher('/test', String, queue_size=10)
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0

    def callback(self, point):
        self.x = point.pose.pose.position.x
        self.y = point.pose.pose.position.y
        self.z = point.pose.pose.position.z
        rospy.loginfo('{},{},{}'.format(self.x, self.y, self.z))
        self.pub.publish('ok')


if __name__ == '__main__':
    try:
        rospy.init_node('transformer', anonymous=True)
        transformer = Transformer()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
