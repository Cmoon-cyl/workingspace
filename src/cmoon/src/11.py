#!/usr/bin/env python
# coding: UTF-8 

import rospy


class Main:
    def __init__(self):
        pass


if __name__ == '__main__':
    try:
        rospy.init_node('name', anonymous=True)
        Main()
    except rospy.ROSInterruptException:
        pass
