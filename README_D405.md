# ArUco Pose Detection with Intel RealSense D405 Camera

A complete ROS2 package for ArUco marker detection and 6DOF pose estimation using Intel RealSense D405 camera. This package provides real-time marker detection with both RGB and depth-based pose estimation.

## 🚀 Quick Start

### 1. Launch ArUco Detection
```bash
cd /home/neel/ros2_ws
source install/setup.bash
ros2 launch aruco_pose_estimation aruco_pose_estimation_d405.launch.py
```

### 2. Generate Test Markers
```bash
python3 /home/neel/ros2_ws/src/ros2-aruco-pose-estimation/generate_aruco_markers.py --ids 0 1 2 3 4
```

### 3. Monitor Detection
```bash
# View detected poses
ros2 topic echo /aruco/poses

# View marker IDs and poses
ros2 topic echo /aruco/markers

# View output image
ros2 run rqt_image_view rqt_image_view /aruco/image

# Launch RViz visualization (if not auto-launched)
./launch_rviz_d405.sh
```

## 📋 Prerequisites

- **ROS2 Humble/Iron** installed
- **Intel RealSense D405** camera connected
- **realsense-ros** package installed
- **OpenCV** with ArUco support

## 🛠️ Installation

### 1. Install Dependencies
```bash
# Python dependencies
pip3 install opencv-python opencv-contrib-python transforms3d

# ROS2 dependencies
sudo apt install ros-iron-realsense2-camera
```

### 2. Build Workspace
```bash
cd /home/neel/ros2_ws
colcon build --packages-select aruco_interfaces aruco_pose_estimation --symlink-install
source install/setup.bash
```

## 🎯 Usage

### Basic Launch Commands

**With Depth (Recommended):**
```bash
ros2 launch aruco_pose_estimation aruco_pose_estimation_d405.launch.py
```

**RGB Only:**
```bash
ros2 launch aruco_pose_estimation aruco_pose_estimation_d405.launch.py use_depth_input:=false
```

**Custom Parameters:**
```bash
ros2 launch aruco_pose_estimation aruco_pose_estimation_d405.launch.py \
    marker_size:=0.1 \
    aruco_dictionary_id:=DICT_4X4_50 \
    use_depth_input:=true
```

### Available Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `marker_size` | 0.1 | Physical size of markers in meters |
| `aruco_dictionary_id` | DICT_4X4_50 | ArUco dictionary type |
| `use_depth_input` | true | Enable depth-based pose estimation |
| `image_topic` | /camera/color/image_raw | RGB image topic |
| `depth_image_topic` | /camera/aligned_depth_to_color/image_raw | Depth image topic |
| `camera_info_topic` | /camera/color/camera_info | Camera calibration topic |

## 📡 Topics

### Subscribed Topics
- `/camera/color/image_raw` - RGB image from D405
- `/camera/aligned_depth_to_color/image_raw` - Depth image (if enabled)
- `/camera/color/camera_info` - Camera calibration parameters

### Published Topics
- `/aruco/poses` - `geometry_msgs/PoseArray` - Detected marker poses
- `/aruco/markers` - `aruco_interfaces/ArucoMarkers` - Marker IDs and poses
- `/aruco/image` - `sensor_msgs/Image` - Output image with visualizations

## 🔧 Configuration

### Marker Size Configuration
Edit `config/aruco_parameters_d405.yaml`:
```yaml
marker_size: 0.1  # Adjust based on your printed markers
```

### Dictionary Types
Available ArUco dictionaries:
- `DICT_4X4_50` - 4x4 markers, 50 IDs
- `DICT_4X4_100` - 4x4 markers, 100 IDs
- `DICT_5X5_250` - 5x5 markers, 250 IDs
- `DICT_6X6_250` - 6x6 markers, 250 IDs

## 🎨 Creating ArUco Markers

### Generate Markers
```bash
# Generate 5 markers (IDs 0-4) with 200px size
python3 generate_aruco_markers.py --ids 0 1 2 3 4 --size 200

# Generate markers with different dictionary
python3 generate_aruco_markers.py --dictionary DICT_5X5_250 --ids 0 1 2 --size 300
```

### Print Guidelines
- **Size**: Print markers at the size specified in `marker_size` parameter
- **Quality**: Use high-quality printing, avoid blurry edges
- **Material**: Print on flat, non-reflective surfaces
- **Lighting**: Ensure good, even lighting when using

