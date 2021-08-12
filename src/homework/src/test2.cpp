#include <geometry_msgs/Twist.h>
#include <ros/ros.h>
#define PI 3.14159265358979323846

int main(int argc, char **argv) {
  ros::init(argc, argv, "draw_rectangle"); //"draw_rectangle"必须是nodename
  std::string topic = "/turtle1/cmd_vel";  // topic name
  ros::NodeHandle n;
  ros::Publisher cmdVelPub = n.advertise<geometry_msgs::Twist>(topic, 1);
  //第一个参数也可以写成"/turtle1/cmd_vel"这样的topic name
  //第二个参数是发布的缓冲区大小,<geometry_msgs::Twist>是消息类型
  ros::Rate loopRate(62);
  //与Rate::sleep();配合指定自循环频率
  ROS_INFO("draw_retangle start..."); //输出显示信息
  geometry_msgs::Twist speed;         // 控制信号载体 Twist message
  //声明一个geometry_msgs::Twist 类型的对象speed，并将速度的值赋值到这个对象里面
  int count = 0;
  while (ros::ok()) {
    speed.linear.x = 1; // 设置线速度为1m/s，正为前进，负为后退
    speed.linear.y = 0;
    speed.linear.z = 0;
    speed.angular.x = 0;
    speed.angular.y = 0;
    speed.angular.z = 0;
    count++;
    while (count == 5) {
      count = 0;
      speed.angular.z = 3.1415926; //转90°
    }
    cmdVelPub.publish(speed); // 将刚才设置的指令发送给机器人
    ros::spinOnce();          //调用此函数给其他回调函数得以执行
    loopRate.sleep();         //按loopRate(2)设置的2HZ将程序挂起
  }

  return 0;
}