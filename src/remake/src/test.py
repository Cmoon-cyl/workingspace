#!/usr/bin/env python
# coding: UTF-8 

import rospy
import tf

class Main:
    def __init__(self, name):
        rospy.init_node(name, anonymous=True)


if __name__ == '__main__':
    try:
        Main('name')
    except rospy.ROSInterruptException:
        pass
