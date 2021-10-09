;; Auto-generated. Do not edit!


(when (boundp 'cmoon_msgs::yolo)
  (if (not (find-package "CMOON_MSGS"))
    (make-package "CMOON_MSGS"))
  (shadow 'yolo (find-package "CMOON_MSGS")))
(unless (find-package "CMOON_MSGS::YOLO")
  (make-package "CMOON_MSGS::YOLO"))
(unless (find-package "CMOON_MSGS::YOLOREQUEST")
  (make-package "CMOON_MSGS::YOLOREQUEST"))
(unless (find-package "CMOON_MSGS::YOLORESPONSE")
  (make-package "CMOON_MSGS::YOLORESPONSE"))

(in-package "ROS")





(defclass cmoon_msgs::yoloRequest
  :super ros::object
  :slots (_signal ))

(defmethod cmoon_msgs::yoloRequest
  (:init
   (&key
    ((:signal __signal) "")
    )
   (send-super :init)
   (setq _signal (string __signal))
   self)
  (:signal
   (&optional __signal)
   (if __signal (setq _signal __signal)) _signal)
  (:serialization-length
   ()
   (+
    ;; string _signal
    4 (length _signal)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _signal
       (write-long (length _signal) s) (princ _signal s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _signal
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _signal (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass cmoon_msgs::yoloResponse
  :super ros::object
  :slots (_data ))

(defmethod cmoon_msgs::yoloResponse
  (:init
   (&key
    ((:data __data) "")
    )
   (send-super :init)
   (setq _data (string __data))
   self)
  (:data
   (&optional __data)
   (if __data (setq _data __data)) _data)
  (:serialization-length
   ()
   (+
    ;; string _data
    4 (length _data)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _data
       (write-long (length _data) s) (princ _data s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _data
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _data (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass cmoon_msgs::yolo
  :super ros::object
  :slots ())

(setf (get cmoon_msgs::yolo :md5sum-) "cf326eebca4f15f37190d8048e512cec")
(setf (get cmoon_msgs::yolo :datatype-) "cmoon_msgs/yolo")
(setf (get cmoon_msgs::yolo :request) cmoon_msgs::yoloRequest)
(setf (get cmoon_msgs::yolo :response) cmoon_msgs::yoloResponse)

(defmethod cmoon_msgs::yoloRequest
  (:response () (instance cmoon_msgs::yoloResponse :init)))

(setf (get cmoon_msgs::yoloRequest :md5sum-) "cf326eebca4f15f37190d8048e512cec")
(setf (get cmoon_msgs::yoloRequest :datatype-) "cmoon_msgs/yoloRequest")
(setf (get cmoon_msgs::yoloRequest :definition-)
      "string signal
---
string data
")

(setf (get cmoon_msgs::yoloResponse :md5sum-) "cf326eebca4f15f37190d8048e512cec")
(setf (get cmoon_msgs::yoloResponse :datatype-) "cmoon_msgs/yoloResponse")
(setf (get cmoon_msgs::yoloResponse :definition-)
      "string signal
---
string data
")



(provide :cmoon_msgs/yolo "cf326eebca4f15f37190d8048e512cec")


