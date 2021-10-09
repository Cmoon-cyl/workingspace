;; Auto-generated. Do not edit!


(when (boundp 'cmoon_msgs::point)
  (if (not (find-package "CMOON_MSGS"))
    (make-package "CMOON_MSGS"))
  (shadow 'point (find-package "CMOON_MSGS")))
(unless (find-package "CMOON_MSGS::POINT")
  (make-package "CMOON_MSGS::POINT"))

(in-package "ROS")
;;//! \htmlinclude point.msg.html


(defclass cmoon_msgs::point
  :super ros::object
  :slots (_result _x _y _z ))

(defmethod cmoon_msgs::point
  (:init
   (&key
    ((:result __result) "")
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    ((:z __z) 0.0)
    )
   (send-super :init)
   (setq _result (string __result))
   (setq _x (float __x))
   (setq _y (float __y))
   (setq _z (float __z))
   self)
  (:result
   (&optional __result)
   (if __result (setq _result __result)) _result)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:z
   (&optional __z)
   (if __z (setq _z __z)) _z)
  (:serialization-length
   ()
   (+
    ;; string _result
    4 (length _result)
    ;; float64 _x
    8
    ;; float64 _y
    8
    ;; float64 _z
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _result
       (write-long (length _result) s) (princ _result s)
     ;; float64 _x
       (sys::poke _x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _y
       (sys::poke _y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _z
       (sys::poke _z (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _result
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _result (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float64 _x
     (setq _x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _y
     (setq _y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _z
     (setq _z (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get cmoon_msgs::point :md5sum-) "ac77d0373f1087448e62e672b94ba1e5")
(setf (get cmoon_msgs::point :datatype-) "cmoon_msgs/point")
(setf (get cmoon_msgs::point :definition-)
      "string result
float64 x
float64 y
float64 z
")



(provide :cmoon_msgs/point "ac77d0373f1087448e62e672b94ba1e5")


