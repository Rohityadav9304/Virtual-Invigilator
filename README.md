# Virtual-Invigilator
this project is based on cheating detection
# About project :
This project detects cheating in examination using hardware (camera, computer system, sound system) and software (machine learning and deep learning).
When system observes cheating activity then a buzzer will play or photo of suspect will be sent to email address of teachers. 
## The model contains following steps in detecting cheating
1. Hand detection 
2. Mobile detection
3. Head pose estimation
4. Multiple person detection
5. Email Sending
6. Decision
# Flow digram :

![flow digram](https://user-images.githubusercontent.com/77377586/122285700-acc3c380-cf0c-11eb-9c23-64a231acefdc.png)

# Block digram :
![blog digram](https://user-images.githubusercontent.com/77377586/122286309-560ab980-cf0d-11eb-85bc-8210c0312d38.jpg)



## Hand detection.
Suppose a student is giving sign to another student using his hand which can help another student in cheating so to detect this type of activity we trained a model that can
detect hand activity 
Hand detection Checks the gesture of the student’s hand ,and if any cheating activity is found then it gives Hand detection output TRUE.
And if any cheating activity is no detected then it give output FALSE.
The hand detection is done by openCV library 
WORKING :
Framewise video capturing takes place with 1second delay ,each video frame is classified after mathching with pretrained data .
So after classification when program observes hand detection data then it gives Hand detection output :TRUE
Otherwise it give FALSE output
and the text will be shown on screen i.e Warning !! Hand acivity deteced

![Screenshot 6_14_2021 7_56_22 PM](https://user-images.githubusercontent.com/77377586/122266084-0b7e4280-cef7-11eb-8042-021d21509e90.png)

## Techincal part of hand detection
OpenCv plays main role in hand detection 
### Importing Libraries
### Reading Image
### SkinMask

It is used for highlighting specific color on image.
hsvim : Change BGR (blue, green, red) image to HSV (hue, saturation, value).
lower : lower range of skin color in HSV.
upper : upper range of skin color in HSV.
skinRegionHSV : Detect skin on the range of lower and upper pixel values in the HSV colorspace.
blurred: bluring image to improve masking.
thresh : applying threshing.
### Contours 
Outline 
### Convex Hull
### Convexity Defects
Any deviation of the object from this hull can be considered as convexity defect.
### Cosine Theorem

![Screenshot (339)](https://user-images.githubusercontent.com/77377586/122288810-a08d3580-cf0f-11eb-8572-f68243cb63f8.png)

![Screenshot (340)](https://user-images.githubusercontent.com/77377586/122272888-797a3800-cefe-11eb-86e8-f1ec79284afe.png)


a,b,c and angle: gamma. Now this gamma is always less than 90 degree, So we can say: If gamma is less than 90 degree or pi/2 we consider it as a finger.
### Counting fingers

![Screenshot (341)](https://user-images.githubusercontent.com/77377586/122288433-750a4b00-cf0f-11eb-913e-41adb719f8fe.png)

### Code 
![Screenshot (345)](https://user-images.githubusercontent.com/77377586/122272206-ee993d80-cefd-11eb-99c7-6dd5328a7955.png)
![Screenshot (346)](https://user-images.githubusercontent.com/77377586/122272232-f822a580-cefd-11eb-802a-d7c9b923e1d0.png)


## Mobile Detection
Moblie detection Checks the gesture of the student’s activity ,and if any Cell phone activity is found then it gives Mobile detection output TRUE.
And if any cheating activity is no detected then it give output FALSE.
Tensorflow and CNN is used for Mobile detection 
WORKING :
Framewise video capturing takes place with 1second delay ,each video frame is classified after mathching with pretrained data .
So after classification when program observes Mobile detection data then it gives Hand detection output :TRUE
Otherwise it give FALSE output
And a text will be shown on screen i.e Warning !!! Mobile detetected

![Screenshot 6_14_2021 7_56_38 PM](https://user-images.githubusercontent.com/77377586/122273406-0b824080-ceff-11eb-8829-2b99e0d122ec.png)
### techincal details 
### dataset :
A pre trained dataset has been used that has 80 clasess of object detection 
name of the dataset is COCO-dataset 
we don't need to train and test the data for object detection we just need to call the mobile detection function and if the mobile is shown in screen than it will be automatically detected 

### tensorflow
It is an open source artificial intelligence library, using data flow graphs to build models. It allows developers to create large-scale neural networks with many layers.
TensorFlow is mainly used for: Classification, Perception, Understanding, Discovering, Prediction and Creation.
### CNN
CNNs are used for image classification and recognition because of its high accuracy. ... The CNN follows a hierarchical model which works on building a network, like a funnel,
and finally gives out a fully-connected layer where all the neurons are connected to each other and the output is processed
### Code
![Screenshot (351)](https://user-images.githubusercontent.com/77377586/122279619-e04f1f80-cf05-11eb-9b0e-a854f8bf062e.png)
![Screenshot (352)](https://user-images.githubusercontent.com/77377586/122279633-e513d380-cf05-11eb-8535-86659a8ef533.png)


## Head pose estimation 
Using head pose estimation we can identify that the studenyt's face is detecting or not in camera 
if the face is not detected then there will be shown a warning on the screen
this is done by the help of Dlib library by the help of shape predictor_68_facial_landmarks file 
### shape predictor_68_facial_landmarks 
this file contains 68 facial landmarks that conains face co-ordinaes and head co-ordinates
n computer vision, the pose of an object refers to its relative orientation and position relative to the camera.

The purpose of face pose estimation is to obtain the orientation of the face relative to the camera:

The idea of ​​face pose estimation: rotate the 3D standard model by a certain angle until the "2D projection" of the "3D feature points" on the model coincides with the feature points on the image to be tested (the feature points on the image are obviously 2D) 

![Screenshot (347)](https://user-images.githubusercontent.com/77377586/122278691-ceb94800-cf04-11eb-89bf-0a9e575c5395.png)

![Frame 6_14_2021 7_55_47 PM](https://user-images.githubusercontent.com/77377586/122278862-058f5e00-cf05-11eb-9236-dc69ec6062bd.png)
![Screenshot 6_14_2021 7_56_48 PM](https://user-images.githubusercontent.com/77377586/122278902-117b2000-cf05-11eb-8690-ab4cd192c6d9.png)

### Code
![Screenshot (348)](https://user-images.githubusercontent.com/77377586/122279369-96fed000-cf05-11eb-9cf3-5fbc1222e14c.png)
![Screenshot (349)](https://user-images.githubusercontent.com/77377586/122279383-9bc38400-cf05-11eb-8a6c-6f0b43f20546.png)
![Screenshot (350)](https://user-images.githubusercontent.com/77377586/122279393-9e25de00-cf05-11eb-818b-f00a3dd4acb6.png)


## Multiple person detection :
This is a part of object detection and this is done by using CoCo datasets 
IF we are focused on a particular student only then multiple person detects multi person activity that weather another person is helping the student in cheating activity.
This is used for online examination


![Screenshot (227)](https://user-images.githubusercontent.com/77377586/122279958-43d94d00-cf06-11eb-8011-ae387dc31788.png)

### Technical details :
### Inside terminal
If you want to see the multiple person detection result then look inside the terminal this will show us the type of object weather is a person cat dog or teddy bear.
same as mobile detection
### Code
![Screenshot (351)](https://user-images.githubusercontent.com/77377586/122279679-f3fa8600-cf05-11eb-8487-babbd10781c3.png)
![Screenshot (352)](https://user-images.githubusercontent.com/77377586/122279696-f78e0d00-cf05-11eb-8eda-e403ba9906a4.png)


## E-mail/buzzer :
when our model identifies any cheating activity then the screenshort of that activity will be sent to the invigilator's e-mail address.
this process is done by smtp(simple mail transfer protocal) library. 
### Code :
![Screenshot (353)](https://user-images.githubusercontent.com/77377586/122280932-5738e800-cf07-11eb-857f-1bdc76447237.png)

# Decision :
As we know to check all these activites at a same time we need to import all the modules in 1 module so we create a main file and this main file will operates all the programms at a same time.
## main.py file :
we import all the sub modules in the main.py file 
this is our final decision taker.
## Flow chart

![flow chart](https://user-images.githubusercontent.com/77377586/122286056-15ab3b80-cf0d-11eb-9fa2-e0c78d9944d3.jpg)

## main.py file takes following decisions if any detection takes place
### If hand sign detected in camera :
#### Decision :Warning !! Hand activity

![Screenshot 6_14_2021 7_56_22 PM](https://user-images.githubusercontent.com/77377586/122283392-1e4e4280-cf0a-11eb-83a1-c53af516942d.png)

### If mobile detected in camera : 
#### Decision :Warning !! Cell phone Detected

![Screenshot 6_14_2021 7_56_38 PM](https://user-images.githubusercontent.com/77377586/122283469-33c36c80-cf0a-11eb-82e8-c6c1c3a0cf40.png)

### If Face not detected in camera :
#### Decision :Warning !! face not detected

![Screenshot 6_14_2021 7_57_01 PM](https://user-images.githubusercontent.com/77377586/122283638-62d9de00-cf0a-11eb-97d3-79c68886b044.png)

### If face is at the centre :
#### Decision : Looking at the centre

![Frame 6_14_2021 7_55_47 PM](https://user-images.githubusercontent.com/77377586/122283731-7ab16200-cf0a-11eb-8c13-ea53aa6d43c1.png)

### if hand detected and face not detected :
#### Decision :Warning !! Unusual activity!

![Frame 6_17_2021 1_26_16 AM](https://user-images.githubusercontent.com/77377586/122284628-6883f380-cf0b-11eb-8bd2-09f5130eaf0c.png)

### If hand detected face not detected and mobile detected :
#### decision :Warning !! 100 % cheating activity .

![Screenshot 6_14_2021 7_57_33 PM](https://user-images.githubusercontent.com/77377586/122284750-86515880-cf0b-11eb-8361-4170e7aa3c62.png)

### If multiple person detected on camera :
#### Decision : More than one person 

![Screenshot (227)](https://user-images.githubusercontent.com/77377586/122285297-29a26d80-cf0c-11eb-8b2a-97d1637d5c87.png)


### Code :

![Screenshot (354)](https://user-images.githubusercontent.com/77377586/122286761-d4675b80-cf0d-11eb-8aaf-68f0228b793c.png)
![Screenshot (355)](https://user-images.githubusercontent.com/77377586/122286780-d92c0f80-cf0d-11eb-87fb-a9a9ca026a62.png)
![Screenshot (356)](https://user-images.githubusercontent.com/77377586/122286794-dd582d00-cf0d-11eb-90f9-e0bf99c96678.png)


# Technologies used (technical details) :

# 1 openCV :
OpenCV is a huge open-source library for computer vision, machine learning, and image processing. OpenCV supports a wide variety of programming languages like Python, C++, Java,
etc. It can process images and videos to identify objects, faces, or even the handwriting of a human. When it is integrated with various libraries, such as Numpy which is a
highly optimized library for numerical operations, then the number of weapons increases in your Arsenal i.e whatever operations one can do in Numpy can be combined with OpenCV.
openCV is the most important library that has been used .
this is used to process :
1. Live video processing
2. frame capturing
3. Hand Detection
4. Writing text on Live screen` 
# 2 Machine learning :
Machine learning is an application of artificial intelligence (AI) that provides systems the ability to automatically learn and improve from experience without being explicitly programmed. Machine learning focuses on the development of computer programs that can access data and use it to learn for themselves.
we used machine learning to train and test our model
# 3 Numpy :
NumPy is the fundamental package for scientific computing in Python. ... NumPy arrays facilitate advanced mathematical and other types of operations on large numbers of data. Typically, such operations are executed more efficiently and with less code than is possible using Python's built-in sequences.
# 4 Deep learning :
Deep learning is a sub-branch of AI and ML that follow the workings of the human brain for processing the datasets and making efficient decision making. ... Practical examples of deep learning are Virtual assistants, vision for driverless cars, money laundering, face recognition and many more
We used deep learning in our project to train neural networks
# 5 Tensorflow Lite :
TensorFlow Lite is an open-source deep learning framework to run TensorFlow models on-device.
it has been used for object detection and image classification
# Keras :
Keras is an open-source software library that provides a Python interface for artificial neural networks. Keras acts as an interface for the TensorFlow library. 






























