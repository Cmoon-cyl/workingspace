#!/usr/bin/python
# coding: UTF-8 

import rospy
import tf2_ros
from tf import transformations as tf
from tf2_geometry_msgs import tf2_geometry_msgs
from geometry_msgs.msg import TransformStamped
from nav_msgs.msg import Odometry
from cmoon_msgs.msg import Point


class Transformer:
    def __init__(self):
        rospy.Subscriber('/odom', Odometry, self.base2map)
        rospy.Subscriber('/yolo_result', Point, self.kinect2base)
        self.buffer_base = tf2_ros.Buffer()  # 创建缓存对象
        self.buffer_kinect = tf2_ros.Buffer()  # 创建缓存对象
        self.sub_base = tf2_ros.TransformListener(self.buffer_base)  # 创建订阅对象,将缓存对象传入
        self.sub_kinect = tf2_ros.TransformListener(self.buffer_kinect)  # 创建订阅对象,将缓存对象传入

    def base2map(self, point):
        base = tf2_geometry_msgs.PointStamped()
        base.header.stamp = rospy.Time()
        base.header.frame_id = 'base_link'
        base.point.x = point.pose.pose.position.x
        base.point.y = point.pose.pose.position.y
        base.point.z = point.pose.pose.position.z
        map = self.buffer_base.transform(base, 'map')
        rospy.loginfo('{},{},{}'.format(map.point.x, map.point.y, map.point.z))

    def kinect2base(self, point):
        kinect = tf2_geometry_msgs.PointStamped()
        kinect.header.stamp = rospy.Time()
        kinect.header.frame_id = 'kinect'
        kinect.point.x = point.x
        kinect.point.y = point.y
        kinect.point.z = point.z

    def dynamic_pub(self, frame):
        pub = tf2_ros.TransformBroadcaster()  # 创建发布坐标系相对关系的对象
        ts = TransformStamped()  # 组织被转换的坐标系相对关系消息
        ts.header.frame_id = frame
        ts.header.stamp = rospy.Time()
        

if __name__ == '__main__':
    try:
        rospy.init_node('tf_transformer', anonymous=True)
        Transformer()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
