#!/usr/bin/env python
#!/usr/bin/env python
import rospy
#msg that i need
from geometry_msgs.msg  import Twist
from turtlesim.msg import Pose

from math import pow,atan2,sqrt



class turtlebot():
    def __init__(self):
        #Creating our node,publisher and subscriber
        rospy.init_node('turtlebot_controller', anonymous=True)
        #publisher to the topic turtle1/cmd_vel - msgtype:Twist[linear x,y,z , angular x,y,z velocities]
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        #subscriber to the topic turtle1/pose - msgtype:Pose[x,y,angle,linear velocity,angular velocity]   
        #self.update_pose=  self.callback is called when a message of type Pose is received
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.callback)

        self.pose = Pose()
        self.rate = rospy.Rate(10)




    #Methods:
    #Callback function implementing the pose value received
    def callback(self, data):
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)

    def get_distance(self, goal_x, goal_y):
        distance = sqrt(pow((goal_x - self.pose.x), 2) + pow((goal_y - self.pose.y), 2))
        return distance



    
    #main method:
    def move2goal(self):

        goal_pose = Pose()
        vel_msg = Twist()
        #inputs
        goal_pose.x = input("Set your x goal:")
        goal_pose.y = input("Set your y goal:")
        distance_tolerance = input("Set your tolerance:")
        


        while sqrt(pow((goal_pose.x - self.pose.x), 2) + pow((goal_pose.y - self.pose.y), 2)) >= distance_tolerance:
            #Porportional Controller-->1.5
            #linear velocity in the x-axis:
            vel_msg.linear.x = 1.5 * sqrt(pow((goal_pose.x - self.pose.x), 2) + pow((goal_pose.y - self.pose.y), 2))
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            #angular velocity in the z-axis:
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 4 * (atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x) - self.pose.theta)

            self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()

        #Stopping our robot after the movement is over
        vel_msg.linear.x = 0
        vel_msg.angular.z =0
        self.velocity_publisher.publish(vel_msg)

        rospy.spin()

if __name__ == '__main__':
    try:
        x = turtlebot()
        x.move2goal()
    except rospy.ROSInterruptException: pass















'''
#!/usr/bin/env python
#!/usr/bin/env python
import rospy
#msg that I need : Twist , Pose
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt

class TurtleBot:
	def __init__(self):
		#create a node which is Publisher and Subscriber 
		rospy.init_node('turtlebot_controller', anonymous=True)
		# Publisher which will publish to the topic '/turtle1/cmd_vel'
		self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)
		# A subscriber to the topic '/turtle1/pose'; self.update_pose is called when a message of type Pose is received
		self.pose_subscriber = rospy.Subscriber('/turtle1/pose',Pose, self.update_pose)

		self.pose = Pose()
		self.rate = rospy.Rate(10)


		#methods:
	def update_pose(self, data): 
        #Callback function which is called when a new message of type Pose is received by the subscriber
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)
   
    def euclidean_distance(self, goal_pose):
        #Euclidean distance between current pose and the goal
        return sqrt(pow((goal_pose.x - self.pose.x), 2) + pow((goal_pose.y - self.pose.y), 2))
   
    def linear_vel(self, goal_pose, constant=1.5):
        return constant * self.euclidean_distance(goal_pose)

    def steering_angle(self, goal_pose):
        return atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x)
   
    def angular_vel(self, goal_pose, constant=6):
        return constant * (self.steering_angle(goal_pose) - self.pose.theta)


    #main method:
    def move2goal(self):
    	#Moves the turtle to the goal
    	goal_pose = Pose()
    	vel_msg = Twist()

    	#input
    	goal_pose.x = input("Set your x goal: ")
    	goal_pose.y = input("Set your y goal: ")
    	# Please, insert a number slightly greater than 0 (e.g. 0.01)
    	distance_tolerance = input("Set your tolerance: ")


    	while self.euclidean_distance(goal_pose) >= distance_tolerance:
    		vel_msg.linear.x=self.linear_vel(goal_pose)
    		vel_msg.linear.y=0
    		vel_msg.linear.z=0
    		vel_msg.angular.x=0
    		vel_msg.angular.y=0
    		vel_msg.angular.z=self.angular_vel(goal_pose)

    		self.velocity_publisher.publish(vel_msg)

    		# Publish at the desired rate.
            self.rate.sleep()
        	
        # Stopping our robot after the movement is over.
        vel_msg.linear.x=0
        vel_msg.angular.z=0
        self.velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    try: 
        x = TurtleBot()
        x.move2goal()
    except rospy.ROSInterruptException:
    	pass
'''     















                                                 
