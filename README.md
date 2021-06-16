# Virtual-Invigilator
this project is based on cheating detection
# About project
This project detects cheating in examination using hardware (camera, computer system, sound system) and software (machine learning and deep learning).
When system observes cheating activity then a buzzer will play or photo of suspect will be sent to email address of teachers. 
## The model contains following steps in detecting cheating
Hand detection 
Mobile detection
Head pose estimation
Multiple person detection
Email Sending
Decision
## Hand detection.
Suppose a student is giving sign to another student using his hand which can help another student in cheating so to detect this type of activity we trained a model that can detect hand activity 
Hand detection Checks the gesture of the student’s hand ,and if any cheating activity is found then it gives Hand detection output TRUE.
And if any cheating activity is no detected then it give output FALSE.
The hand detection is done by openCV library 
WORKING :
Framewise video capturing takes place with 1second delay ,each video frame is classified after mathching with pretrained data .
So after classification when program observes hand detection data then it gives Hand detection output :TRUE
Otherwise it give FALSE output
and the text will be shown on screen i.e Warning !! Hand acivity deteced

![Screenshot 6_14_2021 7_56_22 PM](https://user-images.githubusercontent.com/77377586/122266084-0b7e4280-cef7-11eb-8042-021d21509e90.png)

### Techincal part of hand detection
OpenCv plays main role in hand detection 
#### Importing Libraries
cv2: opencv [pip install opencv]
numpy: for handling arrays as well as for math [pip install numpy]
#### Reading Image
#### SkinMask

It is used for highlighting specific color on image.
hsvim : Change BGR (blue, green, red) image to HSV (hue, saturation, value).
lower : lower range of skin color in HSV.
upper : upper range of skin color in HSV.
skinRegionHSV : Detect skin on the range of lower and upper pixel values in the HSV colorspace.
blurred: bluring image to improve masking.
thresh : applying threshing.
#### Contours
#### Convex Hull
#### Convexity Defects
Any deviation of the object from this hull can be considered as convexity defect.
#### Cosine Theorem
![Screenshot (339)](https://user-images.githubusercontent.com/77377586/122272863-75e6b100-cefe-11eb-86a9-4ad4ff874197.png)
![Screenshot (340)](https://user-images.githubusercontent.com/77377586/122272888-797a3800-cefe-11eb-86e8-f1ec79284afe.png)


a,b,c and angle: gamma. Now this gamma is always less than 90 degree, So we can say: If gamma is less than 90 degree or pi/2 we consider it as a finger.

![Screenshot (341)](https://user-images.githubusercontent.com/77377586/122272925-8139dc80-cefe-11eb-8f41-923a71297057.png)


#### Code 
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
#### dataset :
A pre trained dataset has been used that has 80 clasess of object detection 
name of the dataset is COCO-dataset 
we don't need to train and test the data for object detection we just need to call the mobile detection function and if the mobile is shown in screen than it will be automatically detected 

#### tensorflow
It is an open source artificial intelligence library, using data flow graphs to build models. It allows developers to create large-scale neural networks with many layers. TensorFlow is mainly used for: Classification, Perception, Understanding, Discovering, Prediction and Creation.
#### CNN
CNNs are used for image classification and recognition because of its high accuracy. ... The CNN follows a hierarchical model which works on building a network, like a funnel, and finally gives out a fully-connected layer where all the neurons are connected to each other and the output is processed
### Code
![Screenshot (351)](https://user-images.githubusercontent.com/77377586/122279619-e04f1f80-cf05-11eb-9b0e-a854f8bf062e.png)
![Screenshot (352)](https://user-images.githubusercontent.com/77377586/122279633-e513d380-cf05-11eb-8535-86659a8ef533.png)


## Head pose estimation 
Using head pose estimation we can identify that the studenyt's face is detecting or not in camera 
if the face is not detected then there will be shown a warning on the screen
this is done by the help of Dlib library by the help of shape predictor_68_facial_landmarks file 
#### shape predictor_68_facial_landmarks 
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
























