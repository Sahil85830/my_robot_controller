#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class DrawCircleNode(Node):
    def __init__(self):
        super().__init__("draw_circle")
        # Create a publisher that sends speed instructions to Fastbot's control topic
        self.cmd_vel_pub_ = self.create_publisher(Twist, "/fastbot/cmd_vel", 10)
        # Create a repeating timer loop running at 10Hz (every 0.1 seconds)
        self.timer_ = self.create_timer(0.1, self.send_velocity_command)
        self.get_logger().info("Autonomous Draw Circle Node has been initialized!")

    def send_velocity_command(self):
        msg = Twist()
        msg.linear.x = 0.3   # Move forward at 0.3 meters per second
        msg.angular.z = 0.5  # Spin left at 0.5 radians per second
        self.cmd_vel_pub_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = DrawCircleNode()
    rclpy.spin(node) # Keeps the script running continuously
    rclpy.shutdown()

if __name__ == "__main__":
    main()
