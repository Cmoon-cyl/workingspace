;; Auto-generated. Do not edit!


(when (boundp 'cmoon_msgs::Pose)
  (if (not (find-package "CMOON_MSGS"))
    (make-package "CMOON_MSGS"))
  (shadow 'Pose (find-package "CMOON_MSGS")))
(unless (find-package "CMOON_MSGS::POSE")
  (make-package "CMOON_MSGS::POSE"))

(in-package "ROS")
;;//! \htmlinclude Pose.msg.html


(defclass cmoon_msgs::Pose
  :super ros::object
  :slots (_name _px _py _pz _ox _oy _oz _ow ))

(defmethod cmoon_msgs::Pose
  (:init
   (&key
    ((:name __name) "")
    ((:px __px) 0.0)
    ((:py __py) 0.0)
    ((:pz __pz) 0.0)
    ((:ox __ox) 0.0)
    ((:oy __oy) 0.0)
    ((:oz __oz) 0.0)
    ((:ow __ow) 0.0)
    )
   (send-super :init)
   (setq _name (string __name))
   (setq _px (float __px))
   (setq _py (float __py))
   (setq _pz (float __pz))
   (setq _ox (float __ox))
   (setq _oy (float __oy))
   (setq _oz (float __oz))
   (setq _ow (float __ow))
   self)
  (:name
   (&optional __name)
   (if __name (setq _name __name)) _name)
  (:px
   (&optional __px)
   (if __px (setq _px __px)) _px)
  (:py
   (&optional __py)
   (if __py (setq _py __py)) _py)
  (:pz
   (&optional __pz)
   (if __pz (setq _pz __pz)) _pz)
  (:ox
   (&optional __ox)
   (if __ox (setq _ox __ox)) _ox)
  (:oy
   (&optional __oy)
   (if __oy (setq _oy __oy)) _oy)
  (:oz
   (&optional __oz)
   (if __oz (setq _oz __oz)) _oz)
  (:ow
   (&optional __ow)
   (if __ow (setq _ow __ow)) _ow)
  (:serialization-length
   ()
   (+
    ;; string _name
    4 (length _name)
    ;; float64 _px
    8
    ;; float64 _py
    8
    ;; float64 _pz
    8
    ;; float64 _ox
    8
    ;; float64 _oy
    8
    ;; float64 _oz
    8
    ;; float64 _ow
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _name
       (write-long (length _name) s) (princ _name s)
     ;; float64 _px
       (sys::poke _px (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _py
       (sys::poke _py (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _pz
       (sys::poke _pz (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _ox
       (sys::poke _ox (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _oy
       (sys::poke _oy (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _oz
       (sys::poke _oz (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _ow
       (sys::poke _ow (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float64 _px
     (setq _px (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _py
     (setq _py (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _pz
     (setq _pz (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _ox
     (setq _ox (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _oy
     (setq _oy (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _oz
     (setq _oz (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _ow
     (setq _ow (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get cmoon_msgs::Pose :md5sum-) "bcfa53d5e4d8be1ea92a3489e7b58000")
(setf (get cmoon_msgs::Pose :datatype-) "cmoon_msgs/Pose")
(setf (get cmoon_msgs::Pose :definition-)
      "string name
float64 px
float64 py
float64 pz
float64 ox
float64 oy
float64 oz
float64 ow
")



(provide :cmoon_msgs/Pose "bcfa53d5e4d8be1ea92a3489e7b58000")


