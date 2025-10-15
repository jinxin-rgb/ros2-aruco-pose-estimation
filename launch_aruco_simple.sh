#!/bin/bash

# Simple ArUco detection launch script for D405
# This script launches only the essential components to avoid conflicts

echo "🚀 Starting ArUco Detection System for D405..."

# Source the workspace
source /home/neel/ros2_ws/install/setup.bash

# Wait for camera to be fully released
sleep 2

# Launch the system without RViz to avoid conflicts
ros2 launch aruco_pose_estimation aruco_pose_estimation_d405_fixed.launch.py

echo "✅ ArUco Detection System started!"
