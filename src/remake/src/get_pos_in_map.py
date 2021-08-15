#! /usr/bin/env python
# coding: utf-8
# Created by Cmoon
import rosparam
import rospy
import tf
from tf import transformations as ts
from cmoon_msgs.msg import location


class Sendpos:
    def __init__(self, name):
        rospy.init_node(name)
        tflistener = tf.TransformListener()
        tflistener.waitForTransform('/map', '/base_footprint', rospy.Time(), rospy.Duration(4.0))
        while not rospy.is_shutdown():
            try:
                (trans, rot) = tflistener.lookupTransform('/map', '/base_footprint', rospy.Time(0))
                eu = ts.euler_from_quaternion(rot)
            except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
                rospy.logerr('Error occure when transfrom.')
                return
            rospy.set_param('x', trans[0])
            rospy.set_param('y', trans[1])
            rospy.set_param('theta', eu[2])
            # print('[{},{},{}],[{},{},{},{}]'.format(trans[0], trans[1], trans[2], rot[0], rot[1], rot[2], rot[3]))
            print('[{},{},{}]'.format(trans[0], trans[1], eu[2]))


if __name__ == '__main__':
    try:
        Sendpos('get_pos_in_map')
    except rospy.ROSInterruptException:
        rospy.loginfo(" node terminated.")
