;; Auto-generated. Do not edit!


(when (boundp 'cmoon_msgs::words)
  (if (not (find-package "CMOON_MSGS"))
    (make-package "CMOON_MSGS"))
  (shadow 'words (find-package "CMOON_MSGS")))
(unless (find-package "CMOON_MSGS::WORDS")
  (make-package "CMOON_MSGS::WORDS"))
(unless (find-package "CMOON_MSGS::WORDSREQUEST")
  (make-package "CMOON_MSGS::WORDSREQUEST"))
(unless (find-package "CMOON_MSGS::WORDSRESPONSE")
  (make-package "CMOON_MSGS::WORDSRESPONSE"))

(in-package "ROS")





(defclass cmoon_msgs::wordsRequest
  :super ros::object
  :slots ())

(defmethod cmoon_msgs::wordsRequest
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass cmoon_msgs::wordsResponse
  :super ros::object
  :slots ())

(defmethod cmoon_msgs::wordsResponse
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass cmoon_msgs::words
  :super ros::object
  :slots ())

(setf (get cmoon_msgs::words :md5sum-) "d41d8cd98f00b204e9800998ecf8427e")
(setf (get cmoon_msgs::words :datatype-) "cmoon_msgs/words")
(setf (get cmoon_msgs::words :request) cmoon_msgs::wordsRequest)
(setf (get cmoon_msgs::words :response) cmoon_msgs::wordsResponse)

(defmethod cmoon_msgs::wordsRequest
  (:response () (instance cmoon_msgs::wordsResponse :init)))

(setf (get cmoon_msgs::wordsRequest :md5sum-) "d41d8cd98f00b204e9800998ecf8427e")
(setf (get cmoon_msgs::wordsRequest :datatype-) "cmoon_msgs/wordsRequest")
(setf (get cmoon_msgs::wordsRequest :definition-)
      "
---
")

(setf (get cmoon_msgs::wordsResponse :md5sum-) "d41d8cd98f00b204e9800998ecf8427e")
(setf (get cmoon_msgs::wordsResponse :datatype-) "cmoon_msgs/wordsResponse")
(setf (get cmoon_msgs::wordsResponse :definition-)
      "
---
")



(provide :cmoon_msgs/words "d41d8cd98f00b204e9800998ecf8427e")


