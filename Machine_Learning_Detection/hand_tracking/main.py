import time

import cv2
import mediapipe as mp

cap = cv2.VideoCapture(1)

mphands = mp.solutions.hands
hands = mphands.Hands()
mpdraw = mp.solutions.drawing_utils

ptime = 0
ctime = 0

while True:
    success, img = cap.read()
    imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgrgb)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        # deect points
        for handlms in results.multi_hand_landmarks:
            # color circle at id point
            for id, lm in enumerate(handlms.landmark):
                # print(id, lm)
                h, w, c = img.shape
                # converting ratio to
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(id, cx, cy)
                # if id == 4:
                cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

            mpdraw.draw_landmarks(img, handlms, mphands.HAND_CONNECTIONS)

    # frame per second
    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime

    cv2.putText(
        img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3
    )

    cv2.imshow("Image", img)
    cv2.waitKey(1)
