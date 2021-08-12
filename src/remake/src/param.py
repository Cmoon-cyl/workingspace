#!/usr/bin/env python3
# coding: utf-8

import rospy


class Main:
    def __init__(self, name):
        rospy.init_node(name)
        rospy.init_node(name)


if __name__ == '__main__':
    try:
        Main('send_num')
    except rospy.ROSInterruptException:
        rospy.loginfo("Keyboard interrupt.")
