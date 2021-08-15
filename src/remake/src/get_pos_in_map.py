#! /usr/bin/env python

import rospy
import tf
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped


class Main():
    def __init__(self):
        rospy.init_node('get_pos_in_map_frame')
        rospy.Subscriber('gt_pose', PoseStamped, self.showpose)
        self.key = 0

    def showpose(self, pose):
        if self.key == 0:
            rospy.loginfo('[{},{},{}]'.format(pose.pose.position.x, pose.pose.position.y, pose.pose.position.z))
            rospy.loginfo(
                '[{},{},{},{}]'.format(pose.pose.orientation.x, pose.pose.orientation.y, pose.pose.orientation.z,
                                       pose.pose.orientation.w))
            self.key = 1


if __name__ == '__main__':
    try:
        Main()
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo(" node terminated.")
