#!/usr/bin/python
# coding: UTF-8 

import rospy
import tf2_ros
from tf import transformations as tf
from tf2_geometry_msgs import tf2_geometry_msgs
from geometry_msgs.msg import TransformStamped
from nav_msgs.msg import Odometry


class Transformer:
    def __init__(self):
        rospy.Subscriber('/odom', Odometry, self.base2map)
        self.buffer = tf2_ros.Buffer()  # 创建缓存对象
        self.sub = tf2_ros.TransformListener(self.buffer)  # 创建订阅对象,将缓存对象传入

    def base2map(self, point):
        base = tf2_geometry_msgs.PointStamped()
        base.header.stamp = rospy.Time()
        base.header.frame_id = 'base_link'
        base.point.x = point.pose.pose.position.x
        base.point.y = point.pose.pose.position.y
        base.point.z = point.pose.pose.position.z
        map = self.buffer.transform(base, 'map')
        rospy.loginfo('{},{},{}'.format(map.point.x, map.point.y, map.point.z))


if __name__ == '__main__':
    try:
        rospy.init_node('tf_transformer', anonymous=True)
        Transformer()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
