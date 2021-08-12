#!/usr/bin/env python3
# coding: utf-8
import rospy
import numpy as np
import cv2

# 获取摄像头
cap = cv2.VideoCapture(0)

# 指定VideoWriter的fourCC视频编码
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

# 指定输出文件、fourCC视频编码、FPS帧率、画面大小
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,  480))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("无法打开摄像头")
        break

    # 对画面帧进行处理
    # 这里是将画面翻转   
    frame = cv2.flip(frame, 0)
    
    # 将处理后的画面逐帧保存至output文件中
    out.write(frame)
    # 将处理后的画面逐帧显示在窗口中
    cv2.imshow('frame', frame)
    # 获取键盘按键动作，如果按下q键，就跳出循环
    if cv2.waitKey(1) == ord('q'):
        break
    
# 关闭摄像头、视频保存器、窗口
cap.release()
out.release()
cv2.destroyAllWindows()
