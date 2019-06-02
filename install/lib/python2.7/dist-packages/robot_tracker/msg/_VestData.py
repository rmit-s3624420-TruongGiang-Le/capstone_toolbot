# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from robot_tracker/VestData.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class VestData(genpy.Message):
  _md5sum = "bd3cd6db93142c19287d94b60eb73095"
  _type = "robot_tracker/VestData"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """std_msgs/Float32 x_center
std_msgs/Float32 y_center
std_msgs/Float32 area
std_msgs/Float32 rotation_angle
std_msgs/Float32 cam_height
std_msgs/Float32 cam_width

================================================================================
MSG: std_msgs/Float32
float32 data"""
  __slots__ = ['x_center','y_center','area','rotation_angle','cam_height','cam_width']
  _slot_types = ['std_msgs/Float32','std_msgs/Float32','std_msgs/Float32','std_msgs/Float32','std_msgs/Float32','std_msgs/Float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       x_center,y_center,area,rotation_angle,cam_height,cam_width

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(VestData, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.x_center is None:
        self.x_center = std_msgs.msg.Float32()
      if self.y_center is None:
        self.y_center = std_msgs.msg.Float32()
      if self.area is None:
        self.area = std_msgs.msg.Float32()
      if self.rotation_angle is None:
        self.rotation_angle = std_msgs.msg.Float32()
      if self.cam_height is None:
        self.cam_height = std_msgs.msg.Float32()
      if self.cam_width is None:
        self.cam_width = std_msgs.msg.Float32()
    else:
      self.x_center = std_msgs.msg.Float32()
      self.y_center = std_msgs.msg.Float32()
      self.area = std_msgs.msg.Float32()
      self.rotation_angle = std_msgs.msg.Float32()
      self.cam_height = std_msgs.msg.Float32()
      self.cam_width = std_msgs.msg.Float32()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_6f().pack(_x.x_center.data, _x.y_center.data, _x.area.data, _x.rotation_angle.data, _x.cam_height.data, _x.cam_width.data))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.x_center is None:
        self.x_center = std_msgs.msg.Float32()
      if self.y_center is None:
        self.y_center = std_msgs.msg.Float32()
      if self.area is None:
        self.area = std_msgs.msg.Float32()
      if self.rotation_angle is None:
        self.rotation_angle = std_msgs.msg.Float32()
      if self.cam_height is None:
        self.cam_height = std_msgs.msg.Float32()
      if self.cam_width is None:
        self.cam_width = std_msgs.msg.Float32()
      end = 0
      _x = self
      start = end
      end += 24
      (_x.x_center.data, _x.y_center.data, _x.area.data, _x.rotation_angle.data, _x.cam_height.data, _x.cam_width.data,) = _get_struct_6f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_6f().pack(_x.x_center.data, _x.y_center.data, _x.area.data, _x.rotation_angle.data, _x.cam_height.data, _x.cam_width.data))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.x_center is None:
        self.x_center = std_msgs.msg.Float32()
      if self.y_center is None:
        self.y_center = std_msgs.msg.Float32()
      if self.area is None:
        self.area = std_msgs.msg.Float32()
      if self.rotation_angle is None:
        self.rotation_angle = std_msgs.msg.Float32()
      if self.cam_height is None:
        self.cam_height = std_msgs.msg.Float32()
      if self.cam_width is None:
        self.cam_width = std_msgs.msg.Float32()
      end = 0
      _x = self
      start = end
      end += 24
      (_x.x_center.data, _x.y_center.data, _x.area.data, _x.rotation_angle.data, _x.cam_height.data, _x.cam_width.data,) = _get_struct_6f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_6f = None
def _get_struct_6f():
    global _struct_6f
    if _struct_6f is None:
        _struct_6f = struct.Struct("<6f")
    return _struct_6f