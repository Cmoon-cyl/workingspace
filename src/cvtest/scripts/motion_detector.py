#!/usr/bin/env python
# coding: utf-8 
import cv2
import numpy as np

def center(points):
    x=(points[0][0]+points[1][0]+points[2][0]+points[3][0])/4
    y = (points[0][1] + points[1][1] + points[2][1] + points[3][1]) / 4
    return np.array([np.float32(x),np.float32(y)],np.float32)

cap=cv2.VideoCapture(0)
ret,frame=cap.read()
#我这里画面太大了所以缩小点

#跟踪框
track_window=cv2.selectROI('img', frame)

#获得绿色的直方图
hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
mask=cv2.inRange(hsv,np.array((35,43,46)),np.array((77,255,255)))
hist=cv2.calcHist([hsv],[0],mask,[181],[0,180])
cv2.normalize(hist,hist,0,255,cv2.NORM_MINMAX)
term_crit=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT,10,1)

#设置卡尔曼滤波器
klm=cv2.KalmanFilter(4,2)
klm.measurementMatrix = np.array([[1,0,0,0],[0,1,0,0]],np.float32)
klm.transitionMatrix = np.array([[1,0,1,0],[0,1,0,1],[0,0,1,0],[0,0,0,1]],np.float32)
klm.processNoiseCov = np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],np.float32)
while 1:
    ret,frame=cap.read()
    #frame = cv2.resize(frame, None, None, fx=1 / 2, fy=1 / 2, interpolation=cv2.INTER_CUBIC)
    if ret== True:
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        dst=cv2.calcBackProject([hsv],[0],hist,[0,180],1)
        ret,track_window=cv2.meanShift(dst,track_window,term_crit)
        x,y,w,h=track_window
        
        #获得中间坐标
        cent = center([[x, y], [x + w, y], [x, y + h], [x + w, y + h]])
        #修正参数
        klm.correct(cent)
        #预测
        c = klm.predict()
        #画出预测位置
        cv2.circle(frame, (int(c[0]), int(c[1])), 30, (255, 255, 0), -1)
        #画出矩形框
        img=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        (x,y)=img.shape[:2]
        cv2.imshow('img',img)
        if cv2.waitKey(1)==ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()