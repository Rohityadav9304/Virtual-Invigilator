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
img_path = "data/palm.jpg"
img = cv.imread(img_path)
cv.imshow('palm image',img)
#### SkinMask

It is used for highlighting specific color on image.
hsvim : Change BGR (blue, green, red) image to HSV (hue, saturation, value).
lower : lower range of skin color in HSV.
upper : upper range of skin color in HSV.
skinRegionHSV : Detect skin on the range of lower and upper pixel values in the HSV colorspace.
blurred: bluring image to improve masking.
thresh : applying threshing.

hsvim = cv.cvtColor(img, cv.COLOR_BGR2HSV)
lower = np.array([0, 48, 80], dtype = "uint8")
upper = np.array([20, 255, 255], dtype = "uint8")
skinRegionHSV = cv.inRange(hsvim, lower, upper)
blurred = cv.blur(skinRegionHSV, (2,2))
ret,thresh = cv.threshold(blurred,0,255,cv.THRESH_BINARY)
cv.imshow("thresh", thresh)

#### Contours
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
contours = max(contours, key=lambda x: cv.contourArea(x))
cv.drawContours(img, [contours], -1, (255,255,0), 2)
cv.imshow("contours", img

#### Convex Hull
hull = cv.convexHull(contours)
cv.drawContours(img, [hull], -1, (0, 255, 255), 2)
cv.imshow("hull", img)
#### Convexity Defects
Any deviation of the object from this hull can be considered as convexity defect.
hull = cv.convexHull(contours, returnPoints=False)
defects = cv.convexityDefects(contours, hull)
#### Cosine Theorem

![Screenshot (339)](https://user-images.githubusercontent.com/77377586/122270906-70886700-cefc-11eb-81e7-550ddfd7aef4.png)
![Screenshot (340)](https://user-images.githubusercontent.com/77377586/122270924-78480b80-cefc-11eb-9e11-b6d0efd2d7bb.png)


a,b,c and angle: gamma. Now this gamma is always less than 90 degree, So we can say: If gamma is less than 90 degree or pi/2 we consider it as a finger.

![Screenshot (341)](https://user-images.githubusercontent.com/77377586/122271387-f99f9e00-cefc-11eb-8a26-4567e4d6bbbd.png)
![Screenshot (342)](https://user-images.githubusercontent.com/77377586/122271419-03290600-cefd-11eb-97ad-2a93e816e931.png)

















