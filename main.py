"""
This is the main script of cheating detection. It detects following things:
1. Hand detection 
2. Multiple person detection
3. Head pose detection
4. Mobile detection
"""

import cv2
import numpy as np
import time
import os
import dlib
# developers script
from Hand import handDetection
from objectDetection import objectDetection
from headPoseEstimation import getHeadPose
# import constants as constants
# from emailReport import sendEmail


#Open Camera object
cap = cv2.VideoCapture(0) #object creating
OSLoginId= os.getlogin()  #to get os login id
detector = dlib.get_frontal_face_detector()


# blue color in BGR
color = (255,0,0)

# Line thickness of 2 px
thickness = 2


while cap.isOpened():
    time.sleep(1)
    _, frame = cap.read()
    image = frame.copy()  #480 X 720
    faces = detector(frame)  # ; print(faces)
    hand_result = handDetection(frame) # image processing
    object_detection_result = objectDetection(frame)   #using cnn
    head_detection_result = getHeadPose(frame)
    print("Hand Detection :", hand_result)
    print("object detection:", object_detection_result)
    print("Head detection result:", head_detection_result)

    for face in faces:
        # The face landmarks code begins from here
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
    
    # cv2.rectangle()
    if faces==0:
     pass
    else:
     detect_face=x1
    start_point = (x1, y1)
    
    # Ending coordinate, here (220, 220)
    # represents the bottom right corner of rectangle
    end_point = (x2, y2)

    #image = cv2.rectangle(image, start_point, end_point, color, thickness)

    if object_detection_result['mobileDetection']:
        cv2.putText(image,"WARNING!!! mobile detected",(5,30),cv2.FONT_HERSHEY_SIMPLEX,1,(120,100,50),2, cv2.LINE_AA)
    if hand_result['handDetected']:
        cv2.putText(image,"Warning!! Hand activity detected",(5,45),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),2, cv2.LINE_AA)
    if head_detection_result == 0:
        cv2.putText(image,"WARNING!!! Looking center",(5,80),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),2, cv2.LINE_AA)
        pass
    if head_detection_result == None:
        cv2.putText(image,"WARNING!!! Face not detected",(5,80),cv2.FONT_HERSHEY_SIMPLEX,1,(0,100,100),2, cv2.LINE_AA)
        pass
    if hand_result['handDetected'] and head_detection_result == None:
        cv2.putText(image,"WARNING!!! Unusual activity",(5,350),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,100),2, cv2.LINE_AA)
        pass
    if hand_result['handDetected'] and object_detection_result['mobileDetection'] and head_detection_result == None:
        cv2.putText(image,"WARNING!!! 100% Cheating Activity",(5,400),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,100),2, cv2.LINE_AA)



        #face not detected
        pass


    cv2.imshow("Frame", image)
    #close the output video by pressing 'ESC'
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

