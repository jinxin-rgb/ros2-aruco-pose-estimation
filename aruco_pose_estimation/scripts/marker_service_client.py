#!/usr/bin/env python3
"""
Service client for ArUco marker detection service.

This script sends a one-time request to the ArUco detection service
and displays all detected marker IDs and their corresponding poses as a dictionary.

Usage:
    python3 marker_service_client.py

Author: Generated for ArUco pose estimation system
Version: 2024-10-15
"""

import rclpy
from rclpy.node import Node
from aruco_interfaces.srv import GetMarkers
import time


class MarkerServiceClient(Node):
    def __init__(self):
        super().__init__('marker_service_client')
        
        # Create service client
        self.client = self.create_client(GetMarkers, 'get_markers')
        
        # Wait for service to be available
        self.get_logger().info("Waiting for ArUco detection service...")
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("Service not available, waiting...")
        
        self.get_logger().info("Service is available!")

    def get_markers(self):
        """Send request to get markers and return the response"""
        request = GetMarkers.Request()
        
        self.get_logger().info("Sending request to get markers...")
        
        try:
            # Send the request
            future = self.client.call_async(request)
            rclpy.spin_until_future_complete(self, future)
            
            if future.result() is not None:
                response = future.result()
                return response
            else:
                self.get_logger().error("Service call failed")
                return None
                
        except Exception as e:
            self.get_logger().error(f"Exception in service call: {e}")
            return None

    def format_markers_as_dict(self, response):
        """Format the service response as a dictionary"""
        if response is None:
            return {}
        
        markers_dict = {}
        
        for i, marker_id in enumerate(response.marker_ids):
            pose = response.poses[i]
            
            markers_dict[f"marker_{marker_id}"] = {
                "id": int(marker_id),
                "position": {
                    "x": float(pose.position.x),
                    "y": float(pose.position.y),
                    "z": float(pose.position.z)
                },
                "orientation": {
                    "x": float(pose.orientation.x),
                    "y": float(pose.orientation.y),
                    "z": float(pose.orientation.z),
                    "w": float(pose.orientation.w)
                }
            }
        
        return markers_dict

    def print_markers_dict(self, markers_dict):
        """Print the markers dictionary in a formatted way"""
        if not markers_dict:
            print("No markers detected.")
            return
        
        print("\n" + "="*60)
        print("DETECTED ARUCO MARKERS")
        print("="*60)
        
        for marker_name, marker_data in markers_dict.items():
            print(f"\n{marker_name.upper()}:")
            print(f"  ID: {marker_data['id']}")
            print(f"  Position: ({marker_data['position']['x']:.4f}, "
                  f"{marker_data['position']['y']:.4f}, "
                  f"{marker_data['position']['z']:.4f})")
            print(f"  Orientation: ({marker_data['orientation']['x']:.4f}, "
                  f"{marker_data['orientation']['y']:.4f}, "
                  f"{marker_data['orientation']['z']:.4f}, "
                  f"{marker_data['orientation']['w']:.4f})")
        
        print("\n" + "="*60)
        print(f"Total markers detected: {len(markers_dict)}")
        print("="*60)


def main():
    rclpy.init()
    
    client_node = MarkerServiceClient()
    
    try:
        # Get markers from service
        response = client_node.get_markers()
        
        # Format as dictionary
        markers_dict = client_node.format_markers_as_dict(response)
        
        # Print formatted results
        client_node.print_markers_dict(markers_dict)
        
        # Also print raw dictionary for programmatic use
        print("\nRaw dictionary format:")
        print(markers_dict)
        
    except KeyboardInterrupt:
        print("\nInterrupted by user")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
