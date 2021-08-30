#!/usr/bin/python
# coding: UTF-8 

import rospy
import tf2_ros
from tf import transformations as tf
from tf2_geometry_msgs import tf2_geometry_msgs
from geometry_msgs.msg import TransformStamped, PointStamped
from nav_msgs.msg import Odometry
from cmoon_msgs.msg import Point, Pose


class Transformer:
    def __init__(self):
        rospy.Subscriber('/yolo_result', Point, self.kinect2map, queue_size=10)
        self.show_point = rospy.Publisher('/clicked_point', PointStamped, queue_size=10)
        self.buffer = tf2_ros.Buffer()  # 创建缓存对象
        self.sub = tf2_ros.TransformListener(self.buffer)  # 创建订阅对象,将缓存对象传入
        self.pose = Pose()
        self.point_show = PointStamped()

    def kinect2map(self, point):
        self.dynamic_sub('kinect', 'map', point)

    def dynamic_pub(self, father, child, point):
        pub = tf2_ros.TransformBroadcaster()  # 创建发布坐标系相对关系的对象
        ts = TransformStamped()
        # 被转换的坐标系相对关系消息
        ts.header.frame_id = father
        ts.header.stamp = rospy.Time.now()
        ts.child_frame_id = child
        # 子坐标系相对于父坐标系的偏移量
        ts.transform.translation.x = point.px
        ts.transform.translation.y = point.py
        ts.transform.translation.z = point.pz
        ts.transform.rotation.x = point.ox
        ts.transform.rotation.y = point.oy
        ts.transform.rotation.z = point.oz
        ts.transform.rotation.w = point.ow
        pub.sendTransform(ts)

    def dynamic_sub(self, now_tf, aim_tf, point):
        ps = tf2_geometry_msgs.PointStamped()
        ps.header.stamp = rospy.Time()
        ps.header.frame_id = now_tf
        ps.point.x = point.x
        ps.point.y = point.y
        ps.point.z = point.z
        rate = rospy.Rate(100)
        while not rospy.is_shutdown():
            try:
                result = self.buffer.transform(ps, aim_tf)
                rospy.loginfo('{},{},{}'.format(result.point.x, result.point.y, result.point.z))
                self.point_show.header.frame_id = 'map'
                self.point_show.point.x = result.point.x
                self.point_show.point.y = result.point.y
                self.point_show.point.z = result.point.z
                self.show_point.publish(self.point_show)
                break
            except Exception as e:
                rospy.logwarn('TfError:%s', e)


if __name__ == '__main__':
    try:
        rospy.init_node('tf_transformer', anonymous=True)
        Transformer()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
