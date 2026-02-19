Sign Language Detection using YOLOv8
Overview

This project implements a real-time Sign Language Recognition System using YOLOv8 and OpenCV.
It detects American Sign Language (ASL) alphabets from a live webcam feed and builds words dynamically.

The system is designed as a prototype for deployment on embedded platforms such as Raspberry Pi.

Features

Real-time hand gesture detection

ASL alphabet recognition

Confidence score display

Word building logic (prototype)

Edge-device ready architecture

Tech Stack

Python

YOLOv8 (Ultralytics)

OpenCV

NumPy

Raspberry Pi (Future Deployment)

Model Details

Model: YOLOv8 custom-trained model

Dataset: Custom ASL alphabet dataset

Input: Live webcam stream

Output: Bounding box + predicted alphabet + confidence score


## Installation
1. Clone the repository
  git clone https://github.com/kumaransembedded/sign-language-yolo.git
cd sign-language-yolo
2. Install dependencies
  pip install -r requirements.txt

## Demo
 Future Improvements
  1.Sentence auto-formation improvement
  2.Cloud-based inference version
  3.ESP32 camera integration
  4.Full deployment on Raspberry Pi
  5.Larger and more robust dataset
  
##Project Impact  
  This project demonstrates:
   Real-time computer vision implementation
   Custom YOLO model training 
   Embedded deployment planning
   Practical application of AI in assistive technology
   
Author
Kumaran
Embedded & Automation Engineer
GitHub: https://github.com/kumaransembedded
