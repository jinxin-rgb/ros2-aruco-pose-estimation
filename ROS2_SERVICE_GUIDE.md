# ArUco Marker Detection Service - ROS2 Guide

This guide shows how to use the ArUco marker detection service with the standard `ros2 run` commands.

## 🚀 Quick Start

### 1. Start the ArUco Detection System
```bash
# Terminal 1: Launch the detection system
ros2 launch aruco_pose_estimation aruco_pose_estimation_d405.launch.py
```

### 2. Use the Service Client
```bash
# Terminal 2: Use the service client
ros2 run aruco_pose_estimation marker_service_client.py
```

## 📋 Service Details

### Service Name
- **Service**: `/get_markers`
- **Type**: `aruco_interfaces/srv/GetMarkers`

### Service Request
- **Empty request** - just triggers marker detection

### Service Response
```yaml
std_msgs/Header header
int64[] marker_ids          # Array of detected marker IDs
geometry_msgs/Pose[] poses  # Array of corresponding poses
string[] marker_info        # Additional info like "marker_0", "marker_1"
```

## 🔧 Available Commands

### Check Available Executables
```bash
ros2 pkg executables aruco_pose_estimation
```

### Test the Service
```bash
ros2 run aruco_pose_estimation test_marker_service.py
```

### Use the Service Client
```bash
ros2 run aruco_pose_estimation marker_service_client.py
```

### Check Service Status
```bash
# Check if service is available
ros2 service list | grep get_markers

# Get service info
ros2 service info /get_markers

# Test service directly
ros2 service call /get_markers aruco_interfaces/srv/GetMarkers
```

## 📊 Output Format

The service returns a dictionary with the following structure:

```python
{
    "marker_0": {
        "id": 0,
        "position": {
            "x": 0.1234,
            "y": 0.5678,
            "z": 0.9012
        },
        "orientation": {
            "x": 0.0,
            "y": 0.0,
            "z": 0.0,
            "w": 1.0
        }
    },
    "marker_1": {
        "id": 1,
        "position": {
            "x": -0.1234,
            "y": 0.5678,
            "z": 0.9012
        },
        "orientation": {
            "x": 0.0,
            "y": 0.0,
            "z": 0.7071,
            "w": 0.7071
        }
    }
}
```

## 🔍 Troubleshooting

### Service Not Available
```bash
# Check if ArUco node is running
ros2 node list | grep aruco

# Check service list
ros2 service list | grep get_markers

# Check node info
ros2 node info /aruco_node
```

### No Markers Detected
1. **Check camera connection**: Ensure D405 camera is connected
2. **Verify topics**: `ros2 topic list | grep camera`
3. **Check marker visibility**: Ensure markers are in camera view
4. **Verify marker size**: Check `marker_size` parameter matches physical size
5. **Check lighting**: Ensure adequate lighting for detection

### Service Call Fails
```bash
# Check service status
ros2 service info /get_markers

# Test with ros2 service call
ros2 service call /get_markers aruco_interfaces/srv/GetMarkers

# Check for errors in ArUco node
ros2 topic echo /rosout
```

## 🔄 Integration Examples

### Robot Navigation
```bash
# Get marker poses for navigation
ros2 run aruco_pose_estimation marker_service_client.py
```

### Object Tracking
```bash
# Monitor markers continuously
while true; do
    ros2 run aruco_pose_estimation marker_service_client.py
    sleep 1
done
```

### Calibration
```bash
# Use markers for system calibration
ros2 run aruco_pose_estimation test_marker_service.py
```

## 📈 Performance Notes

- **Service response time**: Typically < 100ms
- **Detection frequency**: Limited by camera frame rate (30 FPS)
- **Latest results**: Service returns the most recent detection results
- **No caching**: Each service call gets fresh detection data

## 📝 Notes

- The service returns the **latest detection results** from the ArUco node
- If no markers are detected, the service returns empty arrays
- The service is **stateless** - each call gets fresh data
- Service calls are **non-blocking** for the detection system
- The detection system continues running normally while serving requests

## 🆘 Support

For issues with the marker detection service:
1. Check the troubleshooting section above
2. Verify the ArUco detection system is running properly
3. Ensure camera and markers are properly configured
4. Check ROS2 service and topic connectivity

---

**Happy Marker Detection! 🎯**
