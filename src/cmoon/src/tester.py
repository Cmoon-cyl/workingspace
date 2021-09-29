#!/usr/bin/env python
# coding: UTF-8 

import rospy


class Main:
    def __init__(self):
        self.a = [i for i in range(10)]
        print(self.a)
        self.keep()

    def keep(self):
        while not rospy.is_shutdown():
            print('hi')


if __name__ == '__main__':
    try:
        rospy.init_node('name', anonymous=True)
        Main()
    except rospy.ROSInterruptException:
        rospy.loginfo('Interrupt happened')
        print('Interrupt')
