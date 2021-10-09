// Auto-generated. Do not edit!

// (in-package cmoon_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class Pose {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.name = null;
      this.px = null;
      this.py = null;
      this.pz = null;
      this.ox = null;
      this.oy = null;
      this.oz = null;
      this.ow = null;
    }
    else {
      if (initObj.hasOwnProperty('name')) {
        this.name = initObj.name
      }
      else {
        this.name = '';
      }
      if (initObj.hasOwnProperty('px')) {
        this.px = initObj.px
      }
      else {
        this.px = 0.0;
      }
      if (initObj.hasOwnProperty('py')) {
        this.py = initObj.py
      }
      else {
        this.py = 0.0;
      }
      if (initObj.hasOwnProperty('pz')) {
        this.pz = initObj.pz
      }
      else {
        this.pz = 0.0;
      }
      if (initObj.hasOwnProperty('ox')) {
        this.ox = initObj.ox
      }
      else {
        this.ox = 0.0;
      }
      if (initObj.hasOwnProperty('oy')) {
        this.oy = initObj.oy
      }
      else {
        this.oy = 0.0;
      }
      if (initObj.hasOwnProperty('oz')) {
        this.oz = initObj.oz
      }
      else {
        this.oz = 0.0;
      }
      if (initObj.hasOwnProperty('ow')) {
        this.ow = initObj.ow
      }
      else {
        this.ow = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Pose
    // Serialize message field [name]
    bufferOffset = _serializer.string(obj.name, buffer, bufferOffset);
    // Serialize message field [px]
    bufferOffset = _serializer.float64(obj.px, buffer, bufferOffset);
    // Serialize message field [py]
    bufferOffset = _serializer.float64(obj.py, buffer, bufferOffset);
    // Serialize message field [pz]
    bufferOffset = _serializer.float64(obj.pz, buffer, bufferOffset);
    // Serialize message field [ox]
    bufferOffset = _serializer.float64(obj.ox, buffer, bufferOffset);
    // Serialize message field [oy]
    bufferOffset = _serializer.float64(obj.oy, buffer, bufferOffset);
    // Serialize message field [oz]
    bufferOffset = _serializer.float64(obj.oz, buffer, bufferOffset);
    // Serialize message field [ow]
    bufferOffset = _serializer.float64(obj.ow, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Pose
    let len;
    let data = new Pose(null);
    // Deserialize message field [name]
    data.name = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [px]
    data.px = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [py]
    data.py = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [pz]
    data.pz = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [ox]
    data.ox = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [oy]
    data.oy = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [oz]
    data.oz = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [ow]
    data.ow = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.name.length;
    return length + 60;
  }

  static datatype() {
    // Returns string type for a message object
    return 'cmoon_msgs/Pose';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'bcfa53d5e4d8be1ea92a3489e7b58000';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string name
    float64 px
    float64 py
    float64 pz
    float64 ox
    float64 oy
    float64 oz
    float64 ow
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Pose(null);
    if (msg.name !== undefined) {
      resolved.name = msg.name;
    }
    else {
      resolved.name = ''
    }

    if (msg.px !== undefined) {
      resolved.px = msg.px;
    }
    else {
      resolved.px = 0.0
    }

    if (msg.py !== undefined) {
      resolved.py = msg.py;
    }
    else {
      resolved.py = 0.0
    }

    if (msg.pz !== undefined) {
      resolved.pz = msg.pz;
    }
    else {
      resolved.pz = 0.0
    }

    if (msg.ox !== undefined) {
      resolved.ox = msg.ox;
    }
    else {
      resolved.ox = 0.0
    }

    if (msg.oy !== undefined) {
      resolved.oy = msg.oy;
    }
    else {
      resolved.oy = 0.0
    }

    if (msg.oz !== undefined) {
      resolved.oz = msg.oz;
    }
    else {
      resolved.oz = 0.0
    }

    if (msg.ow !== undefined) {
      resolved.ow = msg.ow;
    }
    else {
      resolved.ow = 0.0
    }

    return resolved;
    }
};

module.exports = Pose;
