#!/usr/bin/env python3

import cv2
import numpy as np
import argparse
import os

def generate_aruco_markers(dictionary_id, marker_ids, marker_size, output_dir):
    """
    Generate ArUco markers and save them as PNG files.
    
    Args:
        dictionary_id: ArUco dictionary type (e.g., 'DICT_4X4_50')
        marker_ids: List of marker IDs to generate
        marker_size: Size of markers in pixels
        output_dir: Directory to save markers
    """
    
    # Get the dictionary
    dictionary = getattr(cv2.aruco, dictionary_id)
    aruco_dict = cv2.aruco.getPredefinedDictionary(dictionary)
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"Generating ArUco markers using {dictionary_id}")
    print(f"Marker size: {marker_size}x{marker_size} pixels")
    print(f"Output directory: {output_dir}")
    print("-" * 50)
    
    for marker_id in marker_ids:
        try:
            # Generate the marker
            marker = cv2.aruco.generateImageMarker(aruco_dict, marker_id, marker_size)
            
            # Save the marker
            filename = f"aruco_marker_{marker_id}_{dictionary_id}.png"
            filepath = os.path.join(output_dir, filename)
            cv2.imwrite(filepath, marker)
            
            print(f"Generated marker ID {marker_id} -> {filename}")
            
        except Exception as e:
            print(f"Error generating marker ID {marker_id}: {str(e)}")
    
    print("-" * 50)
    print(f"Generated {len(marker_ids)} markers in {output_dir}")

def main():
    parser = argparse.ArgumentParser(description='Generate ArUco markers')
    parser.add_argument('--dictionary', '-d', 
                       default='DICT_4X4_50',
                       help='ArUco dictionary type (default: DICT_4X4_50)')
    parser.add_argument('--ids', '-i', 
                       nargs='+', 
                       type=int, 
                       default=[0, 1, 2, 3, 4],
                       help='Marker IDs to generate (default: 0 1 2 3 4)')
    parser.add_argument('--size', '-s', 
                       type=int, 
                       default=200,
                       help='Marker size in pixels (default: 200)')
    parser.add_argument('--output', '-o', 
                       default='./aruco_markers',
                       help='Output directory (default: ./aruco_markers)')
    
    args = parser.parse_args()
    
    # Validate dictionary
    valid_dictionaries = [
        'DICT_4X4_50', 'DICT_4X4_100', 'DICT_4X4_250', 'DICT_4X4_1000',
        'DICT_5X5_50', 'DICT_5X5_100', 'DICT_5X5_250', 'DICT_5X5_1000',
        'DICT_6X6_50', 'DICT_6X6_100', 'DICT_6X6_250', 'DICT_6X6_1000',
        'DICT_7X7_50', 'DICT_7X7_100', 'DICT_7X7_250', 'DICT_7X7_1000'
    ]
    
    if args.dictionary not in valid_dictionaries:
        print(f"Error: Invalid dictionary '{args.dictionary}'")
        print(f"Valid dictionaries: {', '.join(valid_dictionaries)}")
        return
    
    generate_aruco_markers(args.dictionary, args.ids, args.size, args.output)

if __name__ == '__main__':
    main()
