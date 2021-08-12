#!/usr/bin/env python
# coding: utf-8
import cv2 as cv
import numpy as np

src = np.zeros((400, 600, 3), np.uint8)

pt1 = (200, 100)
pt2 = (300, 200)
color = (255, 255, 0)

# 绘制线段 参数2：起始点 参数3：结束点 参数4：颜色 参数5：线条宽度
cv.line(src, pt1, pt2, color, 2)  # 图，zuoshang, youxia, yanse, xiankuan

# 绘制一个矩形 参数2：左上角  参数3：右下角 参数4：颜色  参数5：线条宽度，若为负数，则填充整个矩形
cv.rectangle(src, pt1, pt2, color, 1)

# 绘制圆形 参数2：圆心  参数3：半径  参数4：颜色 参数5：线条宽度，若为负数，则填充整个圆形
cv.circle(src, (400, 200), 50, color, -1)

# 绘制文字 参数2：文字内容  参数3：文字起始左下点
cv.putText(src, "hello", (200, 100), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 255), 2)

# 显示图片
cv.imshow("src", src)
cv.waitKey()