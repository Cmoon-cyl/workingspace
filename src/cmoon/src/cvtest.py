#!/usr/bin/env python3
# coding: UTF-8 

import cv2
import rospy
import numpy as np
from sensor_msgs.msg import Image


class Main:
    def __init__(self):
        rospy.init_node('cv_test')
        rospy.Subscriber('/k4a/rgb/image_raw', Image, self.process, queue_size=1, buff_size=52428800)
        self.im0 = None

    def process(self, image):
        img = np.frombuffer(image.data, dtype=np.uint8).reshape(image.height, image.width, -1)
        self.im0 = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        self.show(self.im0)

    def show(self, img):
        cv2.namedWindow('yolo', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('yolo', 720, 500)
        cv2.startWindowThread()
        cv2.imshow('yolo', img)
        cv2.waitKey(1)

    def load_module(self):
        pass


if __name__ == '__main__':
    Main()
    rospy.spin()
