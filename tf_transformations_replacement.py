#!/usr/bin/env python3
"""
Simple replacement for tf_transformations using scipy
"""

import numpy as np
from scipy.spatial.transform import Rotation as R

def quaternion_from_euler(ai, aj, ak):
    """Convert Euler angles to quaternion"""
    r = R.from_euler('xyz', [ai, aj, ak], degrees=False)
    return r.as_quat()

def euler_from_quaternion(quaternion):
    """Convert quaternion to Euler angles"""
    r = R.from_quat(quaternion)
    return r.as_euler('xyz')

def quaternion_multiply(quaternion1, quaternion0):
    """Multiply two quaternions"""
    w0, x0, y0, z0 = quaternion0
    w1, x1, y1, z1 = quaternion1
    return np.array([
        -x1*x0 - y1*y0 - z1*z0 + w1*w0,
         x1*w0 + y1*z0 - z1*y0 + w1*x0,
        -x1*z0 + y1*w0 + z1*x0 + w1*y0,
         x1*y0 - y1*x0 + z1*w0 + w1*z0
    ])

def quaternion_inverse(quaternion):
    """Return inverse of quaternion"""
    q = np.array(quaternion)
    return q * np.array([1, -1, -1, -1])

def quaternion_conjugate(quaternion):
    """Return conjugate of quaternion"""
    q = np.array(quaternion)
    return q * np.array([1, -1, -1, -1])

def quaternion_norm(quaternion):
    """Return norm of quaternion"""
    return np.linalg.norm(quaternion)

def quaternion_normalize(quaternion):
    """Normalize quaternion"""
    q = np.array(quaternion)
    return q / quaternion_norm(q)
