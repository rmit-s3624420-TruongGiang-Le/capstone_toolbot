
(cl:in-package :asdf)

(defsystem "robot_tracker-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "VestData" :depends-on ("_package_VestData"))
    (:file "_package_VestData" :depends-on ("_package"))
  ))