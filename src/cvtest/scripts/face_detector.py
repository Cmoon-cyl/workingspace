#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image, RegionOfInterest
from cv_bridge import CvBridge, CvBridgeError


class faceDetector:
    def __init__(self):
        rospy.on_shutdown(self.cleanup)

        self.bridge = CvBridge()
        self.image_pub = rospy.Publisher(
            "cv_bridge_image", Image, queue_size=1)

        cascade_1 = rospy.get_param("~cascade_1", "")
        cascade_2 = rospy.get_param("~cascade_2", "")

        self.cascade_1 = cv2.CascadeClassifier(cascade_1)
        self.cascade_2 = cv2.CascadeClassifier(cascade_2)

        self.haar_scaleFactor = rospy.get_param("~haar_scaleFactor", 1.2)
        self.haar_minNeighbors = rospy.get_param("~haar_minNeighbors", 2)
        self.haar_minSize = rospy.get_param("~haar_minSize", 40)
        self.haar_maxSize = rospy.get_param("~haar_maxSize", 60)
        self.color = (50, 255, 50)

        self.image_sub = rospy.Subscriber(
            "input_rgb_image", Image, self.image_callback, queue_size=1)

    def image_callback(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
            frame = np.array(cv_image, dtype=np.uint8)
        # except EnvironmentError, e:
        #     pass

        grey_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        grey_image = cv2.equalizeHist(grey_image)
        faces_result = self.detect_face(grey_image)

        if len(faces_result) > 0:
            for face in faces_result:
                x, y, w, h = face
                cv2.rectangle(cv_image, (x, y), (x + w, y + h), self.color, 2)

        self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, "bgr8"))

    def detect_face(self, input_image):
        if self.cascade_1:
            faces = self.cascade_1.detectMultiScale(input_image,
                                                    self.haar_scaleFactor,
                                                    self.haar_minNeighbors,
                                                    cv2.CASCADE_SCALE_IMAGE,
                                                    (self.haar_minSize, self.haar_maxSize))

        if len(faces) == 0 and self.cascade_2:
            faces = self.cascade_2.detectMultiScale(input_image,
                                                    self.haar_scaleFactor,
                                                    self.haar_minNeighbors,
                                                    cv2.CASCADE_SCALE_IMAGE,
                                                    (self.haar_minSize, self.haar_maxSize))

        return faces

    def cleanup(self):
        print "Shutting down vision node."
        cv2.destroyAllWindows()


if __name__ == '__main__':
    try:
        rospy.init_node("face_detector")
        faceDetector()
        rospy.loginfo("Face detector is started..")
        rospy.loginfo("Please subscribe the ROS image.")
        rospy.spin()
    except KeyboardInterrupt:
        print "Shutting down face detector node."
        cv2.destroyAllWindows()
