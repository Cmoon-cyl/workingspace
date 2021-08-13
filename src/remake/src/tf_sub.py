#!/usr/bin/env python
# coding: UTF-8 

import rospy
import tf2_ros
from tf2_geometry_msgs import tf2_geometry_msgs


class Main:
    def __init__(self, name):
        rospy.init_node(name, anonymous=True)
        self.buffer = tf2_ros.Buffer()
        self.sub = tf2_ros.TransformListener(self.buffer)
        self.point = tf2_geometry_msgs.PointStamped()
        self.point.header.stamp = rospy.Time.now()
        self.point.header.frame_id = 'laser'
        self.point.point.x = 3.0
        self.point.point.y = 4.0
        self.point.point.z = 5.0
        self.rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            try:
                output = self.buffer.transform(self.point, 'base_link')
                rospy.loginfo(output.point)
            except Exception as e:
                rospy.logwarn('no base_link')
            self.rate.sleep()


if __name__ == '__main__':
    try:
        Main('tf_sub')
    except rospy.ROSInterruptException:
        pass
