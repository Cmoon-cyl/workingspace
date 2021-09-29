#!/usr/bin/env python
# coding: UTF-8 
# Created by Cmoon

import rospy
from navigator import Navigator  # 导航模块
from soundplayer import Soundplayer  # 语音合成模块
from voice_recognizer_ly import Recognizer  # 语音识别模块和分析模块
from base_controller import Base  # 底盘运动模块
from std_msgs.msg import String  # String类型消息,从String.data中可获得信息
import re
import time
import threading

# [[1.90381698705,0.138296546125,0.0],[0.0,0.0,0.98442873708,0.175784133561]] --1
# [-2.73629320294,-0.232648592888,0.0],[0.0,0.0,-0.990913615965,0.134499835296]
LOCATION = {  # 储存导航路径点
    'room': [[-1.31255235434, 1.11784048026, 0.0], [0.0, 0.0, -0.367150217691, 0.930161662105]],
    'door': [[-2.8414547504, -0.317361136433, 0.0], [0.0, 0.0, -0.904963276206, 0.425489681095]],
}


class Controller:
    def __init__(self, name):
        rospy.init_node(name, anonymous=True)  # 初始化ros节点
        self.navigator = Navigator(LOCATION)  # 实例化导航模块
        self.soundplayer = Soundplayer()  # 实例化语音合成模块
        rospy.Subscriber('/xfspeech', String, self.talkback)
        self.wakeup = rospy.Publisher('/xfwakeup', String, queue_size=10)  # 发布
        self.base = Base()  # 实例化移动底盘模块
        tim = threading.Timer(20, self.fun_time)
        self.status = False
        self.t1 = 0
        tim.start()
        self.soundplayer.say("Hello ,this is coco.")
        self.wakeup.publish('ok')

    def fun_time(self):
        if (time.time() - self.t1 > 20):
            self.soundplayer.say("next commend")
            self.wakeup.publish('ok')

    def talkback(self, msg):
        self.cmd = msg.data  # 先进制造
        self.time = time.time()
        if self.cmd != None:
            str_ = self.cmd.lower()
            if str_.find("introduce") != -1 and str_.find("yourself") != -1 or str_.find("name") != -1:
                self.soundplayer.say("My name is coco.")
            elif str_.find("from") != -1:
                self.soundplayer.say("I come from China, I am a number of strive team.")
                rospy.sleep(10)
            elif str_.find("dead") != -1:
                self.soundplayer.say("I am very angry.")
                rospy.sleep(10)
            elif str_.find("come in") != -1:
                self.navigator.goto("room")
                rospy.sleep(10)
            elif str_.find("door") != -1:
                self.navigator.goto("door")
            else:
                rospy.sleep(25)
        self.soundplayer.say("Next commend.")
        self.wakeup.publish('ok')


if __name__ == '__main__':
    control = Controller('nav_control')
    rospy.spin()
