#!/usr/bin/env python
# coding: UTF-8 

import rospy
from std_msgs.msg import String
from std_srvs.srv import Empty
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from sound_play.libsoundplay import SoundClient

LOCATION = [[[3.03755426407, 8.67973995209, 0.0], [0.0, 0.0, -0.999973565473, 0.00727106283505]],
            [[-13.5349721909, 4.6444811821, 0.0], [-13.5349721909, 4.6444811821, 0.0]],
            [[0, 0, 0], [0.0, 0.0, 0.0, 1.0]]
            ]


class Main:
    def __init__(self, name):
        rospy.init_node(name, anonymous=True)


class NAVIGATION:

    def __init__(self):

        self.location = LOCATION
        self.clear_costmap_client = rospy.ServiceProxy('move_base/clear_costmaps', Empty)
        point = self.goal_pose("map", self.location[0][0], self.location[0][1])
        self.go_to_location(point)

    def go_to_location(self, location):
        client = actionlib.SimpleActionClient('move_base', MoveBaseAction)  # 等待MoveBaseAction server启动
        client.wait_for_server()
        while not rospy.is_shutdown():
            flag = False
            while (flag == False):  # 导航到指定点
                print('尝试导航')
                self.clear_costmap_client()
                client.send_goal(location)
                client.wait_for_result()
                if (client.get_state() == 3):
                    flag = True
                    break
            break

    def goal_pose(self, name, position, orientation):
        goal_pose = MoveBaseGoal()
        goal_pose.target_pose.header.frame_id = name
        goal_pose.target_pose.pose.position.x = position[0]
        goal_pose.target_pose.pose.position.y = position[1]
        goal_pose.target_pose.pose.position.z = position[2]

        goal_pose.target_pose.pose.orientation.x = orientation[0]
        goal_pose.target_pose.pose.orientation.y = orientation[1]
        goal_pose.target_pose.pose.orientation.z = orientation[2]
        goal_pose.target_pose.pose.orientation.w = orientation[3]
        return goal_pose


if __name__ == '__main__':
    rospy.init_node('Navigation')
    NAVIGATION()
