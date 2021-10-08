#!/usr/bin/env python
# coding: UTF-8
# Created by Cmoon

import rospy
import numpy as np
import cv2
from pyKinectAzure import pyKinectAzure, _k4a


class Main:
    def __init__(self):
        self.modulePath = r'/usr/lib/x86_64-linux-gnu/libk4a.so'
        self.k4a = pyKinectAzure(self.modulePath)

    def show(self):
        self.k4a.device_open()
        device_config = self.k4a.config
        device_config.color_resolution = _k4a.K4A_COLOR_RESOLUTION_1080P
        print(device_config)
        self.k4a.device_start_cameras(device_config)
        k = 0
        while True:
            # Get capture
            self.k4a.device_get_capture()

            # Get the color image from the capture
            color_image_handle = self.k4a.capture_get_color_image()

            # Check the image has been read correctly
            if color_image_handle:
                # Read and convert the image data to numpy array:
                color_image = self.k4a.image_convert_to_numpy(color_image_handle)

                # Plot the image
                cv2.namedWindow('Color Image', cv2.WINDOW_NORMAL)
                cv2.imshow("Color Image", color_image)
                k = cv2.waitKey(1)

                # Release the image
                self.k4a.image_release(color_image_handle)

            self.k4a.capture_release()

            if k == 27:  # Esc key to stop
                break

        self.k4a.device_stop_cameras()
        self.k4a.device_close()


if __name__ == '__main__':
    try:
        rospy.init_node('name', anonymous=True)
        k4a = Main()
        k4a.show()
    except rospy.ROSInterruptException:
        pass
