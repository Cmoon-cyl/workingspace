#!/usr/bin/env python
# coding: utf-8

import rospy
from cmoon_msgs.srv import cmoon, cmoonRequest, cmoonResponse
import sys


class Main:
    def __init__(self, name):
        rospy.init_node(name, anonymous=True)
        client = rospy.ServiceProxy('add', cmoon)
        client.wait_for_service(timeout=5)
        rospy.loginfo('Request completed.')
        if len(sys.argv) == 3:
            num1 = int(sys.argv[1])
            num2 = int(sys.argv[2])
            response = client.call(num1, num2)
            print(response.sum)
        else:
            while not rospy.is_shutdown():
                num1 = int(input('num1: '))
                num2 = int(input('num2: '))
                response = client.call(num1, num2)
                print(response.sum)

        # num = cmoonRequest(1, 2)
        # sum = send_sum(num)

        # num = cmoonRequest()
        # num.num1 = 4
        # num.num2 = 5
        # sum = send_sum(num)


if __name__ == '__main__':
    try:
        Main('send_num')
    except rospy.ROSInterruptException:
        rospy.loginfo("Keyboard interrupt.")
