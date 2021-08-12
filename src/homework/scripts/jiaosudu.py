#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist


def velocity_publisher():
    rospy.init_node('velocity_publisher', anonymous=True)

    turtle_vel_pub = rospy.Publisher(
        '/turtle1/cmd_vel', Twist, queue_size=1000)

    rate = rospy.Rate(4)
    count = 0
    while not rospy.is_shutdown():
        vel_msg = Twist()
        vel_msg.linear.x = 1
        vel_msg.linear.y = 0
        vel_msg.angular.z = 0
        count = count+1
        while count >= 10:
            count = 0
            vel_msg.angular.z = 3.14159265358979323846
            turtle_vel_pub.publish(vel_msg)
            rospy.loginfo("Publish turtle velocity command[%0.2f m/s, %0.2f rad/s]",
                          vel_msg.linear.x, vel_msg.angular.z)

            rate.sleep()
        turtle_vel_pub.publish(vel_msg)
        rospy.loginfo("Publish turtle velocity command[%0.2f m/s, %0.2f rad/s]",
                      vel_msg.linear.x, vel_msg.angular.z)

        rate.sleep()


if __name__ == '__main__':
    try:
        velocity_publisher()
    except rospy.ROSInterruptException:
        pass