## 🔍 Monitoring and Debugging

### RViz Visualization
The system includes a comprehensive RViz configuration that shows:

- **ArUco Markers**: 3D pose visualization with colored axes
- **Camera Feed**: Live RGB image from D405
- **Detection Image**: Processed image with detected markers highlighted
- **Point Cloud**: 3D depth data from D405 (if depth enabled)
- **TF Frames**: Camera coordinate frames
- **Grid**: Reference coordinate system

**Launch RViz:**
```bash
# Automatically launched with main system
ros2 launch aruco_pose_estimation aruco_pose_estimation_d405.launch.py

# Or launch RViz separately
./launch_rviz_d405.sh
```

### View Detection Results
```bash
# Real-time pose monitoring
ros2 topic echo /aruco/poses

# Marker ID tracking
ros2 topic echo /aruco/markers

# Visual output
ros2 run rqt_image_view rqt_image_view /aruco/image
```

### Test Script
```bash
# Run comprehensive test
python3 test_aruco_detection.py
```

### Check Camera Status
```bash
# List available cameras
rs-enumerate-devices

# Check ROS2 topics
ros2 topic list | grep camera
```

## 🐛 Troubleshooting

### Camera Issues
```bash
# Check camera connection
rs-enumerate-devices

# Verify topics are publishing
ros2 topic hz /camera/color/image_raw
```

### No Markers Detected
1. **Check marker size** - Ensure `marker_size` matches physical size
2. **Verify dictionary** - Use correct `aruco_dictionary_id`
3. **Improve lighting** - Ensure even, bright lighting
4. **Check distance** - Markers should be 0.3-2m from camera
5. **Print quality** - Use high-resolution printing

### Poor Pose Estimation
1. **Enable depth** - Set `use_depth_input:=true`
2. **Calibrate camera** - Ensure accurate intrinsic parameters
3. **Check marker size** - Verify physical dimensions
4. **Improve lighting** - Avoid shadows and reflections

### Performance Issues
1. **Reduce resolution** - Lower camera resolution in launch file
2. **Limit markers** - Use fewer markers simultaneously
3. **Optimize lighting** - Ensure consistent lighting conditions

## 📊 Advanced Usage

### Custom Frame Transformations
```bash
# Add static transform if needed
ros2 run tf2_ros static_transform_publisher 0 0 0 0 0 0 base_link camera_color_optical_frame
```

### Recording Data
```bash
# Record detection data
ros2 bag record /aruco/poses /aruco/markers /aruco/image
```

### Integration with Robot
```python
# Example: Subscribe to poses in your robot code
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseArray

class RobotController(Node):
    def __init__(self):
        super().__init__('robot_controller')
        self.pose_sub = self.create_subscription(
            PoseArray, '/aruco/poses', self.pose_callback, 10)
    
    def pose_callback(self, msg):
        for i, pose in enumerate(msg.poses):
            self.get_logger().info(f'Marker {i}: {pose.position.x}, {pose.position.y}, {pose.position.z}')
```

## 📁 File Structure

```
ros2-aruco-pose-estimation/
├── aruco_interfaces/           # Message definitions
├── aruco_pose_estimation/      # Main detection package
│   ├── config/
│   │   ├── aruco_parameters.yaml
│   │   └── aruco_parameters_d405.yaml  # D405-specific config
│   ├── launch/
│   │   ├── aruco_pose_estimation.launch.py
│   │   └── aruco_pose_estimation_d405.launch.py  # D405 launch
│   └── aruco_pose_estimation/
│       └── aruco_node.py      # Main detection node
├── generate_aruco_markers.py   # Marker generator
├── test_aruco_detection.py     # Test script
└── README_D405.md             # This file
```

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## 📄 License

This project is based on the [ros2-aruco-pose-estimation](https://github.com/AIRLab-POLIMI/ros2-aruco-pose-estimation) package by AIRLab-POLIMI.

## 🆘 Support

For issues specific to this D405 setup:
1. Check the troubleshooting section above
2. Verify camera connection and topics
3. Ensure marker size and dictionary match your setup
4. Check lighting and marker quality

---

**Happy ArUco Detection! 🎯**
