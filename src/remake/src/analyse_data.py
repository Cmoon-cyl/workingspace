#!/usr/bin/env python3
# !coding=utf-8
# Created by Cmoon

import rospy
import os
import pdfkit
from std_msgs.msg import Int8
from std_msgs.msg import String
from gpsr_2020.msg import Command
from sound_play.libsoundplay import SoundClient

LOCATION = {
    'door': ['door', 'dog'],
    'kitchen': ['kitchen', 'page', 'station', 'location'],
    'living room': ['living', 'leaving', 'livingroom', 'living room'],
    'bedroom': ['bedroom', 'bad', 'bed room', 'bad room', 'bed', 'bathroom', 'beijing'],
    'hallway': ['hallway', 'whole way'],
    'dining room': ['dining', 'dying'],
    'garage': ['garage']
}


class Analyse:
    def __init__(self):

        self.rate = rospy.get_param("~rate", 2)
        rospy.Rate(self.rate)
        self.location = LOCATION
        self.soundhandle = SoundClient()
        rospy.sleep(1)
        # Make sure any lingering sound_play process are stopped .
        self.soundhandle.stopAll()

        rospy.sleep(2)
        rospy.loginfo('analyse_data ready...')
        rospy.loginfo("Say one of the navigation commands ...")
        print('...  ... ')

        rospy.Subscriber('/xfspeech', String, self.talkback)
        rospy.Subscriber('/lock_analyse', String, self.lock_change)
        self.pub_cmd = rospy.Publisher('/command', Command, queue_size=1)
        self.xfwakeup_pub = rospy.Publisher('/xfwakeup', String, queue_size=10)

        self.d_location = LOCATION

        self.status = 0
        self.location_go = ''
        self.location_follow = ''
        self.location_catch = ''
        self.question_type = 0
        self.flag_back = False
        self.flag_calling = False
        self.com_type = 0
        self.object = ''
        self.name = ''

        self.lock = False
        self.pdfpath = os.path.dirname(os.path.dirname(__file__)) + '/photo'

        rospy.sleep(2)
        print("I'm ready")
        self.soundhandle.say("I'm ready")

    def init_set(self):

        # 命令參數
        self.status = 0
        self.location_go = ''
        self.location_follow = ''
        self.location_catch = ''
        self.question_type = 0
        self.flag_back = False
        self.flag_calling = False
        self.com_type = 0
        self.object = ''
        self.name = ''

    def analyze_data(self, cmd):

        c5 = 'Do you need me '

        return c5 + '?'

    def processed_cmd(self, cmd):
        cmd = cmd.lower()
        for i in " ,.;?":
            cmd = cmd.replace(i, ' ')
        return cmd

    def get_command(self):
        cmd = Command()
        cmd.com_type = self.com_type
        cmd.location_go = self.location_go
        cmd.location_follow = self.location_follow
        cmd.location_catch = self.location_catch
        cmd.object = self.object
        cmd.name = self.name
        cmd.question_type = self.question_type
        cmd.flag_back = self.flag_back
        cmd.flag_calling = self.flag_calling
        return cmd

    def talkback(self, msg):

        print("\n讯飞读入的信息为: " + msg.data)
        cmd = self.processed_cmd(msg.data)

        if self.status == 0:
            cmd = self.analyze_data(cmd)
            if cmd == 'Do you need me ':
                self.soundhandle.say("Please say the command again. ")
                rospy.sleep(2)
                self.xfwakeup_pub.publish("ok")
            else:

                self.status = 1
                self.cmd = cmd

                print(cmd)
                self.soundhandle.say(cmd)
                rospy.sleep(8)

                self.soundhandle.say("please say yes or no.")
                print('Please say yes or no.')
                rospy.sleep(2)

                self.xfwakeup_pub.publish("ok")

        elif ('Yes.' in cmd) or ('yes' in cmd) and (self.status == 1):
            f = open(self.pdfpath + '/test.html', 'a')
            f.write('<h2>' + self.cmd + '</h2>')
            f.close()
            self.lock_change()
            self.soundhandle.say('Ok, I will.')
            print('Ok, I will.')
            command = self.get_command()
            self.pub_cmd.publish(command)
            self.init_set()

        elif ('No.' in cmd) or ('no' in cmd) or ('oh' in cmd) or ('know' in cmd) and (self.status == 1):

            self.soundhandle.say("Please say the command again. ")
            print("Please say the command again. ")
            rospy.sleep(2)

            self.init_set()

            self.xfwakeup_pub.publish("ok")

    def lock_change(self, msg=None):
        self.lock = not self.lock


if __name__ == "__main__":
    rospy.init_node('Analyse_Data')
    Analyse()
    rospy.spin()
