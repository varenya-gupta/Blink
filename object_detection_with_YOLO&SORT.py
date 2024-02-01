#import all libraries
from ultralytics import YOLO
import cv2
import cvzone
import math
from sort import *

#define camera capture through webcam using cv2 and set dimensions
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

#create Yolo model
model = YOLO('yolov8n.pt')


#define names list for yolov8 database
classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]

#create a SORT based tracker
tracker = Sort(max_age=20, min_hits=3, iou_threshold=0.3)

while cap.isOpened():
    success, img = cap.read()
    #run each frame through the model to get detections
    results = model(img, stream=True)
    #define a empty numpy array to store detection data in tracker
    detections = np.empty((0, 5))
    for r in results:
        boxes = r.boxes
        for box in boxes:
            #get bbox coordinates
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2-x1, y2-y1
            bbox = int(x1), int(y1), int(w), int(h)
            #get confidence and class of each object
            conf = math.ceil((box.conf[0]*100))/100
            cls = int(box.cls[0])
            print(conf)
            print(classNames[cls])
            #create a numpy array that gets the position and confidence of each object
            currentArray = np.array([x1, y1, x2, y2, conf])
            #vertically stack the currentArray arrays in detections
            detections = np.vstack((detections, currentArray))

    #send results into tracker
    resultsTracker = tracker.update(detections)
  
    #get id for each object through sort algorithm
    for result in resultsTracker:
        x1, y1, x2, y2, id = result
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        print(result)
        w, h = x2 - x1, y2 - y1
        #place bbox and text around each detection using cvzone
        cvzone.cornerRect(img, (x1, y1, w, h), l=9, rt=2, colorR=(255, 0, 255))
        cvzone.putTextRect(img, f' {int(id)}', (max(0, x1), max(35, y1)),
                           scale=2, thickness=3, offset=10)
      
    #show detected frames with cv2
    cv2.imshow("Image", img)
    cv2.waitKey(1)
