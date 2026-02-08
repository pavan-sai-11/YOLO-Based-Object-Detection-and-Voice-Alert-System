# Real-Time-Object-Detection-and-Voice-Guidance-System
This project is an AI-based assistive system that combines computer vision (YOLO object detection) with an Arduino ultrasonic distance sensor to detect nearby objects and announce them using voice output. It is designed to help users, especially the visually impaired, to become aware of nearby obstacles.

---

## 📷 Project Overview

The system performs the following functions:

- Detects objects in real time using a webcam and a deep learning model.
- Measures distance using an ultrasonic sensor connected to Arduino.
- Provides audio feedback describing the detected object and its distance.

### Example Output
"There is a person at 75 centimeters"

---

## 🧠 Technologies Used

### Software
- Python
- OpenCV (cv2)
- YOLOv3 Object Detection
- PySerial
- pyttsx3 (Text to Speech)
- NumPy

### Hardware
- Arduino (UNO / Nano)
- Ultrasonic Sensor (HC-SR04)
- Webcam / Laptop Camera

---

## 🎯 Features

- Real-time object detection using deep learning
- Voice alerts for detected obstacles
- Integration of AI and IoT components
- Low-cost and easily extendable system
- Suitable for academic and demonstration purposes

---

## ⚠ Limitations

- Ultrasonic sensor provides only a single distance value, not per object
- Distance cannot be accurately mapped to a specific detected object
- Performance may be slow on low-end computers
- Not suitable for real-world navigation without further enhancements

---

## 🚀 Future Enhancements

- Use faster object detection models such as YOLOv4-tiny or YOLOv8
- Add vibration feedback for silent alerts
- Use multiple sensors for directional obstacle detection
- Integrate depth cameras for accurate distance estimation
- Convert the system into a wearable assistive device

---

## 🎓 Applications

- Assistive technology for visually impaired users
- Smart walking aids
- Robotics obstacle detection systems
- AI and IoT academic projects

---
## 📥 Download YOLO Files Using curl

You can download the required YOLO files directly using the following commands:

```bash
curl -O https://opencv-tutorial.readthedocs.io/en/latest/_downloads/10e685aad953495a95c17bfecd1649e5/yolov3.cfg

curl -L -o yolov3.weights https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov3.weights

curl -O https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names

---
