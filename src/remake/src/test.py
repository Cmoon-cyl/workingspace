#!/usr/bin/env python
# coding: UTF-8 

import rospy


class Main:
    def __init__(self, name):

        self.num = 2
        if 0 < self.num < 4:
            print(self.num)
        else:
            print('no')


if __name__ == '__main__':
    try:
        Main('name')
    except rospy.ROSInterruptException:
        pass
