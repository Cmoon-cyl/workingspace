#!/usr/bin/env python3
# coding:utf-8
import rospy
import math
from sensor_msgs.msg import LaserScan
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry


class DOOROPEN:
    def __init__(self):

        self.flag = False  # 只发送一次开门信号
        self.judge = False
        self.cnt = 0
        self.x_old = 0.0
        self.x_new = 0.0
        self.y_old = 0.0
        self.y_new = 0.0

        self.distance = 0.0

        rospy.Subscriber('/odom', Odometry, self.get_location)
        rospy.Subscriber("scan", LaserScan, self.dooropen)
        self.cmd_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
        self.go_firstpoint = rospy.Publisher('/go_destination', String, queue_size=10)

        rospy.sleep(2)
        rospy.loginfo("get_in_door ready...")

    def dooropen(self, data):

        xx = list(data.ranges)
        yy = list(data.intensities)

        print('xx:' + str(len(xx)) + ' yy:' + str(len(yy)))

        if (yy[239] == 0.0):
            self.cnt += 1
        else:
            self.cnt = 0

        if ((xx[239] != 0 and xx[239] > 1 or self.cnt > 30) and self.flag == False):  # 一段时间没检测到雷达或者检测到的距离小于1
            self.flag = True
            self.get_in_door()

    def get_location(self, odom_msg):

        if (self.judge):
            self.x_new = odom_msg.pose.pose.position.x
            self.y_new = odom_msg.pose.pose.position.y
        else:
            self.x_old = odom_msg.pose.pose.position.x
            self.y_old = odom_msg.pose.pose.position.y

        # print('x_old:'+str(self.x_old)+'  x_new:'+str(self.x_new)+'  y_old'+str(self.y_old)+'  y_new'+str(self.y_new))
        self.distance = ((self.x_new - self.x_old) ** 2 + (self.y_new - self.y_old) ** 2) ** 0.5

    # print(self.distance)

    def get_in_door(self):

        rate = rospy.Rate(10)

        self.judge = True
        rospy.sleep(1)

        while (math.fabs(self.distance - 1) > 0.02):
            if (math.fabs(self.distance - 1) > 0.5):
                speed = 0.5
            else:
                speed = 0.1
            twist_msg = Twist()
            twist_msg.linear.x = speed
            self.cmd_pub.publish(twist_msg)
            rate.sleep()

        self.judge = False
        twist_msg.linear.x = 0
        self.cmd_pub.publish(twist_msg)


if __name__ == '__main__':
    rospy.init_node('DoorOpen', anonymous=False)
    DOOROPEN()
    rospy.spin()
