import cv2
import dlib
import numpy as np

from headPoseEstimation import getHeadPose

cap = cv2.VideoCapture(0)




while cap.isOpened():
    _, frame = cap.read()
    size = frame.shape
    result = getHeadPose(frame)
    print("result:", result)

    cv2.imshow("Output", frame)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break