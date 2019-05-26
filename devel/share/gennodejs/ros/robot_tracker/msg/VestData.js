// Auto-generated. Do not edit!

// (in-package robot_tracker.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class VestData {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.x_center = null;
      this.y_center = null;
      this.area = null;
      this.rotation_angle = null;
      this.cam_height = null;
      this.cam_width = null;
    }
    else {
      if (initObj.hasOwnProperty('x_center')) {
        this.x_center = initObj.x_center
      }
      else {
        this.x_center = 0.0;
      }
      if (initObj.hasOwnProperty('y_center')) {
        this.y_center = initObj.y_center
      }
      else {
        this.y_center = 0.0;
      }
      if (initObj.hasOwnProperty('area')) {
        this.area = initObj.area
      }
      else {
        this.area = 0.0;
      }
      if (initObj.hasOwnProperty('rotation_angle')) {
        this.rotation_angle = initObj.rotation_angle
      }
      else {
        this.rotation_angle = 0.0;
      }
      if (initObj.hasOwnProperty('cam_height')) {
        this.cam_height = initObj.cam_height
      }
      else {
        this.cam_height = 0.0;
      }
      if (initObj.hasOwnProperty('cam_width')) {
        this.cam_width = initObj.cam_width
      }
      else {
        this.cam_width = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type VestData
    // Serialize message field [x_center]
    bufferOffset = _serializer.float32(obj.x_center, buffer, bufferOffset);
    // Serialize message field [y_center]
    bufferOffset = _serializer.float32(obj.y_center, buffer, bufferOffset);
    // Serialize message field [area]
    bufferOffset = _serializer.float32(obj.area, buffer, bufferOffset);
    // Serialize message field [rotation_angle]
    bufferOffset = _serializer.float32(obj.rotation_angle, buffer, bufferOffset);
    // Serialize message field [cam_height]
    bufferOffset = _serializer.float32(obj.cam_height, buffer, bufferOffset);
    // Serialize message field [cam_width]
    bufferOffset = _serializer.float32(obj.cam_width, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type VestData
    let len;
    let data = new VestData(null);
    // Deserialize message field [x_center]
    data.x_center = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [y_center]
    data.y_center = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [area]
    data.area = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [rotation_angle]
    data.rotation_angle = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [cam_height]
    data.cam_height = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [cam_width]
    data.cam_width = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 24;
  }

  static datatype() {
    // Returns string type for a message object
    return 'robot_tracker/VestData';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '009a90b705b09d3266a4baee5469658e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 x_center
    float32 y_center
    float32 area
    float32 rotation_angle
    float32 cam_height
    float32 cam_width
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new VestData(null);
    if (msg.x_center !== undefined) {
      resolved.x_center = msg.x_center;
    }
    else {
      resolved.x_center = 0.0
    }

    if (msg.y_center !== undefined) {
      resolved.y_center = msg.y_center;
    }
    else {
      resolved.y_center = 0.0
    }

    if (msg.area !== undefined) {
      resolved.area = msg.area;
    }
    else {
      resolved.area = 0.0
    }

    if (msg.rotation_angle !== undefined) {
      resolved.rotation_angle = msg.rotation_angle;
    }
    else {
      resolved.rotation_angle = 0.0
    }

    if (msg.cam_height !== undefined) {
      resolved.cam_height = msg.cam_height;
    }
    else {
      resolved.cam_height = 0.0
    }

    if (msg.cam_width !== undefined) {
      resolved.cam_width = msg.cam_width;
    }
    else {
      resolved.cam_width = 0.0
    }

    return resolved;
    }
};

module.exports = VestData;
