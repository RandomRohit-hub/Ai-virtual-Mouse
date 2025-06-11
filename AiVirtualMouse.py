import cv2
import numpy as np
import hand_Module as htm
import time
import autopy

# Set camera dimensions
wCam, hCam = 640, 480
frameR = 100  # Frame reduction for cursor control area

# Initialize webcam
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0  # Previous time for FPS calculation
detector = htm.handDetector(maxHands=1)

# Get screen size
wScr, hScr = autopy.screen.size()
print(wScr, hScr)

while True:
    # 1. Find hand landmarks
    success, img = cap.read()
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)

    # 2. Get the tip of the index and middle fingers
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]  # Index finger tip
        x2, y2 = lmList[12][1:]  # Middle finger tip

        print(x1, y1, x2, y2)

        # 3. Check which fingers are up
        fingers = detector.fingersUp()

        # 4. Draw frame rectangle
        cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (250, 0, 250), 2)

        # 5. Moving Mode: Only Index Finger Up
        if fingers[1] == 1 and fingers[2] == 0:
            # 6. Convert coordinates
            x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))

            # 7. Move mouse
            autopy.mouse.move(wScr - x3, y3)
            cv2.circle(img, (x1, y1), 5, (0, 255, 250), cv2.FILLED)

        # 8. Clicking Mode: Both Index and Middle Fingers Up
        if fingers[1] == 1 and fingers[2] == 1:
            length, img, _ = detector.findDistance(8, 12, img)  # Fixed call
            print(length)
            if length < 20:
                cv2.circle(img, (x1, y1), 5, (0, 255, 250), cv2.FILLED)

            # 10. Click mouse if distance is short (threshold example: < 40)
            if length < 40:
                autopy.mouse.click()

    # 11. Frame rate calculation
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

    # 12. Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)
