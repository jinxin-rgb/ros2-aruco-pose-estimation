#!/bin/bash

# Launch RViz for ArUco detection with D405 camera
# This script can be used to launch RViz separately from the main detection system

echo "Launching RViz for ArUco detection with D405 camera..."

# Source the workspace
source /home/neel/ros2_ws/install/setup.bash

# Launch RViz with the D405 configuration
rviz2 -d /home/neel/ros2_ws/src/ros2-aruco-pose-estimation/aruco_pose_estimation/rviz/cam_detect_d405.rviz
