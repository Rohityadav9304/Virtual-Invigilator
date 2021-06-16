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
hull = cv.convexHull(contours, returnPoints=False)
defects = cv.convexityDefects(contours, hull)
#### Cosine Theorem
![Screenshot (339)](https://user-images.githubusercontent.com/77377586/122272863-75e6b100-cefe-11eb-86a9-4ad4ff874197.png)
![Screenshot (340)](https://user-images.githubusercontent.com/77377586/122272888-797a3800-cefe-11eb-86e8-f1ec79284afe.png)


a,b,c and angle: gamma. Now this gamma is always less than 90 degree, So we can say: If gamma is less than 90 degree or pi/2 we consider it as a finger.

![Screenshot (341)](https://user-images.githubusercontent.com/77377586/122272925-8139dc80-cefe-11eb-8f41-923a71297057.png)


#### Code 
![Screenshot (345)](https://user-images.githubusercontent.com/77377586/122272206-ee993d80-cefd-11eb-99c7-6dd5328a7955.png)
![Screenshot (346)](https://user-images.githubusercontent.com/77377586/122272232-f822a580-cefd-11eb-802a-d7c9b923e1d0.png)


















