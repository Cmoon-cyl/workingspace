#!/usr/bin/env python
# coding: UTF-8 
# Created by Cmoon

import rospy
from std_msgs.msg import String
from soundplayer import Soundplayer
from pdfmaker import Pdfmaker

NAME = {
    'Tom': ['tom', 'town', 'top'],
    'Lucy': ['lucy'],
    'Mike': ['mike', 'make', 'mikey', 'mark', 'like', 'Michael'],
    'Marry': ['marry'],
    'Grape': ['grape']
}

DRINK = {
    'milk': ['milk', 'look', 'book'],
    'beer': ['beer'],
    'cola': ['cola'],
    'wine': ['wine'],
    'juice': ['juice'],
    'tea': ['tee', 'tea']
}


class Recognizer:
    def __init__(self):
        rospy.Subscriber('/xfspeech', String, self.talkback)
        self.wakeup = rospy.Publisher('/xfwakeup', String, queue_size=10)
        self.start_signal = rospy.Publisher('/start_signal', String, queue_size=10)
        # self.stop_signal = rospy.Publisher('/stop_signal', String, queue_size=10)
        self.person_name = rospy.Publisher('/name', String, queue_size=10)
        self.person_drink = rospy.Publisher('/drink', String, queue_size=10)
        self.cmd = None
        self.stop = None
        self.name = NAME
        self.people = ''
        self.drink = DRINK
        self.need = ''
        self._soundplayer = Soundplayer()
        self._pdfmaker = Pdfmaker()
        self.status = 0
        self.key = 1

    def talkback(self, msg):
        if self.key == 1:
            # print(msg.data)
            # self.stop = self.processed_cmd(msg.data)
            # if ('stop' in self.stop) or ('shut up' in self.stop) or ('shop' in self.stop):
            #     self.stop_signal.publish('stop')
            #     print('pub stop')
            #     self.key = 1

            # else:
            print("\n讯飞读入的信息为: " + msg.data)
            self.cmd = self.processed_cmd(msg.data)
            self.judge()

    def judge(self):
        if self.status == 0:
            response = self.analyze()
            if response == 'Are you ':
                self._soundplayer.say("Please say the command again.")
                self.get_cmd()
            else:
                self.status = 1
                print(response)
                self._soundplayer.say(response, 4)
                self._soundplayer.say("please say yes or no.", 1)
                print('Please say yes or no.')
                self.get_cmd()

        elif ('Yes.' in self.cmd) or ('yes' in self.cmd) or ('Yeah' in self.cmd) or ('yeah' in self.cmd) and (
                self.status == 1):

            self._soundplayer.say('Ok, I will.')
            self._pdfmaker.write('Cmd: Are you ' + self.people + ' and do you want to have' + self.need + '?')
            self._pdfmaker.write('Respond: Ok,I know.')
            print('Ok, I know.')
            self.start_signal.publish(self.need)
            self.key = 0
            self.status = 0
            self.people = ''
            self.need = ''


        elif ('No.' in self.cmd) or ('no' in self.cmd) or ('oh' in self.cmd) or ('know' in self.cmd) and (
                self.status == 1):

            self._soundplayer.say("Please say the command again. ")
            print("Please say the command again. ")
            self.status = 0
            self.people = ''
            self.get_cmd()
        else:
            self._soundplayer.say("please say yes or no.")
            print('Please say yes or no.')
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
        response = 'Are you '
        for (key, val) in self.name.items():
            for word in val:
                if word in self.cmd:
                    self.people = key
                    response = response + key + ' and do you want to have '
                    self.person_name.publish(self.people)
                    break
        for (key, val) in self.drink.items():
            for word in val:
                if word in self.cmd:
                    self.need = key
                    response = response + key + '?'
                    self.person_drink.publish(self.need)
                    break
        return response

    # def get_name(self):
    #     name = self.people
    #     return name
    #
    # def get_drink(self):
    #     drink = self.need
    #     return drink


if __name__ == '__main__':
    try:
        rospy.init_node('voice_recognition')
        Recognizer()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
