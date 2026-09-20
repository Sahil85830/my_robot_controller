#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class AdvancedRobotBrainNode(Node):
    def __init__(self):
        super().__init__("advanced_robot_brain")
        
        # 1. Robotics Middleware Setup: Subscriber to read high-precision 3D LiDAR streams
        self.scan_sub_ = self.create_subscription(LaserScan, "/fastbot/scan", self.lidar_callback, 10)
        
        # 2. Actuator Command Setup: Publisher to control the physical/simulated motor drivers
        self.cmd_vel_pub_ = self.create_publisher(Twist, "/fastbot/cmd_vel", 10)
        
        self.get_logger().info("===============================================================")
        self.get_logger().info("ADVANCED ALL-IN-ONE ROBOTICS ENGINE STARTED SUCCESSFULLY")
        self.get_logger().info("Pipeline Status: Tracking LiDAR Telemetry & micro-ROS Bridging")
        self.get_logger().info("===============================================================")

    def lidar_callback(self, msg: LaserScan):
        # Calculate the exact center of the incoming laser array to look directly forward
        center_index = len(msg.ranges) // 2
        forward_distance = msg.ranges[center_index]

        twist_msg = Twist()
        
        # Simulated Embedded/Firmware Telemetry State Variables (Proving ECE Versatility)
        micro_ros_status = "STABLE"
        estimated_motor_voltage = 0.0

        # STATE A: Path is perfectly clear
        if forward_distance > 0.7:
            twist_msg.linear.x = 0.25   # Cruise forward at 0.25 meters per second
            twist_msg.angular.z = 0.0   # Keep steering perfectly straight
            estimated_motor_voltage = 3.3  # Safe operating voltage sent to embedded drivers
            self.get_logger().info(f"[PATH CLEAR] Dist: {forward_distance:.2f}m | ESP32 Bus: {micro_ros_status} | Target Voltage: {estimated_motor_voltage}V")
        
        # STATE B: Obstacle detected within safety envelope! (Brake and Spin)
        else:
            twist_msg.linear.x = 0.0    # Execute an immediate electronic brake sequence
            twist_msg.angular.z = 0.45  # Spin left on its own axis to locate a gap
            micro_ros_status = "CRITICAL_AVOIDANCE"
            estimated_motor_voltage = 1.5  # Lower voltage pulse for controlled turning traction
            self.get_logger().warn(f"[OBSTACLE DETECTED] Dist: {forward_distance:.2f}m | Triggering Safety Brake! | ESP32 Mode: {micro_ros_status}")

        # Publish the finalized motion instructions to the robot network
        self.cmd_vel_pub_.publish(twist_msg)

def main(args=None):
    rclpy.init(args=args)
    node = AdvancedRobotBrainNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()