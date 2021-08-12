#!/usr/bin/env python
# coding: utf-8
from math import radians, pi
from visualization_msgs.msg import Marker
from tf.transformations import quaternion_from_euler
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Pose, Point, Quaternion, Twist
from actionlib_msgs.msg import *
import actionlib
import math
import rospy
import roslib
roslib.load_manifest('rbx1_nav')


class MoveBaseTri():
    def __init__(self):
        rospy.init_node('nav_test', anonymous=False)
#        rospy.on_shutdown(self.shutdown)

        quaternions = list()  # 角度数据
        euler_angles = (0, 2*pi/3, 4*pi/3)  # 机器人方向
        for angle in euler_angles:  # 格式转换
            q_angle = quaternion_from_euler(0, 0, angle, axes='sxyz')
            q = Quaternion(*q_angle)
            quaternions.append(q)
        waypoints = list()  # 储存导航点
        waypoints.append(Pose(Point(1.0, 0, 0.0), quaternions[0]))
        waypoints.append(Pose(Point(0.0, math.sqrt(3), 0.0), quaternions[1]))
        waypoints.append(Pose(Point(-1.0, 0.0, 0.0), quaternions[2]))
        self.init_markers()  # 可视化标记
        for waypoint in waypoints:  # 三个点
            p = Point()
            p = waypoint.position
            self.markers.points.append(p)
        self.cmd_vel_pub = rospy.Publisher('cmd_vel', Twist)  # 发布twist信息
        self.move_base = actionlib.SimpleActionClient(
            "move_base", MoveBaseAction)  # 订阅
        rospy.loginfo("Waiting for move_base action server...")
        self.move_base.wait_for_server(rospy.Duration(60))  # 等待
        rospy.loginfo("Connected to move base server")  # 打在公屏上
        rospy.loginfo("Starting navigation test")

        i = 0  # 计数器
        while i < 3 and not rospy.is_shutdown():  # 发布位置
            self.marker_pub.publish(self.markers)
            goal = MoveBaseGoal()  # 初始化
            goal.target_pose.header.frame_id = 'map'  # 定义
            goal.target_pose.header.stamp = rospy.Time.now()  # 设置时间戳
            goal.target_pose.pose = waypoints[i]  # 第几个导航点
            self.move(goal)  # 机器人移动
            i += 1
            if i==3:
                i=0

    def move(self, goal):
        self.move_base.send_goal(goal)  # 发送位置给服务器
        finished_within_time = self.move_base.wait_for_result(
            rospy.Duration(60))#一分钟时间限制
        if not finished_within_time:#及时止损
            self.move_base.cancel_goal()
            rospy.loginfo("Timed out achieving goal")
        else:
            state = self.move_base.get_state()
            if state == GoalStatus.SUCCEEDED:
                rospy.loginfo("Goal succeeded!")

    def init_markers(self):#标记尺寸
        marker_scale = 0.2
        marker_lifetime = 0  
        marker_ns = 'waypoints'
        marker_id = 0
        marker_color = {'r': 248.0, 'g': 248.0, 'b': 255.0, 'a': 1.0}
        self.marker_pub = rospy.Publisher('waypoint_markers', Marker)#标记发布者
        self.markers = Marker()#初始化列表
        self.markers.ns = marker_ns
        self.markers.id = marker_id
        self.markers.type = Marker.SPHERE_LIST
        self.markers.action = Marker.ADD
        self.markers.lifetime = rospy.Duration(marker_lifetime)
        self.markers.scale.x = marker_scale
        self.markers.scale.y = marker_scale
        self.markers.color.r = marker_color['r']
        self.markers.color.g = marker_color['g']
        self.markers.color.b = marker_color['b']
        self.markers.color.a = marker_color['a']

        self.markers.header.frame_id = 'map'
        self.markers.header.stamp = rospy.Time.now()
        self.markers.points = list()

    def shutdown(self):
        rospy.loginfo("Stopping the robot...")
        #self.move_base.cancel_goal()
        rospy.sleep(2)
        self.cmd_vel_pub.publish(Twist())#停机
        rospy.sleep(1)


if __name__ == '__main__':
    try:
        MoveBaseTri()
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")
