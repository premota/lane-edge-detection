# Lane Detection Project

## Test Result
![lane edge detection](https://github.com/premota/lane-edge-detection/assets/105300445/0e7524dc-184b-4a91-8f0e-37e7dfce2b70)

## Overview
The Lane Detection Project is an image processing and computer vision endeavor aimed at detecting and highlighting lanes in images or videos. The project is implemented in Python using the OpenCV library, providing a set of scripts for image preprocessing and straight lane detection.

## Project Components

**image_preprocessing.py**

The image_preprocessing.py script encompasses various functions crucial for preparing images for lane detection. 
These functions include 
1. Canny edge detection
2. region of interest masking
3. Hough line detection
4. A mechanism for averaging slope and intercept to identify lanes effectively.

**straight_lane_detection.py**

The straight_lane_detection.py script utilizes the preprocessed images or videos to perform real-time straight lane detection. The combination of image preprocessing and lane detection allows for an accurate representation of road lanes in various scenarios.

## Motivation

The primary motivation behind this project is to enhance road safety through advanced driver assistance systems (ADAS). By accurately detecting and tracking lanes, this project lays the foundation for applications in autonomous vehicles, driver alert systems, and lane-keeping assistance. Although this project takes a simplified approach to solving the problem, it can also stand as a good foundation in understanding the abilities of computer vision and openCV and how it can be utilized for simple lane detection.

## Real-World Applications of Lane detection systems.

1. Autonomous Vehicles
In the realm of autonomous vehicles, accurate lane detection is crucial for navigation and trajectory planning. This project contributes to the development of self-driving technologies by providing a reliable method for identifying and following lanes on the road.

2. Driver Assistance Systems
Modern vehicles often incorporate driver assistance systems to enhance safety. Lane detection can be employed to alert drivers when they unintentionally deviate from their lanes, promoting safer driving practices.

## Future Developments
This project serves as a foundation for future developments in computer vision and image processing. Potential enhancements include advanced lane detection algorithms, integration with additional sensors, and adaptation for complex road scenarios.
