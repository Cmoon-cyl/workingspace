#!/usr/bin/env python3
# coding: UTF-8 

import rospy
from Detector import BodyDetector, FaceDetector
from std_msgs.msg import String


class Main:
    def __init__(self):
        rospy.Subscriber('/detect', String, self.callback)
        self.body = BodyDetector()
        self.face = FaceDetector()

    def callback(self, msg):
        if msg.data == 'face':
            pass


if __name__ == '__main__':
    try:
        rospy.init_node('name', anonymous=True)
        Main()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
