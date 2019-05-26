;; Auto-generated. Do not edit!


(when (boundp 'robot_tracker::VestData)
  (if (not (find-package "ROBOT_TRACKER"))
    (make-package "ROBOT_TRACKER"))
  (shadow 'VestData (find-package "ROBOT_TRACKER")))
(unless (find-package "ROBOT_TRACKER::VESTDATA")
  (make-package "ROBOT_TRACKER::VESTDATA"))

(in-package "ROS")
;;//! \htmlinclude VestData.msg.html


(defclass robot_tracker::VestData
  :super ros::object
  :slots (_x_center _y_center _area _rotation_angle _cam_height _cam_width ))

(defmethod robot_tracker::VestData
  (:init
   (&key
    ((:x_center __x_center) 0.0)
    ((:y_center __y_center) 0.0)
    ((:area __area) 0.0)
    ((:rotation_angle __rotation_angle) 0.0)
    ((:cam_height __cam_height) 0.0)
    ((:cam_width __cam_width) 0.0)
    )
   (send-super :init)
   (setq _x_center (float __x_center))
   (setq _y_center (float __y_center))
   (setq _area (float __area))
   (setq _rotation_angle (float __rotation_angle))
   (setq _cam_height (float __cam_height))
   (setq _cam_width (float __cam_width))
   self)
  (:x_center
   (&optional __x_center)
   (if __x_center (setq _x_center __x_center)) _x_center)
  (:y_center
   (&optional __y_center)
   (if __y_center (setq _y_center __y_center)) _y_center)
  (:area
   (&optional __area)
   (if __area (setq _area __area)) _area)
  (:rotation_angle
   (&optional __rotation_angle)
   (if __rotation_angle (setq _rotation_angle __rotation_angle)) _rotation_angle)
  (:cam_height
   (&optional __cam_height)
   (if __cam_height (setq _cam_height __cam_height)) _cam_height)
  (:cam_width
   (&optional __cam_width)
   (if __cam_width (setq _cam_width __cam_width)) _cam_width)
  (:serialization-length
   ()
   (+
    ;; float32 _x_center
    4
    ;; float32 _y_center
    4
    ;; float32 _area
    4
    ;; float32 _rotation_angle
    4
    ;; float32 _cam_height
    4
    ;; float32 _cam_width
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _x_center
       (sys::poke _x_center (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _y_center
       (sys::poke _y_center (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _area
       (sys::poke _area (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _rotation_angle
       (sys::poke _rotation_angle (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _cam_height
       (sys::poke _cam_height (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _cam_width
       (sys::poke _cam_width (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _x_center
     (setq _x_center (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _y_center
     (setq _y_center (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _area
     (setq _area (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _rotation_angle
     (setq _rotation_angle (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _cam_height
     (setq _cam_height (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _cam_width
     (setq _cam_width (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get robot_tracker::VestData :md5sum-) "009a90b705b09d3266a4baee5469658e")
(setf (get robot_tracker::VestData :datatype-) "robot_tracker/VestData")
(setf (get robot_tracker::VestData :definition-)
      "float32 x_center
float32 y_center
float32 area
float32 rotation_angle
float32 cam_height
float32 cam_width

")



(provide :robot_tracker/VestData "009a90b705b09d3266a4baee5469658e")


