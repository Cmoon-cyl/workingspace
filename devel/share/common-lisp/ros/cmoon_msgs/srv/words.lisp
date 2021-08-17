; Auto-generated. Do not edit!


(cl:in-package cmoon_msgs-srv)


;//! \htmlinclude words-request.msg.html

(cl:defclass <words-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass words-request (<words-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <words-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'words-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name cmoon_msgs-srv:<words-request> is deprecated: use cmoon_msgs-srv:words-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <words-request>) ostream)
  "Serializes a message object of type '<words-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <words-request>) istream)
  "Deserializes a message object of type '<words-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<words-request>)))
  "Returns string type for a service object of type '<words-request>"
  "cmoon_msgs/wordsRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'words-request)))
  "Returns string type for a service object of type 'words-request"
  "cmoon_msgs/wordsRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<words-request>)))
  "Returns md5sum for a message object of type '<words-request>"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'words-request)))
  "Returns md5sum for a message object of type 'words-request"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<words-request>)))
  "Returns full string definition for message of type '<words-request>"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'words-request)))
  "Returns full string definition for message of type 'words-request"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <words-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <words-request>))
  "Converts a ROS message object to a list"
  (cl:list 'words-request
))
;//! \htmlinclude words-response.msg.html

(cl:defclass <words-response> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass words-response (<words-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <words-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'words-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name cmoon_msgs-srv:<words-response> is deprecated: use cmoon_msgs-srv:words-response instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <words-response>) ostream)
  "Serializes a message object of type '<words-response>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <words-response>) istream)
  "Deserializes a message object of type '<words-response>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<words-response>)))
  "Returns string type for a service object of type '<words-response>"
  "cmoon_msgs/wordsResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'words-response)))
  "Returns string type for a service object of type 'words-response"
  "cmoon_msgs/wordsResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<words-response>)))
  "Returns md5sum for a message object of type '<words-response>"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'words-response)))
  "Returns md5sum for a message object of type 'words-response"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<words-response>)))
  "Returns full string definition for message of type '<words-response>"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'words-response)))
  "Returns full string definition for message of type 'words-response"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <words-response>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <words-response>))
  "Converts a ROS message object to a list"
  (cl:list 'words-response
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'words)))
  'words-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'words)))
  'words-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'words)))
  "Returns string type for a service object of type '<words>"
  "cmoon_msgs/words")