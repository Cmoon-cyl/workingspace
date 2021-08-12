#!/usr/bin/env python3
#coding: utf-8
import rospy
from geometry_msgs.msg import Twist
import cv2
import numpy as np
class robot:
    def __init__(self):
        self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
    def turn(self, flag):
        msg = Twist()
        if(flag ==1):
            msg.angular.z=0.5
        elif(flag == 0):
            msg.angular.z = 0
        else:
            msg.angular.z=-0.5
        self.pub.publish(msg)

def judge(img):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #frame = cv2.GaussianBlur(gray,(5,5),0)
    #ret,frame=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    ret,frame=cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    h = frame.shape[0]
    w = frame.shape[1]
    box = frame[int(0.25*h):int(0.75*h),int(0.25*w):int(0.75*w)]
    value = np.mean(box)
    print(value)
    cv2.imshow("bwtext",frame)

    if(value < 60):
        return -1
    elif(value >=60 and value <130):
        return 0
    else:
        return 1

def main():
    rospy.init_node("bwtest")
    RB = robot()
    cap = cv2.VideoCapture(0)
    while(not rospy.is_shutdown()):
        ret, img = cap.read()
        RB.turn(judge(img))
        #cv2.imshow("example",img)
        k = cv2.waitKey(1)
        if(k == ord("q")):
            cv2.destroyAllWindows()
            break
if __name__ == "__main__":
    main()