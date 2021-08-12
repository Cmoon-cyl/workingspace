#!/usr/bin/env python3
#coding: utf-8
import rospy
from geometry_msgs.msg import Twist
import cv2
import numpy as np
class robot:
    def __init__(self):
        self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
        #参数含义
    def straight(self, flag):
        msg = Twist()
        if(flag ==1):
            msg.linear.x=0.2
        elif(flag == 0):
            msg.linear.x = 0
        else:
            msg.linear.x=-0.2
        self.pub.publish(msg)

def judge(img):

    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #print(gray.shape)
    h = gray.shape[0]
    w = gray.shape[1]
    box = gray[int(0.25*h):int(0.75*h),int(0.25*w):int(0.75*w)]
    #print(box.shape)
    value = np.mean(box)
    print(value)
    cv2.imshow("example",box)
    if(value < 60):
        return -1
    elif(value >=60 and value <130):
        return 0
    else:
        return 1
    #环境参数60， 130

def main():
    rospy.init_node("example3")
    RB = robot()
    cap = cv2.VideoCapture(0)
    while(not rospy.is_shutdown()):
        ret, img = cap.read()
        RB.straight(judge(img))
        #cv2.imshow("example",img)
        k = cv2.waitKey(1)
        if(k == ord("q")):
            cv2.destroyAllWindows()
            break
if __name__ == "__main__":
    main()