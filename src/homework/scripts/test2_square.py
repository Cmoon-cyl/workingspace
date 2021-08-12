#! /usr/bin/env python3
# coding:utf-8
#通过odom信息走正方形
import rospy
import math
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

class CallBack:
	def __init__(self):
		self.sub = rospy.Subscriber('/odom',Odometry,self.callback)
		self.pub = rospy.Publisher('/cmd_vel',Twist,queue_size=10)
		self.rate = rospy.Rate(10)

	def callback(self,msg):
		w = msg.pose.pose.orientation.w			#怎么获得的位置信息
		z = msg.pose.pose.orientation.z
		self.x = msg.pose.pose.position.x
		self.y = msg.pose.pose.position.y
		theta = math.atan2(2*w*z,1-2*z**2)/math.pi*180			#怎么进行的角度转换，自己思考
		if(theta<0):
			self.theta = theta + 360
		else:
			self.theta = theta
		#print(self.theta)

	def turn90(self):		#想想怎么写一个能进行指定角度旋转的函数
		vel = Twist()
		start_angle = self.theta
		#print(self.theta-start_angle)
		changed_angle = self.theta - start_angle +360 if (self.theta<270 and  start_angle>=270) else self.theta - start_angle
		while(changed_angle<=90):
			if(changed_angle<80):
				vel.angular.z = 0.5
				self.pub.publish(vel)
			else:
				vel.angular.z = 0.1
				self.pub.publish(vel)
			#print(self.theta - start_angle)
			self.rate.sleep()
			changed_angle = self.theta - start_angle +360 if (self.theta<270 and  start_angle>=270) else self.theta - start_angle
		self.pub.publish(Twist())

	def get_distance(self,x,y):
		distance = ((self.x-x)**2+(self.y-y)**2)**0.5
		return distance

	def goline(self):
		vel = Twist()
		start_x = self.x
		start_y = self.y
		while(self.get_distance(start_x,start_y)<1):
			if(self.get_distance(start_x,start_y)<0.8):
				vel.linear.x = 0.5
				self.pub.publish(vel)
			else:
				vel.linear.x = 0.1
				self.pub.publish(vel)
			self.rate.sleep()
			#print('distance:'+str(self.get_distance(start_x,start_y)))
		self.pub.publish(Twist())




if __name__ == '__main__':
	rospy.init_node('test',anonymous=True)
	a = CallBack()
	rospy.sleep(1)
	for i in range(4):
		a.goline()
		a.turn90()