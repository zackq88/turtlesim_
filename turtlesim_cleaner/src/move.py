#!/usr/bin/env python   
#do not remove the first commented line.
import rospy
from geometry_msgs.msg import Twist

def move():
    # Starts a new node
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    #inputs
    print("You wanna move ! ")
    v = input("how fast:")
    d = input("how far:")
    isForward = input("if forward => 1 /if backward => 0 :")
    #Checking forward/backward
    if(isForward==1):
        vel_msg.linear.x = v
    else:
        vel_msg.linear.x = -v
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0
    
    while not rospy.is_shutdown():
        t0 = float(rospy.Time.now().to_sec())
        my_current_position = 0
        #Loop to move the turtle until we arrived the desired postion
        while(my_current_position < d):
            #Publish the velocity ( give vel_msg to the turtle)
            velocity_publisher.publish(vel_msg)
            t1=float(rospy.Time.now().to_sec())
            my_current_position= v*(t1-t0)
        #we have arrived
        vel_msg.linear.x = 0
        velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException: pass
