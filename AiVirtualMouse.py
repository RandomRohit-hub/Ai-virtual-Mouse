import cv2
import numpy as np
import hand_Module as htm
import time
import autopy

wCam, hCam = 640, 480


cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0


while True:
    #1. find hand landmark
    success, img = cap.read()

    # 2 get the tip of the index and middle finger
    #3 check t=which finger are up
    #4 only index finger : Moving mode
    #5 convert coordination
    #6 smoothen values
    #7 move mouse
    #8 both index and middle finger are up clicking mode
    #9 find distance bw finger
    #10 click mouse if distance short
    #11 frame rate
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img,str(int(fps)),(20,50),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),2)
    #12 display

    cv2.imshow("image", img)
    cv2.waitKey(1)
