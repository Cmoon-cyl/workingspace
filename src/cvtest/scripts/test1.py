#!/usr/bin/env python
# coding: utf-8 
import rospy
import numpy as np
import cv2
from geometry_msgs.msg import Twist

class robot:
    def __init__(self):
        self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
    def straight(self, flag):
        msg = Twist()
        if(flag ==1):
            msg.angular.z=0.2
        elif(flag == 0):
            msg.angular.z = 0
        else:
            msg.angular.z=-0.2
        self.pub.publish(msg)
        
def main():
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

if __name__ =='__main__':
        try:
            rospy.init_node("huidu_test")
            rospy.loginfo("Starting huidu_test node.")
            run()
        except rospy.ROSInterruptException:
            pass

while(not rospy.is_shutdown()):
    ret , img = cap.read()
    gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',gray)
    if cv2.waitKey(1) &0xFF ==ord('q'):  #按q键退出
    	break	
cap.release()
cv2.destroyAllWindows()