#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseArray, Pose
from aruco_interfaces.msg import ArucoMarkers
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

class ArucoTestNode(Node):
    def __init__(self):
        super().__init__('aruco_test_node')
        
        # Create subscribers
        self.pose_array_sub = self.create_subscription(
            PoseArray,
            '/aruco/poses',
            self.pose_array_callback,
            10
        )
        
        self.markers_sub = self.create_subscription(
            ArucoMarkers,
            '/aruco/markers',
            self.markers_callback,
            10
        )
        
        self.image_sub = self.create_subscription(
            Image,
            '/aruco/image',
            self.image_callback,
            10
        )
        
        self.bridge = CvBridge()
        
        self.get_logger().info('ArUco Test Node started. Waiting for detections...')

    def pose_array_callback(self, msg):
        self.get_logger().info(f'Detected {len(msg.poses)} ArUco markers')
        for i, pose in enumerate(msg.poses):
            self.get_logger().info(f'Marker {i+1}: Position: [{pose.position.x:.3f}, {pose.position.y:.3f}, {pose.position.z:.3f}]')

    def markers_callback(self, msg):
        self.get_logger().info(f'Marker IDs detected: {list(msg.marker_ids)}')
        for i, marker_id in enumerate(msg.marker_ids):
            pose = msg.poses[i]
            self.get_logger().info(f'Marker ID {marker_id}: Position: [{pose.position.x:.3f}, {pose.position.y:.3f}, {pose.position.z:.3f}]')

    def image_callback(self, msg):
        try:
            # Convert ROS image to OpenCV format
            cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
            
            # Display the image
            cv2.imshow('ArUco Detection', cv_image)
            cv2.waitKey(1)
            
        except Exception as e:
            self.get_logger().error(f'Error processing image: {str(e)}')

def main(args=None):
    rclpy.init(args=args)
    
    node = ArucoTestNode()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        cv2.destroyAllWindows()
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
