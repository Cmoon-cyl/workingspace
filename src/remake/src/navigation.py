#!/usr/bin/env python3
# !coding=utf-8

import rospy
from std_msgs.msg import String
from std_srvs.srv import Empty
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from sound_play.libsoundplay import SoundClient

LOCATION = {
    'door': [[-4.352973, -6.186659, 0.000000], [0.000000, 0.000000, -0.202218, -0.979341]],
    'living room': [[-0.476640, -4.946882, 0.000000], [0.000000, 0.000000, 0.808888, 0.587962]],
    'kitchen': [[-1.658400, -0.046712, 0.000000], [0.000000, 0.000000, -0.986665, 0.162761]],
    'bedroom': [[3.859466, -2.201285, 0.000000], [0.000000, 0.000000, -0.247601, -0.968862]],
    'dining room': [[3.583689, 0.334696, 0.000000], [0.000000, 0.000000, -0.820933, -0.571025]],
    'garage': [[0.166213, 3.886673, 0.000000], [0.000000, 0.000000, -0.982742, 0.184983]],
}


class NAVIGATION:

    def __init__(self):

        self.location = LOCATION

        rospy.Subscriber('/navigation', String, self.posePosition)
        self.pub_unlock_yes = rospy.Publisher('/lock_yes_to_base', String, queue_size=1)
        self.soundhandle = SoundClient()

        rospy.sleep(1)
        # Make sure any lingering sound_play process are stopped .
        self.soundhandle.stopAll()

        self.clear_costmap_client = rospy.ServiceProxy('move_base/clear_costmaps', Empty)

        rospy.sleep(1)
        rospy.loginfo('go_destination ready...')

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

    def posePosition(self, place):
        point = self.goal_pose("map", self.location[place.data][0], self.location[place.data][1])
        self.go_to_location(point)
        print('I have got the  ' + place.data)
        self.soundhandle.say('I have got the  ' + place.data)
        rospy.sleep(2)
        self.pub_unlock_yes.publish('')

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
    rospy.spin()
