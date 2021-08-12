#!/usr/bin/env python3
# coding: utf-8
import rospy
import numpy as np
import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.open(0)
while cap.isOpened():
    flag, frame = cap.read()
    if not flag:
        berak
   # 进行Canny边缘检测
    frame = cv2.Canny(frame, 100, 200)
    #将单通道图像复制三份，摞成三通道图像
    frame = np.dstack((frame, frame, frame))
    cv2.imshow('img', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
