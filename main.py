import serial
import time
import cv2
import pyttsx3
import numpy as np

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

try:
    ser = serial.Serial('COM7', 9600, timeout=1)
    time.sleep(2)
    print("[INFO] Serial connected")
except Exception as e:
    print(f"[ERROR] Serial not connected: {e}")
    ser = None

net = cv2.dnn.readNetFromDarknet("yolov3.cfg", "yolov3.weights")
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers().flatten()]

with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

cap = cv2.VideoCapture(0)
last_spoken = ""

while True:
    ret, frame = cap.read()
    if not ret:
        break

    distance = None
    if ser and ser.in_waiting:
        try:
            line = ser.readline().decode().strip()
            distance = int(float(line))
        except:
            distance = None

    h, w = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    detections = net.forward(output_layers)

    boxes, confidences, class_ids = [], [], []

    for output in detections:
        for det in output:
            scores = det[5:]
            cid = np.argmax(scores)
            conf = scores[cid]
            if conf > 0.5:
                cx = int(det[0] * w)
                cy = int(det[1] * h)
                bw = int(det[2] * w)
                bh = int(det[3] * h)
                x = int(cx - bw / 2)
                y = int(cy - bh / 2)
                boxes.append([x, y, bw, bh])
                confidences.append(float(conf))
                class_ids.append(cid)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    object_name = None
    if len(indexes) > 0:
        i = indexes.flatten()[0]
        object_name = classes[class_ids[i]]
        x, y, bw, bh = boxes[i]
        label = f"{object_name} ({int(confidences[i]*100)}%)"
        cv2.rectangle(frame, (x, y), (x + bw, y + bh), (0, 255, 0), 2)
        cv2.putText(frame, label, (x, y - 8), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    if object_name and distance is not None:
        message = f"There is a {object_name} at {distance} centimeters"
        if message != last_spoken:
            print(message)
            try:
                engine.say(message)
                engine.runAndWait()
                last_spoken = message
            except Exception as e:
                print("TTS error:", e)

    cv2.imshow("Object Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
if ser:
    ser.close()
cv2.destroyAllWindows()
