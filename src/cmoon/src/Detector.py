#!/usr/bin/env python
# coding: UTF-8 

import rospy
import asyncio
import io
import glob
import os
import sys
import time
import uuid
import requests
from urllib.parse import urlparse
from io import BytesIO
from PIL import Image, ImageDraw
import numpy as np
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person


class Detector:
    def __init__(self):
        self._key = '62458807cbd94b9097d6ba36bab6caf5'
        self._endpoint = 'https://cmoon-face.cognitiveservices.azure.com/'
        print('Ready')

    def find_face(self, path, landmark=False, attributes=None):
        """
        example:path=/home/cmoon/图片/face.jpeg
        JPEG, PNG, GIF, BMP supported
        attributes=['age','gender','glasses','emotion',...]
        """

        face_client = FaceClient(self._endpoint, CognitiveServicesCredentials(self._key))
        image = open("/home/cmoon/图片/face.jpeg", 'rb')
        detected_faces = face_client.face.detect_with_stream(image=image,
                                                             return_face_landmarks=landmark,
                                                             return_face_attributes=attributes,
                                                             recognition_model='recognition_01',
                                                             detection_model='detection_01')
        id = detected_faces[0].face_id
        rectangle = detected_faces[0].face_rectangle
        attribute = detected_faces[0].face_attributes
        return id, attribute, rectangle

    def find_body(self):
        pass

    def find_object(self):
        pass


if __name__ == '__main__':
    try:
        rospy.init_node('name', anonymous=True)
        detector = Detector()
        id, attribute, rectangle = detector.find_face(r'/home/cmoon/图片/face.jpeg', attributes=['age', 'gender'])
        print(attribute.age)
        # rospy.spin()
    except rospy.ROSInterruptException:
        pass
