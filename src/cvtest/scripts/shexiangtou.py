#!/usr/bin/env python3
# coding: utf-8
import rospy
import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while(not rospy.is_shutdown()):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #ret,frame=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    #frame=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C , cv2.THRESH_BINARY,11,2 )
    frame= cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY,11,2)
    cv2.imshow('img', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

