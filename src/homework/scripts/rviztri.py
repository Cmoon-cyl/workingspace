#!/usr/bin/env python3
#coding: utf-8
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int16
from std_msgs.msg import Float64
from nav_msgs.msg import Odometry
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Twist
import math
import sys
import time

def goal_pose(name,position, orientation):
    goal_pose = MoveBaseGoal()
    goal_pose.target_pose.header.frame_id = name
    goal_pose.target_pose.pose.position.x = position[0]
    goal_pose.target_pose.pose.position.y = position[1]
    goal_pose.target_pose.pose.position.z = position[2]

    goal_pose.target_pose.pose.orientation.x=orientation[0]
    goal_pose.target_pose.pose.orientation.y=orientation[1]
    goal_pose.target_pose.pose.orientation.z=orientation[2]
    goal_pose.target_pose.pose.orientation.w=orientation[3]
    return goal_pose


goal1 = goal_pose("map",[3,0, 0], [0.0, 0.0, 0.7071068, 0.7071068])
#
goal2 = goal_pose("map",[3, 4 , 0], [0.0, 0.0, 1, 0])
#
goal3 = goal_pose("map",[0 ,2, 0], [0.0, 0.0,-0.7071068,0.7071068])
#
goal4 = goal_pose("map",[0, 0, 0], [0.0, 0.0, 0, 1])


positons = [goal1, goal2, goal3, goal4]

if __name__ == '__main__':
    rospy.init_node("example2")
    client=actionlib.SimpleActionClient('move_base',MoveBaseAction)
    #等待MoveBaseAction server启动
    client.wait_for_server()
    while not rospy.is_shutdown():
        for i in range(len(positons)):
            pose = positons[i]
            flag = False
            while(flag == False):
                #导航到指定点
                client.send_goal(pose)
                client.wait_for_result()
                if(client.get_state() == 3):
                    flag = True
                    break
        break
                
