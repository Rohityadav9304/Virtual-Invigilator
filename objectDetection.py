from datetime import datetime
import cv2
import numpy as np
import time

import mobile_detect.object_detector_detection_api_lite as api_lite
detector = api_lite.ObjectDetectorLite()


def objectDetection(frame):
    """
    pre trained model on coco dataset
    coco dataset has 80 classes
    """
    objectDetectionResult = {}
    result = detector.detect(frame, 0.2)
    person_count=0
    objectDetectionResult['mobileDetection'] = False
    for obj in result:
        print("main detection from tensorflow:", obj) #[(60, 71), (632, 478), 0.9426616, 'person']
        if obj[3]=='person':
            # personConfidence = obj[2]  
            person_count = person_count+1
            (x1, y1) = obj[0]
            (x2, y2) = obj[1]

        elif obj[3]=='cell phone':
            (x1, y1) = obj[0]
            (x2, y2) = obj[1]
            cv2.rectangle(frame, obj[0], obj[1], (255, 0, 0), 2)
            mobileConfidence = obj[2] * 100
            mobileConfidence = "{:.2f}".format(mobileConfidence)
            objectDetectionResult['mobileDetection'] = True
            print(f'{[datetime.now().strftime("%H:%M:%S")]} ALERT!! Mobile detected {mobileConfidence}...')

    if person_count>1:
        objectDetectionResult['multiplePerson'] = True
        # isMultiplePerson = 1
        print(f'{[datetime.now().strftime("%H:%M:%S")]} ALERT!! More than 1 person detected...')
        # cv2.putText(frame,"WARNING!!! More than 1 person detected",(5,40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),2, cv2.LINE_AA)
    else:
        objectDetectionResult['multiplePerson'] = False
    
    return objectDetectionResult
