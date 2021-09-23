#!/usr/bin/env python
# coding: UTF-8

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
# To install this module, run:
# python -m pip install Pillow
from PIL import Image, ImageDraw
import numpy as np
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person

KEY = '62458807cbd94b9097d6ba36bab6caf5'
ENDPOINT = 'https://cmoon-face.cognitiveservices.azure.com/'

# Create an authenticated FaceClient.
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))
# image = Image.open("/home/cmoon/图片/face.jpeg")
image = open("/home/cmoon/图片/face.jpeg", 'rb')
# print(image.read())
path = r"/home/cmoon/图片/face.jpeg"
# img = np.array(image)

detected_faces = face_client.face.detect_with_stream(image=image, return_face_id=True,
                                                     return_face_landmarks=False,
                                                     return_face_attributes=['age', 'gender', 'glasses', 'emotion',
                                                                             'hair'],
                                                     recognition_model='recognition_01',
                                                     return_recognition_model=False, detection_model='detection_01',
                                                     face_id_time_to_live=86400, custom_headers=None, raw=False,
                                                     callback=None, **{})
print(detected_faces[0].face_attributes)
print(1)
# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# cap.open(0)
# detected_faces=None
# while cap.isOpened():
#     flag, frame = cap.read()
#     detected_faces = face_client.face.detect_with_stream(image=frame, return_face_id=True, return_face_landmarks=False,
#                                                          return_face_attributes=None,
#                                                          recognition_model='recognition_01',
#                                                          return_recognition_model=False, detection_model='detection_01',
#                                                          face_id_time_to_live=86400, custom_headers=None, raw=False,
#                                                          callback=None, **{})
# cap.release()
