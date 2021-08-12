#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist


def velocity_publisher():
    rospy.init_node('velocity_publisher', anonymous=True)

    turtle_vel_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    rate = rospy.Rate(62)
    count = 0
    while not rospy.is_shutdown():
        vel_msg = Twist()
        count = count+1
        vel_msg.linear.x = 2
        vel_msg.linear.y = 0
        while count >= 80:
            count = count+1
            vel_msg.linear.x = 0
            vel_msg.linear.y = 2
            turtle_vel_pub.publish(vel_msg)
            rospy.loginfo("Publish turtle velocity command[%0.2f m/s, %0.2f rad/s]",
                          vel_msg.linear.x, vel_msg.angular.z)
            rate.sleep()
            while count >= 160:
                count = count+1
                vel_msg.linear.x = -2
                vel_msg.linear.y = 0
                turtle_vel_pub.publish(vel_msg)
                rospy.loginfo("Publish turtle velocity command[%0.2f m/s, %0.2f rad/s]",
                              vel_msg.linear.x, vel_msg.angular.z)
                rate.sleep()
                while count >= 240:
                    count = count+1
                    vel_msg.linear.x = 0
                    vel_msg.linear.y = -2
                    if count >= 320:
                        count = 0
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
