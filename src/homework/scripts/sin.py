#!/usr/bin/env python
# coding: utf-8
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
PI = 3.1415926535897

import math

# Initial value of theta is 0
theta = 0



# Subscriber callback function
def pose_callback(pose):
    global theta
    req =  2 * math.pi
    if pose.theta < 0:
        alpha = req - (pose.theta + (2 * math.pi))
    else:
        alpha = req - pose.theta

    alpha = 2 * math.pi - alpha
    theta = alpha


# sin_graph function
def sin_graph():
    # Starts a new node
    global theta
    rospy.init_node('sin_graph', anonymous=True)

    # Initialization of publisher
    velocity_publisher = rospy.Publisher(
        '/turtle1/cmd_vel', Twist, queue_size=10)
    # Subscribing to topic Pose
    rospy.Subscriber("/turtle1/pose", Pose, pose_callback)

    vel_msg = Twist()

    # Initializing basic data
    speed = 0.2
    radius = 1
    vel_msg.linear.x = speed
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = speed/radius

    
    
    # Rate at which message is published (10 times per second)
    rate = rospy.Rate(10)

    # Loop until current distance is re-initialized to zero(theta = 0)
    while not rospy.is_shutdown():
        
        vel_msg.linear.x = speed * math.cos(theta)
        vel_msg.angular.z =  math.sin(theta)
        velocity_publisher.publish(vel_msg)
       
        rospy.loginfo("Moving in a sine curve")
        print(theta)
        rate.sleep()

    # Forcing our robot to stop
    print("Goal Reached")
    vel_msg.linear.x = 0
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)
    rospy.spin()


if __name__ == '__main__':
    try:
        # Testing our function
        sin_graph()
    except rospy.ROSInterruptException:
        pass