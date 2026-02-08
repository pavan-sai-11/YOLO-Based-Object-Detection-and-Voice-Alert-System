# VisionAssist – YOLO-Based Object Detection with Voice Guidance

VisionAssist is a real-time object detection and voice guidance system built using **YOLO (You Only Look Once)**.  
The system detects objects through a live camera feed and provides **audio feedback**, making it useful as an assistive technology prototype and for smart vision applications.

---

##Project Overview

The system performs the following operations:
 - Detects objects in real time using a webcam and a YOLO object detection model
 - Measures distance using an ultrasonic sensor connected to an Arduino
 - Provides spoken feedback describing the detected object and its distance

---

## Features
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

## ⚙️ Installation & Setup
  ### Clone the Repository
  
   ```bash
	git clone https://github.com/YOUR_USERNAME/VisionAssist-YOLO-Voice-Guidance.git
    cd VisionAssist-YOLO-Voice-Guidance
```

   ### Install Required Libraries
   
  ```bash
   pip install opencv-python numpy pyttsx3
  ```

## Download the YOLO weight file and place it inside the yolo/ folder:
	•	yolov3.weights

## Run the Application
  ```bash
  python main.py
```
## Output
  - Camera starts automatically
  - Objects are detected in real time
  - Detected objects are announced using voice guidance


## Future Enhancements
  - Upgrade to YOLOv8
  - Improve distance estimation
  - Add vibration or mobile alerts
  - Deploy on Raspberry Pi
  - Cloud-based object tracking

---

## ⚠ Limitations

  - Single-point distance sensing limits object-specific accuracy
  - Detection accuracy varies with lighting and system performance
  - Not optimized for real-world deployment

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


```
