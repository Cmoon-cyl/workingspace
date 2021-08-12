#!/usr/bin/env python3
# coding: utf-8

import rospy
from cmoon_msgs.srv import cmoon, cmoonResponse


class Sum:
    def __init__(self, name):
        rospy.init_node(name)
        rospy.Service('add', cmoon, self.returnsum)
        rospy.loginfo('Service on')
    def returnsum(self, req):
        num1 = req.num1
        num2 = req.num2
        sum = num1 + num2
        response = cmoonResponse()
        response.sum = sum
        return response


if __name__ == '__main__':
    try:
        Sum('get_num')
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo("Keyboard interrupt.")
