#!/usr/bin/env python
# coding: UTF-8 

import rospy
import tf2_ros
from tf import transformations as tf
from tf2_geometry_msgs import tf2_geometry_msgs
from geometry_msgs.msg import TransformStamped
from nav_msgs.msg import Odometry


class Transformer:
    def __init__(self):
        self.buffer = tf2_ros.Buffer()
        self.sub = tf2_ros.TransformListener(self.buffer)
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
