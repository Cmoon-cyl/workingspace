#!/usr/bin/env python
# coding: UTF-8 

import rospy
import tf2_ros
from geometry_msgs.msg import TransformStamped
from tf import transformations as tf


class Main:
    def __init__(self, name):
        rospy.init_node(name, anonymous=True)
        self.pub = tf2_ros.StaticTransformBroadcaster()
        self.ts = TransformStamped()
        self.ts.header.stamp = rospy.Time.now()
        self.ts.header.frame_id = 'base_link'
        self.ts.child_frame_id = 'laser'

        self.ts.transform.translation.x = 2.0
        self.ts.transform.translation.y = 3.0
        self.ts.transform.translation.z = 4.0

        self.qtn = tf.quaternion_from_euler(0, 0, 0)
        self.ts.transform.rotation.x = self.qtn[0]
        self.ts.transform.rotation.y = self.qtn[1]
        self.ts.transform.rotation.z = self.qtn[2]
        self.ts.transform.rotation.w = self.qtn[3]

        self.pub.sendTransform(self.ts)


if __name__ == '__main__':
    try:
        Main('tf_publisher')
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
