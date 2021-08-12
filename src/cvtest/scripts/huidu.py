#!/usr/bin/env python
# coding: utf-8
import numpy as np
import cv2
img = cv2.imread('/home/cmoon/图片/test1.png', 1)
dstImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('image', dstImg)

k = cv2.waitKey(0)&0xFF
if(k == ord("q")):
     cv2.destroyAllWindows()