# VisionAssist – YOLO-Based Object Detection with Voice Guidance

VisionAssist is a real-time object detection and voice guidance system built using **YOLO (You Only Look Once)**.  
The system detects objects through a live camera feed and provides **audio feedback**, making it useful as an assistive technology prototype and for smart vision applications.

---

##Project Overview

The system performs the following operations:
	•	Detects objects in real time using a webcam and a YOLO object detection model
	•	Measures distance using an ultrasonic sensor connected to an Arduino
	•	Provides spoken feedback describing the detected object and its distance

---

## 🚀 Features
- Real-time object detection using **YOLO**
- Voice guidance for detected objects
- Live video processing with **OpenCV**
- Can be integrated with sensors for distance awareness
- Modular and extendable design

---

## 🛠️ Technologies Used
- **Python**
- **YOLO (Object Detection)**
- **OpenCV**
- **Text-to-Speech (TTS)**
- **Arduino & Ultrasonic Sensor** (optional)

---

## 📂 Project Structure

isionAssist-YOLO-Voice-Guidance/
│
├── main.py
├── yolo/
│   ├── yolov3.cfg
│   ├── coco.names
│
├── arduino/
│   └── distance_sensor.ino
│
├── README.md
└── .gitignore

---
---

## ⚙️ Installation & Setup
  ### 1️⃣ Clone the Repository
    ```bash
    git clone https://github.com/YOUR_USERNAME/VisionAssist-YOLO-Voice-Guidance.git
    cd VisionAssist-YOLO-Voice-Guidance

##Install Required Libraries
  '''bash
   pip install opencv-python numpy pyttsx3

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
