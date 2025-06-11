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
detector=htm.handDetector(maxHands=1)
wScr,hScr=autopy.screen.size()
print(wScr,hScr)


while True:
    #1. find hand landmark
    success, img = cap.read()
    img=detector.findHands(img)
    lmList,bbox=detector.findPosition(img)
    print(lmList)

    # 2 get the tip of the index and middle finger
    if len(lmList) != 0:
        x1,y1=lmList[8][1:]
        x2,y2=lmList[12][1:]
        print(x1,y1,x2,y2)
    #3 check t=which finger are up
    fingers =detector.fingersUp()
    # print(fingers)
    #4 only index finger : Moving mode
    if fingers[1]==1 and fingers[2]==0:

    #5 convert coordination
        x3=np.interp(x1,(0,wCam),(0,wScr))
        y3=np.interp(y1,(0,hCam),(0,hScr))
    #6 smoothen values

    #7 move mouse
        autopy.mouse.move (wScr-x3,y3)
        cv2.circle(img, (x1, y1), 5, (0, 255, 250), cv2.FILLED)

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
