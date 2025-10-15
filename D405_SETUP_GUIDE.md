# ArUco Pose Detection Setup for Intel RealSense D405 Camera

This guide will help you set up ArUco marker detection and pose estimation using your Intel RealSense D405 camera with ROS2.

## Prerequisites

1. **ROS2 Humble or Iron** installed
2. **Intel RealSense SDK** and **realsense-ros** package installed
3. **ArUco markers** printed (recommended size: 10cm x 10cm for 0.1m marker_size)

## Installation Steps

### 1. Install Dependencies

```bash
# Install Python dependencies
pip3 install opencv-python opencv-contrib-python transforms3d

# Install ROS2 dependencies (if not already installed)
sudo apt install ros-iron-realsense2-camera
```

### 2. Build the Workspace

```bash
cd /home/neel/ros2_ws
colcon build --packages-select aruco_interfaces aruco_pose_estimation --symlink-install
source install/setup.bash
```

## Usage Instructions

### 1. Start the ArUco Detection System

**Option A: With Depth (Recommended for D405)**
```bash
ros2 launch aruco_pose_estimation aruco_pose_estimation_d405.launch.py
```

**Option B: RGB Only**
```bash
ros2 launch aruco_pose_estimation aruco_pose_estimation_d405.launch.py use_depth_input:=false
```

**Option C: Custom Parameters**
```bash
ros2 launch aruco_pose_estimation aruco_pose_estimation_d405.launch.py \
    marker_size:=0.1 \
    aruco_dictionary_id:=DICT_4X4_50 \
    use_depth_input:=true
```

### 2. Monitor Detection Results

**View detected poses:**
```bash
ros2 topic echo /aruco/poses
```

**View marker IDs and poses:**
```bash
ros2 topic echo /aruco/markers
```

**View output image with detections:**
```bash
ros2 run rqt_image_view rqt_image_view /aruco/image
```

### 3. Test with Custom Script

```bash
python3 /home/neel/ros2_ws/src/ros2-aruco-pose-estimation/test_aruco_detection.py
```

## Configuration Parameters

Edit `/home/neel/ros2_ws/src/ros2-aruco-pose-estimation/aruco_pose_estimation/config/aruco_parameters_d405.yaml`:

- `marker_size`: Physical size of your ArUco markers in meters
- `aruco_dictionary_id`: Dictionary type (DICT_4X4_50, DICT_5X5_250, etc.)
- `use_depth_input`: Enable/disable depth-based pose estimation

## Topic Information

### Subscribed Topics:
- `/camera/color/image_raw`: RGB image from D405
- `/camera/aligned_depth_to_color/image_raw`: Depth image (if enabled)
- `/camera/color/camera_info`: Camera calibration parameters

### Published Topics:
- `/aruco/poses`: PoseArray with detected marker poses
- `/aruco/markers`: ArucoMarkers with IDs and poses
- `/aruco/image`: Output image with detected markers visualized

## Troubleshooting

### 1. Camera Not Detected
```bash
# Check if camera is connected
rs-enumerate-devices

# Check ROS2 topics
ros2 topic list | grep camera
```

### 2. No Markers Detected
- Ensure ArUco markers are printed clearly
- Check marker size parameter matches physical size
- Verify dictionary ID matches your markers
- Ensure good lighting conditions

### 3. Poor Pose Estimation
- Calibrate your camera for better intrinsic parameters
- Use depth input for more accurate 3D pose estimation
- Ensure markers are not too close or too far from camera

## Creating ArUco Markers

You can generate ArUco markers using OpenCV:

```python
import cv2
import numpy as np

# Generate a marker
dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
marker_id = 0
marker_size = 200  # pixels

marker = cv2.aruco.generateImageMarker(dictionary, marker_id, marker_size)
cv2.imwrite(f'aruco_marker_{marker_id}.png', marker)
```

## Advanced Usage

### Custom Frame Configuration
If you need to transform poses to a different frame:

```bash
ros2 run tf2_ros static_transform_publisher 0 0 0 0 0 0 base_link camera_color_optical_frame
```

### Recording Data
```bash
ros2 bag record /aruco/poses /aruco/markers /aruco/image
```

This setup should work perfectly with your D405 camera for ArUco marker detection and pose estimation!
