#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist, Point, Quaternion
import tf
import tf2_ros
import sys
from geometry_msgs.msg import PoseStamped 
from move_base_msgs.msg import MoveBaseActionResult 
from math import radians, copysign, sqrt, pow, pi
import PyKDL
def quat_to_angle(quat):
        rot = PyKDL.Rotation.Quaternion(quat.x, quat.y, quat.z, quat.w)
        return rot.GetRPY()[2]

class OutAndBack():
    def __init__(self):
        # Give the node a name
        rospy.init_node('out_and_back', anonymous=False)

        # Set rospy to execute a shutdown function when exiting       
        rospy.on_shutdown(self.shutdown)

        # Publisher to control the robot's speed
        self.cmd_vel = rospy.Publisher('/cmd_vel', Twist, queue_size=5)
        
        # How fast will we update the robot's movement?
        self.rate = 20
        
        # Set the equivalent ROS rate variable
        self.r = rospy.Rate(self.rate)
        
        # Set the forward linear speed to 0.15 meters per second 
        self.linear_speed = 0.15
        
        # Set the travel distance in meters
        self.goal_distance = 1.0

        # Set the rotation speed in radians per second
        self.angular_speed = 0.5
        
        # Set the angular tolerance in degrees converted to radians
        self.angular_tolerance = radians(1.0)
        
        # Set the rotation angle to Pi radians (180 degrees)
        self.goal_angle = -pi/5    #the angle the robot will turn when self.turn()

        # Initialize the tf listener
        self.tf_listener = tf.TransformListener()
        
        # Give tf some time to fill its buffer
        rospy.sleep(2)
        
        # Set the odom frame
        self.odom_frame = '/odom'
        
        ####
        
        self.gpsr_pub = rospy.Publisher('move_base_simple/goal', PoseStamped, queue_size=5)
	self.exit_point=PoseStamped()
	rospy.Subscriber('/move_base/result', MoveBaseActionResult, self.base_status_callback)
	self.base_status = MoveBaseActionResult()
	
        # Find out if the robot uses /base_link or /base_footprint
        try:
            self.tf_listener.waitForTransform(self.odom_frame, '/base_footprint', rospy.Time(), rospy.Duration(1.0))
            self.base_frame = '/base_footprint'
        except (tf.Exception, tf.ConnectivityException, tf.LookupException):
            try:
                self.tf_listener.waitForTransform(self.odom_frame, '/base_link', rospy.Time(), rospy.Duration(1.0))
                self.base_frame = '/base_link'
            except (tf.Exception, tf.ConnectivityException, tf.LookupException):
                rospy.loginfo("Cannot find transform between /odom and /base_link or /base_footprint")
                rospy.signal_shutdown("tf Exception")  
        
        # Initialize the position variable as a Point type
        self.position = Point()
        rospy.sleep(5)
        self.getindoor(1.5)#go straight for 1m
        #self.turn() 
        #self.getindoor(1)
        
        self.exit_point.header.stamp = rospy.Time.now()
	self.exit_point.header.frame_id = 'map'
	 #self.q = tf.transformations.quaternion_from_euler(0,0,1.15)
	 
	self.exit_point.pose.position.x = 7
        self.exit_point.pose.position.y = -4.65		
	self.exit_point.pose.position.z = 0
	self.exit_point.pose.orientation.x= 0
	self.exit_point.pose.orientation.y = 0
	self.exit_point.pose.orientation.z = 0.714402109852
	self.exit_point.pose.orientation.w = 0.699735396732	    		
	rospy.sleep(2)	    	
	#self.gpsr_pub.publish(self.exit_point)	  
	  	
	
	   	            
    def getindoor(self,goal):    
        # Loop once for each leg of the trip
        for i in range(1):
            # Initialize the movement command
            self.move_cmd = Twist()
            
            # Set the movement command to forward motion
            self.move_cmd.linear.x = self.linear_speed
            
            # Get the starting position values     
            (self.position, self.rotation) = self.get_odom()
                        
            self.x_start = self.position.x
            self.y_start = self.position.y
            
            # Keep track of the distance traveled
            self.distance = 0
            self.goal_distance = goal
            # Enter the loop to move along a side
            while self.distance < self.goal_distance and not rospy.is_shutdown():
                # Publish the Twist message and sleep 1 cycle         
                self.cmd_vel.publish(self.move_cmd)
                
                self.r.sleep()
        
                # Get the current position
                (self.position, self.rotation) = self.get_odom()
                
                # Compute the Euclidean distance from the start
                self.distance = sqrt(pow((self.position.x - self.x_start), 2) + 
                                pow((self.position.y - self.y_start), 2))

            # Stop the robot before the rotation
            self.cmd_vel.publish(Twist())
            rospy.sleep(1)
            
    def turn(self):
            # Set the movement command to a rotation
            self.move_cmd = Twist()
            self.move_cmd.angular.z = self.angular_speed
            
            # Track the last angle measured
            self.last_angle = self.rotation
            
            # Track how far we have turned
            self.turn_angle = 0
            
            while abs(self.turn_angle + self.angular_tolerance) < abs(self.goal_angle) and not rospy.is_shutdown():
                # Publish the Twist message and sleep 1 cycle         
                self.cmd_vel.publish(self.move_cmd)
                self.r.sleep()
                
                # Get the current rotation
                (self.position, self.rotation) = self.get_odom()
                
                # Compute the amount of rotation since the last loop
                self.delta_angle = self.normalize_angle(self.rotation - self.last_angle)
                
                # Add to the running total
                self.turn_angle += self.delta_angle
                self.last_angle = self.rotation
                
            # Stop the robot before the next leg
            self.cmd_vel.publish(Twist())
            rospy.sleep(1)
        
    def get_odom(self):
        # Get the current transform between the odom and base frames
        try:
            (trans, rot)  = self.tf_listener.lookupTransform(self.odom_frame, self.base_frame, rospy.Time(0))
        except (tf.Exception, tf.ConnectivityException, tf.LookupException):
            rospy.loginfo("TF Exception")
            return

        return (Point(*trans), quat_to_angle(Quaternion(*rot)))
        
    def shutdown(self):
        # Always stop the robot when shutting down the node.
        rospy.loginfo("Stopping the robot...")
        self.cmd_vel.publish(Twist())
        rospy.sleep(1)
              
    def normalize_angle(self,angle):
        res = angle
        while res > pi:
            res -= 2.0 * pi
        while res < -pi:
            res += 2.0 * pi
        return res
        
    def base_status_callback(self, msg):
    	self.base_status = msg.status.status
 
if __name__ == '__main__':
    try:
        OutAndBack()
        #rospy.spin()
    except:
        rospy.loginfo("Out-and-Back node terminated.")

