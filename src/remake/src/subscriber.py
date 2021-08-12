#!/usr/bin/env python3
#coding: utf-8

import rospy
from std_msgs.msg import String
from nav_msgs.msg import Odometry
from cmoon_msgs.msg import location


def callback(msg):
    rospy.loginfo('callback')
    ll=location()
    ll.location='living room'
    ll.x=1.0
    ll.y=2.0
    pub=rospy.Publisher('location',location,queue_size=10)
    pub.publish(ll)
    rospy.loginfo('location:{} x:{} y{}'.format(ll.location,ll.x,ll.y))

def main():
    rospy.init_node('test1')
    rospy.Subscriber('/odom',Odometry,callback)
    # pub=rospy.Publisher('location',location,queue_size=10)
    # ll=location()
    # ll.location='living room'
    # ll.x=1.0
    # ll.y=2.0
    # rate=rospy.Rate(1)
    # while not rospy.is_shutdown():
    #     pub.publish(ll)
    #     rospy.loginfo('location:{} x:{} y{}'.format(ll.location,ll.x,ll.y))
    #     rate.sleep()
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        rospy.loginfo("Keyboard interrupt.")