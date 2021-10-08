#!/usr/bin/env python
# coding: UTF-8 

import rospy
from aip import AipBodyAnalysis


class Body:
    def __init__(self):
        APP_ID = '24949761'
        API_KEY = '02d2yaps6uEDgOGRzMqs9Ggo'
        SECRET_KEY = 'NBDdIGGZtrLvCoi6aMxZ1Qd2uELcLiGU'
        self.client = AipBodyAnalysis(APP_ID, API_KEY, SECRET_KEY)

    def get_file_content(self, filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    def get_body(self):
        image = self.get_file_content('/home/cmoon/图片/photo.jpg')

        """ 调用人体检测与属性识别 """
        self.client.bodyAttr(image)

        """ 如果有可选参数 """
        options = {}
        options["type"] = "gender,age,glasses,upper_color,upper_wear"

        """ 带参数调用人体检测与属性识别 """
        result = self.client.bodyAttr(image, options)
        print(result)


if __name__ == '__main__':
    body = Body()
    body.get_body()
