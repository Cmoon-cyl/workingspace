#!/usr/bin/env python
# -*- coding: utf-8 -*-


import rospy
from turtlesim.srv import Spawn


def turtle_spawn():
    rospy.init_node('turtle_spawn')

    rospy.wait_for_service('/spawn')

    try:
        add_turtle = rospy.ServiceProxy('/spawn', Spawn)
        res = add_turtle(2.0, 2.0, 0.0, 'turtle2')
        return res.name
    except rospy.ServiceException:
        print ('Service call failed!')


if __name__ == "__main__":
    # print (Spawn turtle successfully [name:%s]) % (turtle_spawn()))
