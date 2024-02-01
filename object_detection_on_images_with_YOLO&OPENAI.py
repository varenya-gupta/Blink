#import necessary libraries 
from ultralytics import YOLO
import cv2
#import openai program from file
import basic_openai_api_usage.py

#create Yolo model
model = YOLO('yolov8n.pt')

#define class names for yolo database
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

#define dictionary to get number of each class in database
IdentifiedClassNames = {"person":0, "bicycle":0, "car":0, "motorbike":0, "aeroplane":0, "bus":0, "train":0, "truck":0, "boat":0,
              "traffic light":0, "fire hydrant":0, "stop sign":0, "parking meter":0, "bench":0, "bird":0, "cat":0,
              "dog":0, "horse":0, "sheep":0, "cow":0, "elephant":0, "bear":0, "zebra":0, "giraffe":0, "backpack":0, "umbrella":0,
              "handbag":0, "tie":0, "suitcase":0, "frisbee":0, "skis":0, "snowboard":0, "sports ball":0, "kite":0, "baseball bat":0,
              "baseball glove":0, "skateboard":0, "surfboard":0, "tennis racket":0, "bottle":0, "wine glass":0, "cup":0,
              "fork":0, "knife":0, "spoon":0, "bowl":0, "banana":0, "apple":0, "sandwich":0, "orange":0, "broccoli":0,
              "carrot":0, "hot dog":0, "pizza":0, "donut":0, "cake":0, "chair":0, "sofa":0, "pottedplant":0, "bed":0,
              "diningtable":0, "toilet":0, "tvmonitor":0, "laptop":0, "mouse":0, "remote":0, "keyboard":0, "cell phone":0,
              "microwave":0, "oven":0, "toaster":0, "sink":0, "refrigerator":0, "book":0, "clock":0, "vase":0, "scissors":0,
              "teddy bear":0, "hair drier":0, "toothbrush":0}

#define another dictionary to remove classes with 0 number using basic logic
GptNames = {}

#generate results by running the image through the model
results = model("place image path here", show=True)
cv2.waitKey(0)
#basic code to add 1 to each class in IdentifiedClassNames for each detection
for r in results:
    boxes = r.boxes
    for box in boxes:
        cls = int(box.cls[0])
        identify = classNames[cls]
        IdentifiedClassNames[identify] += 1

#logic to remove classes with 0 number
for key, value in IdentifiedClassNames.items():
    if value > 0:
        GptNames[key] = value
# convert to string
GptNames = str(GptNames)
#run dictionary through openai while using specificly engineered prompt to get a response
basic_openai_api_usage.check(GptNames)
