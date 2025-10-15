#!/bin/bash

# Launch RViz separately for ArUco visualization
# Use this after the main ArUco system is running

echo "🎨 Starting RViz for ArUco visualization..."

# Source the workspace
source /home/neel/ros2_ws/install/setup.bash

# Launch RViz with the D405 configuration
rviz2 -d /home/neel/ros2_ws/src/ros2-aruco-pose-estimation/aruco_pose_estimation/rviz/cam_detect_d405.rviz

echo "✅ RViz started for ArUco visualization!"
