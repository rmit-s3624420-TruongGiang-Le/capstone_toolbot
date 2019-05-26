// Generated by gencpp from file robot_tracker/VestData.msg
// DO NOT EDIT!


#ifndef ROBOT_TRACKER_MESSAGE_VESTDATA_H
#define ROBOT_TRACKER_MESSAGE_VESTDATA_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace robot_tracker
{
template <class ContainerAllocator>
struct VestData_
{
  typedef VestData_<ContainerAllocator> Type;

  VestData_()
    : x_center(0.0)
    , y_center(0.0)
    , area(0.0)
    , rotation_angle(0.0)
    , cam_height(0.0)
    , cam_width(0.0)  {
    }
  VestData_(const ContainerAllocator& _alloc)
    : x_center(0.0)
    , y_center(0.0)
    , area(0.0)
    , rotation_angle(0.0)
    , cam_height(0.0)
    , cam_width(0.0)  {
  (void)_alloc;
    }



   typedef float _x_center_type;
  _x_center_type x_center;

   typedef float _y_center_type;
  _y_center_type y_center;

   typedef float _area_type;
  _area_type area;

   typedef float _rotation_angle_type;
  _rotation_angle_type rotation_angle;

   typedef float _cam_height_type;
  _cam_height_type cam_height;

   typedef float _cam_width_type;
  _cam_width_type cam_width;





  typedef boost::shared_ptr< ::robot_tracker::VestData_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::robot_tracker::VestData_<ContainerAllocator> const> ConstPtr;

}; // struct VestData_

typedef ::robot_tracker::VestData_<std::allocator<void> > VestData;

typedef boost::shared_ptr< ::robot_tracker::VestData > VestDataPtr;
typedef boost::shared_ptr< ::robot_tracker::VestData const> VestDataConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::robot_tracker::VestData_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::robot_tracker::VestData_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace robot_tracker

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'robot_tracker': ['/home/dev/robot/src/robot_tracker/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::robot_tracker::VestData_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::robot_tracker::VestData_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::robot_tracker::VestData_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::robot_tracker::VestData_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::robot_tracker::VestData_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::robot_tracker::VestData_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::robot_tracker::VestData_<ContainerAllocator> >
{
  static const char* value()
  {
    return "009a90b705b09d3266a4baee5469658e";
  }

  static const char* value(const ::robot_tracker::VestData_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x009a90b705b09d32ULL;
  static const uint64_t static_value2 = 0x66a4baee5469658eULL;
};

template<class ContainerAllocator>
struct DataType< ::robot_tracker::VestData_<ContainerAllocator> >
{
  static const char* value()
  {
    return "robot_tracker/VestData";
  }

  static const char* value(const ::robot_tracker::VestData_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::robot_tracker::VestData_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float32 x_center\n\
float32 y_center\n\
float32 area\n\
float32 rotation_angle\n\
float32 cam_height\n\
float32 cam_width\n\
";
  }

  static const char* value(const ::robot_tracker::VestData_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::robot_tracker::VestData_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.x_center);
      stream.next(m.y_center);
      stream.next(m.area);
      stream.next(m.rotation_angle);
      stream.next(m.cam_height);
      stream.next(m.cam_width);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct VestData_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::robot_tracker::VestData_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::robot_tracker::VestData_<ContainerAllocator>& v)
  {
    s << indent << "x_center: ";
    Printer<float>::stream(s, indent + "  ", v.x_center);
    s << indent << "y_center: ";
    Printer<float>::stream(s, indent + "  ", v.y_center);
    s << indent << "area: ";
    Printer<float>::stream(s, indent + "  ", v.area);
    s << indent << "rotation_angle: ";
    Printer<float>::stream(s, indent + "  ", v.rotation_angle);
    s << indent << "cam_height: ";
    Printer<float>::stream(s, indent + "  ", v.cam_height);
    s << indent << "cam_width: ";
    Printer<float>::stream(s, indent + "  ", v.cam_width);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ROBOT_TRACKER_MESSAGE_VESTDATA_H
