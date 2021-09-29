#!/usr/bin/python3
# coding: UTF-8 

import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import String
from pdfmaker import Pdfmaker

IMAGE_WIDTH = 1241
IMAGE_HEIGHT = 376
# from numpy
import os
import cv2
import torch
import torch.backends.cudnn as cudnn
import numpy as np
from models.experimental import attempt_load
from utils.general import (
    check_img_size, non_max_suppression, apply_classifier, scale_coords,
    xyxy2xywh, plot_one_box, strip_optimizer, set_logging)
from utils.torch_utils import select_device, load_classifier, time_synchronized
from cmoon_msgs.msg import Point

ros_image = 0


class Detector:
    def __init__(self):
        set_logging()
        self.device = select_device('')
        self.K = np.array([614.86962890625, 0.0, 635.5834350585938,
                           0.0, 614.7677612304688, 364.99200439453125,
                           0.0, 0.0, 1.0]).reshape(3, 3)
        print(self.K)
        self.K = np.linalg.inv(self.K)  # 矩阵求逆
        print(self.K)
        self.half = self.device.type != 'cpu'  # half precision only supported on CUDA
        self.path = os.path.dirname(os.path.dirname(__file__)) + '/src/minyolo5/weights'
        self.weights = self.path + '/yolov5s_old.pt'
        self.imgsz = 640
        np.set_printoptions(threshold=np.inf)
        self.model = attempt_load(self.weights, map_location=self.device)  # load FP32 model
        self.imgsz = check_img_size(self.imgsz, s=self.model.stride.max())  # check img_size

        if self.half:
            self.model.half()  # to FP16
        # rospy.Subscriber('/rgb_image', Image, self.image_callback, queue_size=1, buff_size=52428800)
        rospy.Subscriber('/k4a/rgb/image_raw', Image, self.image_callback, queue_size=1, buff_size=52428800)
        # rospy.Subscriber('/dep_image', Image, self.image_dep_callback, queue_size=1, buff_size=52428800)
        rospy.Subscriber('/k4a/depth_to_rgb/image_raw', Image, self.image_dep_callback, queue_size=1,
                         buff_size=52428800)
        rospy.Subscriber('/ros2yolo', String, self.send_img, queue_size=1)
        self.pdfmaker = Pdfmaker()
        self.yolo_result = rospy.Publisher('/yolo_result', Point, queue_size=1)
        self.rubbish_number = 0
        self.ros_image_depth = None
        # self.ros_image = None

    def image_dep_callback(self, image):
        self.ros_image_depth = np.frombuffer(image.data, dtype=np.uint16).reshape(image.height, image.width, -1)
        # print(self.ros_image_depth.shape)

    def image_callback(self, image):
        # global ros_image
        img = np.frombuffer(image.data, dtype=np.uint8).reshape(image.height, image.width, -1)
        self.ros_image = cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)

    def send_img(self, msg):
        coorindate_cls = list()  # 存放类别,x1,y1,x2,y2
        target_coorindate = list()  # 存放目标点三维坐标 二维列表
        point = Point()
        with torch.no_grad():
            coorindate_cls = self.detect()
        if (coorindate_cls != list()):
            for cls in coorindate_cls:
                center_x = round((cls[3] - cls[1]) / 2 + cls[1])
                center_y = round((cls[4] - cls[2]) / 2 + cls[2])
                print("coor:%s,%s" % (center_x, center_y))
                dep = self.ros_image_depth[center_y][center_x].item()
                if (dep > 100):  # 大于10cm
                    image_coorindate = np.array([center_x * dep, center_y * dep, dep]).reshape(3, 1)  # 图像坐标
                    camera_coorindate = np.dot(self.K, image_coorindate)  # 相机坐标
                    # 坐标1mm 转变后除100变m
                    target_coorindate.append([cls[0], camera_coorindate[0].item() / 1000,
                                              camera_coorindate[1].item() / 1000,
                                              camera_coorindate[2].item() / 1000,
                                              ]
                                             )
                    point.result = cls[0]
                    point.x = camera_coorindate[0].item() / 1000
                    point.y = camera_coorindate[1].item() / 1000
                    point.z = camera_coorindate[2].item() / 1000
                    print('publishing')
                    self.yolo_result.publish(point)

        print(target_coorindate)

    def detect(self):
        coorindate_cls = list()
        global ros_image
        cudnn.benchmark = True
        dataset = self.loadimg(self.ros_image)
        # print(dataset[3])
        # plt.imshow(dataset[2][:, :, ::-1])
        names = self.model.module.names if hasattr(self.model, 'module') else self.model.names
        # colors = [[random.randint(0, 255) for _ in range(3)] for _ in range(len(names))]
        # colors=[[0,255,0]]
        augment = 'store_true'
        conf_thres = 0.3
        iou_thres = 0.45
        # classes = (0,39, 64, 67)  # (0,1,2)
        classes = [i for i in range(80)]  # (0,1,2)
        agnostic_nms = 'store_true'
        img = torch.zeros((1, 3, self.imgsz, self.imgsz), device=self.device)  # init img
        _ = self.model(img.half() if self.half else img) if self.device.type != 'cpu' else None  # run once
        path = dataset[0]
        img = dataset[1]
        im0s = dataset[2]
        vid_cap = dataset[3]
        img = torch.from_numpy(img).to(self.device)
        img = img.half() if self.half else img.float()  # uint8 to fp16/32
        img /= 255.0  # 0 - 255 to 0.0 - 1.0

        if img.ndimension() == 3:
            img = img.unsqueeze(0)
        # Inference
        pred = self.model(img, augment=augment)[0]
        # Apply NMS
        pred = non_max_suppression(pred, conf_thres, iou_thres, classes=classes, agnostic=agnostic_nms)

        view_img = 1
        save_txt = 1
        save_conf = 'store_true'

        for i, det in enumerate(pred):  # detections per image
            p, s, im0 = path, '', im0s
            # s += '%gx%g ' % img.shape[2:]  # print string
            gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]  # normalization gain whwh
            if det is not None:
                # print(det)
                # Rescale boxes from img_size to im0 size
                det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()
                # Print results
                for c in det[:, -1].unique():
                    n = (det[:, -1] == c).sum()  # detections per class
                    # s += '%g %ss, ' % (n, names[int(c)])  # add to string
                    s = names[int(c)]  # add to string
                    # Write results
                for *xyxy, conf, cls in reversed(det):  # v x1 y1 x2 y2
                    coorindate_cls.append(
                        [names[int(cls)], xyxy[:][0].item(), xyxy[:][1].item(), xyxy[:][2].item(), xyxy[:][3].item()])
                    if save_txt:  # Write to file
                        xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / gn).view(-1).tolist()  # normalized xywh
                        line = (cls, conf, *xywh) if save_conf else (cls, *xywh)  # label format
                    if view_img:  # Add bbox to image
                        c = int(cls)  # integer class
                        label = '%s %.2f' % (names[int(cls)], conf)

                        plot_one_box(xyxy, im0, label=label, color=[0, 255, 0], line_thickness=3)
                        # print("shape",im0.shape)

                if s != '':
                    print(s)
                    self.rubbish_number += 1
                    ros_image = im0[:, :, [2, 1, 0]]
                    # path = os.path.dirname(os.path.dirname(__file__)) + '/pdf/'
                    # savename = path + 'rubbish' + str(self.rubbish_number) + '.jpg'
                    # cv2.imwrite(savename, ros_image)
                    # self.pdfmaker.write_img(savename)
        out_img = im0[:, :, [2, 1, 0]]
        cv2.namedWindow('yolo', cv2.WINDOW_NORMAL)
        # cv2.resizeWindow('yolo', 640, 480)
        cv2.resizeWindow('yolo', 1280, 640)
        cv2.startWindowThread()
        cv2.imshow('yolo', out_img)
        cv2.waitKey(1)
        return coorindate_cls

    def loadimg(self, img):  # 接受opencv图片
        img_size = 640
        cap = None
        path = None
        img0 = img
        img = self.letterbox(img0, new_shape=img_size)[0]
        img = img[:, :, ::-1].transpose(2, 0, 1)  # BGR to RGB, to 3x416x416
        img = np.ascontiguousarray(img)
        return path, img, img0, cap

    def letterbox(self, img, new_shape=(640, 640), color=(114, 114, 114), auto=True, scaleFill=False, scaleup=True):
        # Resize image to a 32-pixel-multiple rectangle https://github.com/ultralytics/yolov3/issues/232
        shape = img.shape[:2]  # current shape [height, width]
        if isinstance(new_shape, int):
            new_shape = (new_shape, new_shape)

        # Scale ratio (new / old)
        r = min(new_shape[0] / shape[0], new_shape[1] / shape[1])
        if not scaleup:  # only scale down, do not scale up (for better test mAP)
            r = min(r, 1.0)

        # Compute padding
        ratio = r, r  # width, height ratios
        new_unpad = int(round(shape[1] * r)), int(round(shape[0] * r))
        dw, dh = new_shape[1] - new_unpad[0], new_shape[0] - new_unpad[1]  # wh padding
        if auto:  # minimum rectangle
            dw, dh = np.mod(dw, 32), np.mod(dh, 32)  # wh padding
        elif scaleFill:  # stretch
            dw, dh = 0.0, 0.0
            new_unpad = (new_shape[1], new_shape[0])
            ratio = new_shape[1] / shape[1], new_shape[0] / shape[0]  # width, height ratios

        dw /= 2  # divide padding into 2 sides
        dh /= 2

        if shape[::-1] != new_unpad:  # resize
            img = cv2.resize(img, new_unpad, interpolation=cv2.INTER_LINEAR)
        top, bottom = int(round(dh - 0.1)), int(round(dh + 0.1))
        left, right = int(round(dw - 0.1)), int(round(dw + 0.1))
        img = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)  # add border
        return img, ratio, (dw, dh)


if __name__ == '__main__':
    try:
        rospy.init_node('detector', anonymous=True)
        Detector()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
