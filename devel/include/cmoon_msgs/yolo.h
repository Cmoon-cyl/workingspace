// Generated by gencpp from file cmoon_msgs/yolo.msg
// DO NOT EDIT!


#ifndef CMOON_MSGS_MESSAGE_YOLO_H
#define CMOON_MSGS_MESSAGE_YOLO_H

#include <ros/service_traits.h>


#include <cmoon_msgs/yoloRequest.h>
#include <cmoon_msgs/yoloResponse.h>


namespace cmoon_msgs
{

struct yolo
{

typedef yoloRequest Request;
typedef yoloResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct yolo
} // namespace cmoon_msgs


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::cmoon_msgs::yolo > {
  static const char* value()
  {
    return "cf326eebca4f15f37190d8048e512cec";
  }

  static const char* value(const ::cmoon_msgs::yolo&) { return value(); }
};

template<>
struct DataType< ::cmoon_msgs::yolo > {
  static const char* value()
  {
    return "cmoon_msgs/yolo";
  }

  static const char* value(const ::cmoon_msgs::yolo&) { return value(); }
};


// service_traits::MD5Sum< ::cmoon_msgs::yoloRequest> should match
// service_traits::MD5Sum< ::cmoon_msgs::yolo >
template<>
struct MD5Sum< ::cmoon_msgs::yoloRequest>
{
  static const char* value()
  {
    return MD5Sum< ::cmoon_msgs::yolo >::value();
  }
  static const char* value(const ::cmoon_msgs::yoloRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::cmoon_msgs::yoloRequest> should match
// service_traits::DataType< ::cmoon_msgs::yolo >
template<>
struct DataType< ::cmoon_msgs::yoloRequest>
{
  static const char* value()
  {
    return DataType< ::cmoon_msgs::yolo >::value();
  }
  static const char* value(const ::cmoon_msgs::yoloRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::cmoon_msgs::yoloResponse> should match
// service_traits::MD5Sum< ::cmoon_msgs::yolo >
template<>
struct MD5Sum< ::cmoon_msgs::yoloResponse>
{
  static const char* value()
  {
    return MD5Sum< ::cmoon_msgs::yolo >::value();
  }
  static const char* value(const ::cmoon_msgs::yoloResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::cmoon_msgs::yoloResponse> should match
// service_traits::DataType< ::cmoon_msgs::yolo >
template<>
struct DataType< ::cmoon_msgs::yoloResponse>
{
  static const char* value()
  {
    return DataType< ::cmoon_msgs::yolo >::value();
  }
  static const char* value(const ::cmoon_msgs::yoloResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // CMOON_MSGS_MESSAGE_YOLO_H
