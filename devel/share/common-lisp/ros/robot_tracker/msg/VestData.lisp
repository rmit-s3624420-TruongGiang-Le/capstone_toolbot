; Auto-generated. Do not edit!


(cl:in-package robot_tracker-msg)


;//! \htmlinclude VestData.msg.html

(cl:defclass <VestData> (roslisp-msg-protocol:ros-message)
  ((x_center
    :reader x_center
    :initarg :x_center
    :type cl:float
    :initform 0.0)
   (y_center
    :reader y_center
    :initarg :y_center
    :type cl:float
    :initform 0.0)
   (area
    :reader area
    :initarg :area
    :type cl:float
    :initform 0.0)
   (rotation_angle
    :reader rotation_angle
    :initarg :rotation_angle
    :type cl:float
    :initform 0.0)
   (cam_height
    :reader cam_height
    :initarg :cam_height
    :type cl:float
    :initform 0.0)
   (cam_width
    :reader cam_width
    :initarg :cam_width
    :type cl:float
    :initform 0.0))
)

(cl:defclass VestData (<VestData>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <VestData>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'VestData)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name robot_tracker-msg:<VestData> is deprecated: use robot_tracker-msg:VestData instead.")))

(cl:ensure-generic-function 'x_center-val :lambda-list '(m))
(cl:defmethod x_center-val ((m <VestData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_tracker-msg:x_center-val is deprecated.  Use robot_tracker-msg:x_center instead.")
  (x_center m))

(cl:ensure-generic-function 'y_center-val :lambda-list '(m))
(cl:defmethod y_center-val ((m <VestData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_tracker-msg:y_center-val is deprecated.  Use robot_tracker-msg:y_center instead.")
  (y_center m))

(cl:ensure-generic-function 'area-val :lambda-list '(m))
(cl:defmethod area-val ((m <VestData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_tracker-msg:area-val is deprecated.  Use robot_tracker-msg:area instead.")
  (area m))

(cl:ensure-generic-function 'rotation_angle-val :lambda-list '(m))
(cl:defmethod rotation_angle-val ((m <VestData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_tracker-msg:rotation_angle-val is deprecated.  Use robot_tracker-msg:rotation_angle instead.")
  (rotation_angle m))

(cl:ensure-generic-function 'cam_height-val :lambda-list '(m))
(cl:defmethod cam_height-val ((m <VestData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_tracker-msg:cam_height-val is deprecated.  Use robot_tracker-msg:cam_height instead.")
  (cam_height m))

(cl:ensure-generic-function 'cam_width-val :lambda-list '(m))
(cl:defmethod cam_width-val ((m <VestData>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_tracker-msg:cam_width-val is deprecated.  Use robot_tracker-msg:cam_width instead.")
  (cam_width m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <VestData>) ostream)
  "Serializes a message object of type '<VestData>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'x_center))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'y_center))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'area))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'rotation_angle))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'cam_height))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'cam_width))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <VestData>) istream)
  "Deserializes a message object of type '<VestData>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'x_center) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'y_center) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'area) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'rotation_angle) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'cam_height) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'cam_width) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<VestData>)))
  "Returns string type for a message object of type '<VestData>"
  "robot_tracker/VestData")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'VestData)))
  "Returns string type for a message object of type 'VestData"
  "robot_tracker/VestData")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<VestData>)))
  "Returns md5sum for a message object of type '<VestData>"
  "009a90b705b09d3266a4baee5469658e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'VestData)))
  "Returns md5sum for a message object of type 'VestData"
  "009a90b705b09d3266a4baee5469658e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<VestData>)))
  "Returns full string definition for message of type '<VestData>"
  (cl:format cl:nil "float32 x_center~%float32 y_center~%float32 area~%float32 rotation_angle~%float32 cam_height~%float32 cam_width~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'VestData)))
  "Returns full string definition for message of type 'VestData"
  (cl:format cl:nil "float32 x_center~%float32 y_center~%float32 area~%float32 rotation_angle~%float32 cam_height~%float32 cam_width~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <VestData>))
  (cl:+ 0
     4
     4
     4
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <VestData>))
  "Converts a ROS message object to a list"
  (cl:list 'VestData
    (cl:cons ':x_center (x_center msg))
    (cl:cons ':y_center (y_center msg))
    (cl:cons ':area (area msg))
    (cl:cons ':rotation_angle (rotation_angle msg))
    (cl:cons ':cam_height (cam_height msg))
    (cl:cons ':cam_width (cam_width msg))
))
