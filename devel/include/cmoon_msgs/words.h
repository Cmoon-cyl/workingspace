// Generated by gencpp from file cmoon_msgs/words.msg
// DO NOT EDIT!


#ifndef CMOON_MSGS_MESSAGE_WORDS_H
#define CMOON_MSGS_MESSAGE_WORDS_H

#include <ros/service_traits.h>


#include <cmoon_msgs/wordsRequest.h>
#include <cmoon_msgs/wordsResponse.h>


namespace cmoon_msgs
{

struct words
{

typedef wordsRequest Request;
typedef wordsResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct words
} // namespace cmoon_msgs


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::cmoon_msgs::words > {
  static const char* value()
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const ::cmoon_msgs::words&) { return value(); }
};

template<>
struct DataType< ::cmoon_msgs::words > {
  static const char* value()
  {
    return "cmoon_msgs/words";
  }

  static const char* value(const ::cmoon_msgs::words&) { return value(); }
};


// service_traits::MD5Sum< ::cmoon_msgs::wordsRequest> should match
// service_traits::MD5Sum< ::cmoon_msgs::words >
template<>
struct MD5Sum< ::cmoon_msgs::wordsRequest>
{
  static const char* value()
  {
    return MD5Sum< ::cmoon_msgs::words >::value();
  }
  static const char* value(const ::cmoon_msgs::wordsRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::cmoon_msgs::wordsRequest> should match
// service_traits::DataType< ::cmoon_msgs::words >
template<>
struct DataType< ::cmoon_msgs::wordsRequest>
{
  static const char* value()
  {
    return DataType< ::cmoon_msgs::words >::value();
  }
  static const char* value(const ::cmoon_msgs::wordsRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::cmoon_msgs::wordsResponse> should match
// service_traits::MD5Sum< ::cmoon_msgs::words >
template<>
struct MD5Sum< ::cmoon_msgs::wordsResponse>
{
  static const char* value()
  {
    return MD5Sum< ::cmoon_msgs::words >::value();
  }
  static const char* value(const ::cmoon_msgs::wordsResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::cmoon_msgs::wordsResponse> should match
// service_traits::DataType< ::cmoon_msgs::words >
template<>
struct DataType< ::cmoon_msgs::wordsResponse>
{
  static const char* value()
  {
    return DataType< ::cmoon_msgs::words >::value();
  }
  static const char* value(const ::cmoon_msgs::wordsResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // CMOON_MSGS_MESSAGE_WORDS_H
