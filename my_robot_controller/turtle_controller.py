#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


class TurtleControllerNode(Node):
    def __init__(self):
        super().__init__('turtle_controller') #node name

        self.cmd_val_publisher = self.create_publisher(
            Twist,"/turtle1/cmd_vel",10) 
          
        self.pose_subscriber = self.create_subscription(
            Pose,"/turtle1/pose",self.pose_callback,10)
 
        self.get_logger().info('Turtle COntroller Node has been started.')
        
    def pose_callback(self, pose:Pose):
        cmd =Twist()

        if pose.x >=9.0  or pose.x <2 or pose.y >9.0 or pose.y <2:
            cmd.linear.x = 1.0;
            cmd.linear.y = 1.0;
            cmd.angular.z = 0.9;
        else:
            cmd.linear.x = 5.0
            cmd.angular.z = 0.0
        self.cmd_val_publisher.publish(cmd)




        # def send_velocity(self):
        #     msg =Twist()
        #     msg.linear.x = 2.0
        #     msg.angular.z = 1.0
        #     self.cmd_vel_pub.publish(msg)



def main(args=None):

    rclpy.init(args=args)
    node = TurtleControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()    