#!/usr/bin/env python3
# coding: utf-8

import math
import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist


class Turtle:
    def __init__(self, name):
        rospy.init_node(name)
        rospy.Subscriber('/turtle1/pose', Pose, self.control)
        self.pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.size = 5
        self.kp1 = 6
        self.kp2 = 4
        self.kd = 15
        self.aim = 0.025
        self.vel_cmd = Twist()
        self.point = []
        self.x = None
        self.y = None
        self.theta = None
        self.goal = None
        self.error = None
        self.flag = 0
        self.lock = 0

    def control(self, pose):
        self.choose_graph('square', pose)

    def choose_graph(self, graph, pose):
        self.set_goal_points(graph, pose, self.size)
        self.get_present_point(pose)
        self.go_graph(self.kp1, self.kp2, self.kd, self.aim)

    def set_goal_points(self, graph, pose, size=5):
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
        self.x = pose.x
        self.y = pose.y
        self.theta = pose.theta

    def go_graph(self, kp1=4, kp2=4, kd=15, aim=0.025):
        self.go_line(kp1, kd, aim)
        self.rotate(kp2)

    def find_closest_point(self):
        distance = [math.sqrt((self.x - self.point[i][0]) ** 2 + (self.y - self.point[i][1]) ** 2) for i in range(4)]
        closest_point = distance.index(min(distance))
        return closest_point

    def go_line(self, kp=2, kd=15, aim=0.08, ):
        if self.lock == 0:
            if self.flag == 0:
                closest_point = self.find_closest_point()
                self.goal = closest_point + 1 if closest_point != len(self.point) - 1 else 0
                self.error = self.size
                self.flag += 1
            last_error = self.error
            self.error = math.sqrt((self.x - self.point[self.goal][0]) ** 2 + (self.y - self.point[self.goal][1]) ** 2)
            if abs(self.error) > aim:
                self.vel_cmd.linear.x = kp * self.error + kd * (self.error - last_error)
                rospy.loginfo('going')
                rospy.loginfo('{},{},{}'.format(self.error, self.error - last_error, self.vel_cmd.linear.x))
            else:
                self.vel_cmd.linear.x = 0
                self.lock = 1
            self.pub.publish(self.vel_cmd)

    def rotate(self, kp=2):
        if self.lock == 1:
            if self.flag == 1:
                closest_point = self.find_closest_point()
                self.goal = closest_point if closest_point != len(self.point) - 1 else 0
                self.flag += 1
            self.error = abs(self.theta - self.point[self.goal][2])
            if self.error > 0.01:
                self.vel_cmd.angular.z = kp * (self.error + 0.1)
                rospy.loginfo('rotating')
                rospy.loginfo('{},{}'.format(self.error, self.vel_cmd.linear.x))
            else:
                self.vel_cmd.angular.z = 0
                self.flag = 0
                self.lock = 0
            self.pub.publish(self.vel_cmd)


if __name__ == '__main__':
    try:
        Turtle('turtle_graph')
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo("Keyboard interrupt.")
