#!/usr/bin/env python3
# coding: utf-8
import rospy
import numpy as np
import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.open(0)
while cap.isOpened():
    flag, frame = cap.read()
    cv2.imshow('my_window', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destoryAllWindows()
