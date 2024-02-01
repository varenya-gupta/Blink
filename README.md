# Blink
Blink is a a device that helps blind people in navigation by using a object detection system with a tracking based algorithm, a openai api based generative ai, and a voice recognition that allows the user to seamlessly understand and navigate their surroundings and a gps system with directions using googles directions and geolocation api.

# How to run and test the programs:
## Step1: 
Create a `virtual enviornment` to install all the required libraries. These libraries will be required to run the programs. I would recommend using an IDE such as Pycharm as they have direct ways to create a new virtual enviornment when creating a new project or when creating a new interpreter.

![image](https://github.com/varenya-gupta/Blink/assets/153254554/a0046503-c117-4067-82c4-436b6f7f6a39)

## Step2:
Install all libraries in the `requirements.txt` file either by duplicating it and opening it in a IDE like Pycharm or by manually downloading them through pip.

![image](https://github.com/varenya-gupta/Blink/assets/153254554/f65d2b10-7321-4691-8818-d49b622f6b1e)

## Step3:
Duplicate the rest of the files into the virtual enviornment and run and test the various programs.

# Important points and helpful tips for running the programs:
* For running `object_detection_with_YOLO&SORT.py` a webcam is required as the cv2 function has been setup for using a camera. For testing using a video use the path of the video instead of the webcam and     
  commenting out the width and height settings like so:
  ```
  cap = cv2.VideoCapture('path to video file')
  #cap.set(3, 1280)
  #cap.set(4, 720)
  ```
* Before attempting to use `basic_openai_api_usage.py` api key that has been provided in the synopsis must be used.
  
  ![apikeyhidden](https://github.com/varenya-gupta/Blink/assets/153254554/4a9bd1d1-f0b4-4ff3-a426-d1c4edf71f8d)

  ```
  openai.api_key = "place key here"
  ```
* `object_detection_on_images_with_YOLO&OPENAI.py` requires path to a image in the results line.
  ```
  results = model("place image path here", show=True)
  ```
  
* Using `coordinates_finder.py` will prompt for a location and then will provide the latitude and longitude of that place as well as your current location's latitude and longitude. However due to certain reasons we haven't been able to use the `directions api` by google.

* Some Images and Videos have been provide in the `refrences` folder and can be used for testing.
