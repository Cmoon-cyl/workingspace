#!/usr/bin/env python3
# coding: utf-8

import rospy
from cmoon_msgs.srv import cmoon, cmoonRequest, cmoonResponse


class Main:
    def __init__(self, name):
        rospy.init_node(name, anonymous=True)
        send_sum = rospy.ServiceProxy('add', cmoon)
        try:
            rospy.wait_for_service('add', timeout=5)
        except rospy.ROSException:
            print('Service done.')

        # num = cmoonRequest(1, 2)
        # sum = send_sum(num)

        # num = cmoonRequest()
        # num.num1 = 4
        # num.num2 = 5
        # sum = send_sum(num)

        sum = send_sum(3, 7)

        print(sum.sum)


if __name__ == '__main__':
    try:
        Main('send_num')
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo("Keyboard interrupt.")
