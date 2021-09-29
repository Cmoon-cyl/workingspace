#!/usr/bin/env python
# coding: UTF-8
# Created by Cmoon

import rospy
from std_msgs.msg import String
from soundplayer import Soundplayer
from pdfmaker import Pdfmaker

LOCATION = {
    'name': ['name'],
    'from': ['from', 'where'],
    'in': ['come', 'come in'],
    'out': ['out'],
}


class Recognizer:
    def __init__(self):
        rospy.Subscriber('/xfspeech', String, self.talkback)
        self.wakeup = rospy.Publisher('/xfwakeup', String, queue_size=10)
        self.start_signal = rospy.Publisher('/start_signal', String, queue_size=10)
        self.cmd = None
        self.location = LOCATION
        self.goal = ''
        self._soundplayer = Soundplayer()
        self._pdfmaker = Pdfmaker()
        self.status = 0
        self.key = 1
        self.mode = None
        self._soundplayer.say('Hello,this is coco.What do you want for me.')

    def talkback(self, msg):
        if self.key == 1:
            print("\n讯飞读入的信息为: " + msg.data)
            self.cmd = self.processed_cmd(msg.data)
            self.judge()

    def judge(self):
        response = self.analyze()

        if response == '':
            self._soundplayer.say("Please say your request again. ")
            self.get_cmd()
        elif response == 'name':
            print(response)
            self._soundplayer.say('My name is coco.', 3)
            self._soundplayer.say("What's your next request?", 3)
            self.get_cmd()
        elif response == 'from':
            print(response)
            self._soundplayer.say('I come from China, I am a number of strive team.', 6)
            self._soundplayer.say("What's your next request?", 3)
            self.get_cmd()
        elif response == 'in':
            print(response)
            self._soundplayer.say('Ok,i will get in.', 3)

            self._soundplayer.say("What's your next request?", 3)
            self.get_cmd()

    def processed_cmd(self, cmd):
        cmd = cmd.lower()
        for i in " ,.;?":
            cmd = cmd.replace(i, ' ')
        return cmd

    def get_cmd(self):
        """获取一次命令"""
        self._soundplayer.play('Speak.')
        self.wakeup.publish('ok')

    def analyze(self):
        response = ''
        for (key, val) in self.location.items():
            for word in val:
                if word in self.cmd:
                    response = key
                    break
        return response


if __name__ == '__main__':
    try:
        rospy.init_node('voice_recognition')
        Recognizer()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
