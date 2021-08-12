#!/usr/bin/env python3
# coding: utf-8

import math
import rospy
from turtlesim.msg import Pose  # Pose数据类型包含乌龟的坐标和角度
from geometry_msgs.msg import Twist  # Twist数据类型包含线速度和角速度


class Turtle:
    def __init__(self, name, graph):
        rospy.init_node(name)  # 初始化节点
        rospy.Subscriber('/turtle1/pose', Pose, self.control)  # 实例化订阅者，参数为订阅的话题名，消息类型，回调函数
        self.pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)  # 实例化发布者，参数为发布的话题名，消息类型，队列长度
        self._graph = graph
        self.size = 5  # 图形的大小
        self.kp1 = 6  # 走直线的比例控制参数
        self.kp2 = 4  # 转角度的比例控制参数
        self.kd = 10  # 走直线的微分控制参数
        self.aim = 0.025  # 目标的误差值
        self.vel_cmd = Twist()  # 实例化Twist消息类型的消息
        self.point = []  # 储存所走路径目标点
        self.x = None  # 乌龟目前所在x坐标
        self.y = None  # 乌龟目前所在y坐标
        self.theta = None  # 乌龟目前角度
        self.goal = None  # 乌龟下一个要到达的目标点
        self.error = None  # 现在距离目标点的误差值
        self.flag = 0  # flag和lock实现走直线和转角度的互锁，执行完一个才能执行另一个
        self.lock = 0

    def control(self, pose):
        """订阅的回调函数"""
        self.choose_graph(self._graph, pose)  # 设定要走什么形状

    def choose_graph(self, graph, pose):
        """根据传入的图形设定目标点，获取当前位置，控制运动"""
        self.set_goal_points(graph, pose, self.size)
        self.get_present_point(pose)
        self.go_graph(self.kp1, self.kp2, self.kd, self.aim)

    def set_goal_points(self, graph, pose, size=5):
        """设定不同形状的目标点，坐标和角度"""
        if graph == 'square':
            self.point.append([pose.x, pose.y, pose.theta])
            self.point.append([pose.x + size, pose.y, pose.theta + math.pi / 2])
            self.point.append([pose.x + size, pose.y + size, pose.theta + math.pi])
            self.point.append([pose.x, pose.y + size, pose.theta - math.pi / 2])

        elif graph == 'tri':
            self.point.append([pose.x, pose.y, pose.theta])
            self.point.append([pose.x + size, pose.y, math.pi * 2 / 3])
            self.point.append(
                [pose.x + size / 2, pose.y + (size / 2 * math.tan(math.pi / 3)), pose.theta - math.pi * 2 / 3])
            self.point.append([pose.x, pose.y, pose.theta])

        elif graph == 'rec':
            self.point.append([pose.x, pose.y, pose.theta])
            self.point.append([pose.x + 5, pose.y, pose.theta + math.pi / 2])
            self.point.append([pose.x + 5, pose.y + 3, pose.theta + math.pi])
            self.point.append([pose.x, pose.y + 3, pose.theta - math.pi / 2])

        else:
            raise NotImplementedError('Do not support such graph.')

    def get_present_point(self, pose):
        """获取当前坐标和角度"""
        self.x = pose.x
        self.y = pose.y
        self.theta = pose.theta

    def go_graph(self, kp1=4, kp2=4, kd=15, aim=0.025):
        """控制运动"""
        self.go_line(kp1, kd, aim)
        self.rotate(kp2)

    def find_closest_point(self):
        """寻找现在距离哪个点最近"""
        # 计算现在坐标和其他所有目标点的距离，传入distance列表
        distance = [math.sqrt((self.x - self.point[i][0]) ** 2 + (self.y - self.point[i][1]) ** 2) for i in range(4)]
        closest_point = distance.index(min(distance))  # 获取列表中最小的点的索引
        return closest_point

    def go_line(self, kp=2, kd=15, aim=0.08, ):
        """控制走直线"""
        if self.lock == 0:  # 和旋转互锁
            if self.flag == 0:  # 第一次进函数执行一次初始化
                closest_point = self.find_closest_point()  # 获取最近的点
                self.goal = closest_point + 1 if closest_point != len(self.point) - 1 else 0  # 计算下一个目标点
                self.error = self.size  # 初始误差为设定的图形大小
                self.flag += 1  # 保证初始化只执行一次
            last_error = self.error  # 上一次的误差
            self.error = math.sqrt(
                (self.x - self.point[self.goal][0]) ** 2 + (self.y - self.point[self.goal][1]) ** 2)  # 计算现在的误差
            if abs(self.error) > aim:  # 误差大于设定精度时前进
                self.vel_cmd.linear.x = kp * self.error + kd * (self.error - last_error)  # pd控制计算当前速度
                rospy.loginfo('going')
                rospy.loginfo('{},{},{}'.format(self.error, self.error - last_error, self.vel_cmd.linear.x))
            else:
                self.vel_cmd.linear.x = 0
                self.lock = 1  # 解锁旋转
            self.pub.publish(self.vel_cmd)  # 发布乌龟速度

    def rotate(self, kp=2):
        """控制旋转"""
        if self.lock == 1:  # 和直走互锁
            if self.flag == 1:  # 第一次进函数执行一次初始化函数
                closest_point = self.find_closest_point()  # 获取最近的点
                self.goal = closest_point if closest_point != len(self.point) - 1 else 0  # 计算下一个目标点
                self.flag += 1  # 保证只执行一次初始化
            self.error = abs(self.theta - self.point[self.goal][2])  # 计算当前误差
            if self.error > 0.01:  # 误差大于0.01时保持旋转
                self.vel_cmd.angular.z = kp * (self.error + 0.1)  # p控制计算旋转速度
                rospy.loginfo('rotating')
                rospy.loginfo('{},{}'.format(self.error, self.vel_cmd.linear.x))
            else:
                self.vel_cmd.angular.z = 0
                self.flag = 0
                self.lock = 0
            self.pub.publish(self.vel_cmd)  # 发布乌龟速度


if __name__ == '__main__':
    try:
        Turtle('turtle_graph', input('Input graph(square or tri ir rec): '))  # 实例化Turtle，传入初始化的节点名
        rospy.spin()  # 循环监听callback
    except rospy.ROSInterruptException:
        rospy.loginfo("Keyboard interrupt.")
