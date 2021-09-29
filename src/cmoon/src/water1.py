#!/usr/bin/env python
# coding: UTF-8
# Created by Cmoon

import rospy
from std_msgs.msg import String
from soundplayer import Soundplayer
from pdfmaker import Pdfmaker
from navigator import Navigator  # 导航模块
import time

COMMAND = {
    'introduce': ['name', 'introduce', 'yourself'],
    'from': ['from', 'where'],
    'in': ['here', 'come here'],
    'out': ['back', 'go back'],
    'handsome': ['handsome', 'handsame'],
    'date': ['date', 'day', 'days', 'data'],
    'people': ['human', 'people', 'paper', 'human being']
}

LOCATION = {  # 储存导航路径点
    'you': [[5.493321, -0.543651, 0.000000], [0.000000, 0.000000, 0.970636, -0.240553]],
    'my home': [[3.768458, -3.502853, 0.000000], [0.000000, 0.000000, 0.258183, 0.966096]],
    # 'room': [[-0.476640, -4.946882, 0.000000], [0.000000, 0.000000, 0.808888, 0.587962]],
    # 'door': [[-4.352973, -6.186659, 0.000000], [0.000000, 0.000000, -0.202218, -0.979341]],
}


class Recognizer:
    def __init__(self):
        rospy.Subscriber('/xfspeech', String, self.talkback)
        self.wakeup = rospy.Publisher('/xfwakeup', String, queue_size=10)
        self.start_signal = rospy.Publisher('/start_signal', String, queue_size=10)
        self.navigator = Navigator(LOCATION)  # 实例化导航模块
        self.cmd = None
        self.command = COMMAND
        self.location = LOCATION
        self.goal = ''
        self._soundplayer = Soundplayer()
        self._pdfmaker = Pdfmaker()
        self.status = 0
        self.key = 1
        self.mode = None
        self.cnt = 0
        self._soundplayer.say('Hello,this is jack.', 2)
        self._soundplayer.say('What do you want for me.', 2)
        self.get_cmd()

    def talkback(self, msg):
        if self.key == 1:
            print("\n讯飞读入的信息为: " + msg.data)
            self.cmd = self.processed_cmd(msg.data)
            self.judge()

    def judge(self):
        response = self.analyze()
        if response == '':
            if self.cnt >= 3:
                self._soundplayer.say("your english is so bad", 2)
                self._soundplayer.say("do not communicate with me ", 3)
                self._soundplayer.say("change someone else to talk with me", 3)
                self.cnt = 0
            self.cnt += 1
            self._soundplayer.say("Please say the request again.")
            self.get_cmd()
        elif response == 'introduce':  # What's your name?/ Who are you?
            print(response)
            self._soundplayer.say('My name is jack.', 2)
            self._soundplayer.say('I am a emotionless robot killer.', 2)
            self._soundplayer.say('I am a number of the strive team', 3)
            self._soundplayer.say('I like playing football', 3)
            self._soundplayer.say('I like playing football', 3)
            self._soundplayer.say("What's your next request?", 2)
            self.get_cmd()
        elif response == 'from':  # Where are you from?
            print(response)
            self._soundplayer.say('I come from China.', 6)
            self._soundplayer.say("What's your next request?", 3)
            self.get_cmd()
        elif response == 'in':  # Come in.
            print(response)
            self._soundplayer.say('Ok,i will get to you.', 3)
            self.navigator.goto('you')
            self._soundplayer.say("What's your next request?", 2)
            self.get_cmd()
        elif response == 'out':  # Get out.
            print(response)
            self._soundplayer.say('Ok,i will get back.', 3)
            self.navigator.goto('my home')
        elif response == 'date':
            array = time.localtime(time.time())
            oth = time.strftime("%Y--%m--%d %H:%M:%S", array)
            strs = oth.split(' ')[0].split("--")
            str = 'Today is September the twenty eighth.'
            self._soundplayer.say(str, 3)
            self._soundplayer.say("What's your next request?", 2)
            self.get_cmd()
        elif response == 'handsome':
            self._soundplayer.say('It must be our leader professor shenzhi Huang.', 5)
            self._soundplayer.say("What's your next request?", 2)
            self.get_cmd()
        elif response == 'people':
            self._soundplayer.say("don't ask me", 3)
            self._soundplayer.say("i just want to kill", 1)
            self._soundplayer.say("all the people in this room", 4)
            self._soundplayer.say("activating killing mode?", 10)
            self._soundplayer.say("assessing task difficulty", 2)
            self._soundplayer.say("too difficult.  Give up the task", 3)
            self._soundplayer.say("What's your next request?", 2)
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
        for (key, val) in self.command.items():
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
