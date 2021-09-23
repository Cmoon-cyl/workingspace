#!/usr/bin/env python
# coding: UTF-8 
# Created by Cmoon

import rospy
from std_msgs.msg import String
from soundplayer import Soundplayer
from pdfmaker import Pdfmaker

NAME = {
    'paul': ['paul', 'poor', 'pull', 'pool', 'ball'],
    'john': ['john', 'joy', 'join', 'joe'],
    'george': ['george', 'joy', 'joe', 'living room', 'draw'],
    'ringo': ['ringo', 'bingo', 'win', 'win go', 'Bingo'],
    'alice': ['alice', 'alex'],
    'linda': ['linda', 'in love'],
}


class Recognizer:
    def __init__(self):
        rospy.Subscriber('/xfspeech', String, self.talkback)
        self.wakeup = rospy.Publisher('/xfwakeup', String, queue_size=10)
        self.start_signal = rospy.Publisher('/name', String, queue_size=10)
        self.cmd = None
        self.namelist = NAME
        self.name = ''
        self._soundplayer = Soundplayer()
        self._pdfmaker = Pdfmaker()
        self.status = 0
        self.key = 1

    def talkback(self, msg):
        if self.key == 1:
            print("\n讯飞读入的信息为: " + msg.data)
            self.cmd = self.processed_cmd(msg.data)
            self.judge()

    def judge(self):
        response = self.analyze()
        if response == 'I have caught ':
            self._soundplayer.say("Please say your name again. ")
            self.get_cmd()
        else:
            self.status = 1
            print(response)
            self._soundplayer.say(response)
            self._soundplayer.say("You were eliminated.", 2)
            print('You were eliminated.')
            self.start_signal.publish(self.name)

    def processed_cmd(self, cmd):
        cmd = cmd.lower()
        for i in " ,.;?":
            cmd = cmd.replace(i, ' ')
        return cmd

    def get_name(self):
        """获取一次命令"""
        self._soundplayer.play('Speak.')
        self.wakeup.publish('ok')

    def analyze(self):
        response = 'I have caught '
        for (key, val) in self.namelist.items():
            for word in val:
                if word in self.cmd:
                    self.name = key
                    response = response + key + '?'
                    break
        return response


if __name__ == '__main__':
    try:
        rospy.init_node('voice_recognition')
        Recognizer()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
