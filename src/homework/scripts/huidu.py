#!/usr/bin/env python
# coding: utf-8
import numpy as np
import cv2
img = cv2.imread('/home/cmoon/图片/bizhi.jpg', 0)
cv2.imshow('image', img)
cv2.namedWindow('image',cv2.AUTO_SIZE)
k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('46.png', img)
    cv2.destoryAllWindows()
