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
'''python

import numpy as np
import cv2 as cv

def skinmask(img):
    hsvim = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    lower = np.array([0, 48, 80], dtype = "uint8")
    upper = np.array([20, 255, 255], dtype = "uint8")
    skinRegionHSV = cv.inRange(hsvim, lower, upper)
    blurred = cv.blur(skinRegionHSV, (2,2))
    ret, thresh = cv.threshold(blurred,0,255,cv.THRESH_BINARY)
    return thresh

def getcnthull(mask_img):
    contours, hierarchy = cv.findContours(mask_img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    contours = max(contours, key=lambda x: cv.contourArea(x))
    hull = cv.convexHull(contours)
    return contours, hull

def getdefects(contours):
    hull = cv.convexHull(contours, returnPoints=False)
    defects = cv.convexityDefects(contours, hull)
    return defects


def handDetection(img):
    handResult = {}
    try:
        mask_img = skinmask(img)
        contours, hull = getcnthull(mask_img)
        #cv.drawContours(img, [contours], -1, (255,255,0), 2)
        #cv.drawContours(img, [hull], -1, (0, 255, 255), 2)
        defects = getdefects(contours)
        if defects is not None:
            cnt = 0
            for i in range(defects.shape[0]):  # calculate the angle
                s, e, f, d = defects[i][0]
                start = tuple(contours[s][0])
                end = tuple(contours[e][0])
                far = tuple(contours[f][0])
                a = np.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
                b = np.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
                c = np.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
                angle = np.arccos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))  #      cosine theorem
                if angle <= np.pi / 2:  # angle less than 90 degree, treat as fingers
                    cnt += 1
            cv.putText(img, str(cnt), (0, 50), cv.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0) , 2, cv.LINE_AA)
            if cnt >= 7:
                handResult['handDetected'] = True
                cv.putText(img, "HAND DETECTED", (50, 100), cv.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0) , 2, cv.LINE_AA)
            else:
                handResult['handDetected'] = False
        return handResult    
    except:
        pass

'''











