; Auto-generated. Do not edit!


(cl:in-package cmoon_msgs-srv)


;//! \htmlinclude yolo-request.msg.html

(cl:defclass <yolo-request> (roslisp-msg-protocol:ros-message)
  ((signal
    :reader signal
    :initarg :signal
    :type cl:string
    :initform ""))
)

(cl:defclass yolo-request (<yolo-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <yolo-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'yolo-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name cmoon_msgs-srv:<yolo-request> is deprecated: use cmoon_msgs-srv:yolo-request instead.")))

(cl:ensure-generic-function 'signal-val :lambda-list '(m))
(cl:defmethod signal-val ((m <yolo-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cmoon_msgs-srv:signal-val is deprecated.  Use cmoon_msgs-srv:signal instead.")
  (signal m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <yolo-request>) ostream)
  "Serializes a message object of type '<yolo-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'signal))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'signal))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <yolo-request>) istream)
  "Deserializes a message object of type '<yolo-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'signal) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'signal) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<yolo-request>)))
  "Returns string type for a service object of type '<yolo-request>"
  "cmoon_msgs/yoloRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'yolo-request)))
  "Returns string type for a service object of type 'yolo-request"
  "cmoon_msgs/yoloRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<yolo-request>)))
  "Returns md5sum for a message object of type '<yolo-request>"
  "cf326eebca4f15f37190d8048e512cec")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'yolo-request)))
  "Returns md5sum for a message object of type 'yolo-request"
  "cf326eebca4f15f37190d8048e512cec")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<yolo-request>)))
  "Returns full string definition for message of type '<yolo-request>"
  (cl:format cl:nil "string signal~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'yolo-request)))
  "Returns full string definition for message of type 'yolo-request"
  (cl:format cl:nil "string signal~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <yolo-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'signal))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <yolo-request>))
  "Converts a ROS message object to a list"
  (cl:list 'yolo-request
    (cl:cons ':signal (signal msg))
))
;//! \htmlinclude yolo-response.msg.html

(cl:defclass <yolo-response> (roslisp-msg-protocol:ros-message)
  ((data
    :reader data
    :initarg :data
    :type cl:string
    :initform ""))
)

(cl:defclass yolo-response (<yolo-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <yolo-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'yolo-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name cmoon_msgs-srv:<yolo-response> is deprecated: use cmoon_msgs-srv:yolo-response instead.")))

(cl:ensure-generic-function 'data-val :lambda-list '(m))
(cl:defmethod data-val ((m <yolo-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cmoon_msgs-srv:data-val is deprecated.  Use cmoon_msgs-srv:data instead.")
  (data m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <yolo-response>) ostream)
  "Serializes a message object of type '<yolo-response>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'data))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'data))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <yolo-response>) istream)
  "Deserializes a message object of type '<yolo-response>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'data) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'data) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<yolo-response>)))
  "Returns string type for a service object of type '<yolo-response>"
  "cmoon_msgs/yoloResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'yolo-response)))
  "Returns string type for a service object of type 'yolo-response"
  "cmoon_msgs/yoloResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<yolo-response>)))
  "Returns md5sum for a message object of type '<yolo-response>"
  "cf326eebca4f15f37190d8048e512cec")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'yolo-response)))
  "Returns md5sum for a message object of type 'yolo-response"
  "cf326eebca4f15f37190d8048e512cec")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<yolo-response>)))
  "Returns full string definition for message of type '<yolo-response>"
  (cl:format cl:nil "string data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'yolo-response)))
  "Returns full string definition for message of type 'yolo-response"
  (cl:format cl:nil "string data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <yolo-response>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'data))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <yolo-response>))
  "Converts a ROS message object to a list"
  (cl:list 'yolo-response
    (cl:cons ':data (data msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'yolo)))
  'yolo-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'yolo)))
  'yolo-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'yolo)))
  "Returns string type for a service object of type '<yolo>"
  "cmoon_msgs/yolo")