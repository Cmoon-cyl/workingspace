#!/usr/bin/env python
#coding: utf-8
import rospy
from std_msgs.msg import Int16
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import math
import time

class turtleSquare:
    def __init__(self):
        self.theta  = 0
        self.x  = 0
        self.y  = 0
        self.sub = rospy.Subscriber('/turtle1/pose', Pose, self.getPose)
        self.pub=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
        time.sleep(1)

    def getPose(self, data):
        self.theta = data.theta
        self.x = data.x
        self.y = data.y

    def turn90(self):
        rp = rospy.Rate(10)
        start = self.theta
        end = start+math.pi/2 if start+math.pi/2<=math.pi else start+math.pi/2-2*math.pi
        msg = Twist()
        maxspeed = 3
        while(abs(self.theta-end)>0.001):
            diff = abs(self.theta-end) if abs(self.theta-end) < math.pi else 2*math.pi-abs(self.theta-end) 
            msg.angular.z = maxspeed * diff /math.pi/2+0.005
            self.pub.publish(msg)
            rp.sleep()

    def run(self, dis):
        rp = rospy.Rate(5)
        speed = Twist()
        speed.linear.x = 1
        nowx = self.x
        nowy = self.y
        while(abs( math.sqrt( (self.x-nowx)*(self.x-nowx)+(self.y-nowy)*(self.y-nowy))-dis)  >0.01) :
            self.pub.publish(speed)
            rp.sleep()

    def square(self):
        for i in range(4):
            self.run(5)
            self.turn90()

def main():
    rospy.init_node("square")
    S = turtleSquare()
    S.square()

if __name__ == '__main__':
    main()