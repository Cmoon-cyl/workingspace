// Auto-generated. Do not edit!

// (in-package cmoon_msgs.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class yoloRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.signal = null;
    }
    else {
      if (initObj.hasOwnProperty('signal')) {
        this.signal = initObj.signal
      }
      else {
        this.signal = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type yoloRequest
    // Serialize message field [signal]
    bufferOffset = _serializer.string(obj.signal, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type yoloRequest
    let len;
    let data = new yoloRequest(null);
    // Deserialize message field [signal]
    data.signal = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.signal.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'cmoon_msgs/yoloRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '9591b8ace81feee36c93130ad3fe6a19';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string signal
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new yoloRequest(null);
    if (msg.signal !== undefined) {
      resolved.signal = msg.signal;
    }
    else {
      resolved.signal = ''
    }

    return resolved;
    }
};

class yoloResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.data = null;
    }
    else {
      if (initObj.hasOwnProperty('data')) {
        this.data = initObj.data
      }
      else {
        this.data = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type yoloResponse
    // Serialize message field [data]
    bufferOffset = _serializer.string(obj.data, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type yoloResponse
    let len;
    let data = new yoloResponse(null);
    // Deserialize message field [data]
    data.data = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.data.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'cmoon_msgs/yoloResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '992ce8a1687cec8c8bd883ec73ca41d1';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string data
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new yoloResponse(null);
    if (msg.data !== undefined) {
      resolved.data = msg.data;
    }
    else {
      resolved.data = ''
    }

    return resolved;
    }
};

module.exports = {
  Request: yoloRequest,
  Response: yoloResponse,
  md5sum() { return 'cf326eebca4f15f37190d8048e512cec'; },
  datatype() { return 'cmoon_msgs/yolo'; }
};
