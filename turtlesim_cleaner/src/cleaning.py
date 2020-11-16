#!/usr/bin/env python
#!/usr/bin/env python
import rospy
from geometry_msgs.msg  import Twist
from turtlesim.msg import Pose
from math import pow,atan2,sqrt
PI = 3.1415926535897

class turtlebot():
	#gotogoal methods:#######################################
    def __init__(self):
        rospy.init_node('turtlebot_controller', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.callback)
        self.pose = Pose()
        self.rate = rospy.Rate(10)
    def callback(self, data):
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)
    def get_distance(self, goal_x, goal_y):
        distance = sqrt(pow((goal_x - self.pose.x), 2) + pow((goal_y - self.pose.y), 2))
        return distance
    def move2goal(self,distance_tolerance):
    	print('**GO TO GOAAAAAL**')
        goal_pose = Pose()
        goal_pose.x=1
        goal_pose.y=1
        vel_msg = Twist()
        while sqrt(pow((goal_pose.x - self.pose.x), 2) + pow((goal_pose.y - self.pose.y), 2)) >= distance_tolerance:
            vel_msg.linear.x = 1.5 * sqrt(pow((goal_pose.x - self.pose.x), 2) + pow((goal_pose.y - self.pose.y), 2))
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 4 * (atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x) - self.pose.theta)
            self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()
        vel_msg.linear.x = 0
        vel_msg.angular.z =0
        self.velocity_publisher.publish(vel_msg)
        #############################################################

    def rotate(self,v,angle,isPositivedirection):
        velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        vel_msg = Twist()
        print("**ROTATE**")
        angular_speed = v*2*PI/360
        relative_angle = angle*2*PI/360
        vel_msg.linear.x=0
        vel_msg.linear.y=0
        vel_msg.linear.z=0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        if (isPositivedirection==1):
            vel_msg.angular.z = abs(angular_speed)
        else:
            vel_msg.angular.z = -abs(angular_speed)
        t0 = rospy.Time.now().to_sec()
        current_angle = 0
        while(current_angle < relative_angle):
            velocity_publisher.publish(vel_msg)
            t1 = rospy.Time.now().to_sec()
            current_angle = angular_speed*(t1-t0)
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)


    def move(self,v,d,isForward):
        velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        vel_msg = Twist()
        print("**FORWARD**")
        if(isForward==1):
            vel_msg.linear.x = v
        else:
            vel_msg.linear.x = -v 
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0
        t0 = float(rospy.Time.now().to_sec())
        my_current_position = 0
        while(my_current_position < d):
            velocity_publisher.publish(vel_msg)
            t1=float(rospy.Time.now().to_sec())
            my_current_position= v*(t1-t0)

        vel_msg.linear.x = 0
        velocity_publisher.publish(vel_msg)
       

##########################################################
if __name__ == '__main__':
    try:
        x = turtlebot()
        x.move2goal(0.1)
        x.rotate(100,90,0)
        x.move(3,9,1)

        x.rotate(100,90,0)
        x.move(2,1.5,1)
        x.rotate(100,90,0)
        x.move(3,9,1)

        x.rotate(100,90,1)
        x.move(2,1.5,1)
        x.rotate(100,90,1)
        x.move(3,9,1)

        x.rotate(100,90,0)
        x.move(2,1.5,1)
        x.rotate(100,90,0)
        x.move(3,9,1)

        x.rotate(100,90,1)
        x.move(2,1.5,1)
        x.rotate(100,90,1)
        x.move(3,9,1)

        x.rotate(100,90,0)
        x.move(2,1.5,1)
        x.rotate(100,90,0)
        x.move(3,9,1)
        x.rotate(100,180,0)

    except rospy.ROSInterruptException: pass
