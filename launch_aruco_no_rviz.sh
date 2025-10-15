#!/bin/bash

# Launch ArUco detection without RViz to avoid camera conflicts
# This script launches only the essential components

echo "🚀 Starting ArUco Detection System (without RViz)..."

# Source the workspace
source /home/neel/ros2_ws/install/setup.bash

# Wait for camera to be fully released
sleep 2

# Launch the system without RViz
ros2 launch aruco_pose_estimation aruco_pose_estimation_d405.launch.py use_rviz:=false

echo "✅ ArUco Detection System started (without RViz)!"
