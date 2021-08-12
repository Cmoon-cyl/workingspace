#!/usr/bin/env python
# coding:utf-8
import sys 
import rospy 
from std_msgs.msg import String 
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from std_msgs.msg import String, Int16
import math
class indoor: 
    def __init__(self): 
        self.sub=rospy.Subscriber('/start',String,self.callback)
        self.pub = rospy.Publisher("/cmd_vel", Twist,queue_size=10)
        self.sub2=rospy.Subscriber('/odom',Odometry,self.get_x)
        self.pub2 = rospy.Publisher("/go",Int16,queue_size=10)
        self.x = 0
    def callback(self, data):
        if(data.data != "ok"):
            return
        rate = rospy.Rate(10)
        start_x=self.x 
        start_y=self.y

        while((start_x-self.x)**2+(start_y-self.y)**2<1):
            if((start_x-self.x)**2+(start_y-self.y)**2 < 0.75):
                speed = 0.3
            else:
                speed = 0.1
            if((start_x-self.x)**2+(start_y-self.y)**2 >1):
                speed = -speed
            twist_msg = Twist()
            twist_msg.linear.x = speed
            #print((start_x-self.x)**2+(start_y-self.y)**2)
            #rospy.login
            self.pub.publish(twist_msg)
            #print(speed)
            rate.sleep()
	self.pub2.publish(1)
    def get_x(self, odom_msg):
        self.x = odom_msg.pose.pose.position.x
        self.y = odom_msg.pose.pose.position.y
        #print(self.x)
        #print(self.y)
if __name__ == '__main__': 
    rospy.init_node('indoor', anonymous=False) 
    lidar = indoor() 
    rospy.spin()
