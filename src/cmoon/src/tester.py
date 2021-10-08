#!/usr/bin/env python3
# coding: UTF-8 

import rospy
from Detector import FaceDetector, BodyDetector


class Tester:
    def __init__(self):
        self.face = FaceDetector()
        self.body = BodyDetector()

    def test(self):
        result = self.body.detect(
            ['age', 'gender', 'upper_wear', 'upper_wear_texture', 'upper_wear_fg', 'upper_color',
             'lower_wear', 'lower_color', 'face_mask', 'glasses', 'headwear', 'bag'])
        # result=self.face.get_attr('/home/cmoon/workingspace/src/cmoon/photo/photo.jpg', ['age','gender'])
        # result=self.body.get_attr('/home/cmoon/workingspace/src/cmoon/photo/photo.jpg', ['age','gender'])

        print(result)


if __name__ == '__main__':
    try:
        rospy.init_node('name', anonymous=True)
        tester = Tester()
        tester.test()
    except rospy.ROSInterruptException:
        pass
