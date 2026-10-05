import cv2
import numpy as np
from utils1 import *

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

initalizeTrackbars()

canvas = None

points = []

drawColor = ( 0, 0, 255)



while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    if canvas is None:
        canvas = np.zeros_like(img)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    imgBlur = cv2.GaussianBlur(imgHSV, (3, 3), 0)
    lower , upper = getTrackbarValue()
    mask = cv2.inRange(imgBlur, lower, upper)
    kernel = np.ones((9, 9), np.uint8)
    maskDialation = cv2.dilate(mask, kernel, iterations=2)
    maskEroded = cv2.erode(maskDialation, kernel, iterations=1)
    cx ,cy = getContours(maskEroded , img)
    if cx is not None and cy is not None:
        if cy < 60 and cx < 120:
            canvas = np.zeros_like(img)  # Tuvali temizle
            points.clear()  # Geçmiş noktaları sil
            points.append(None)
        else:
            points.append((cx, cy))
    else:
        points.append(None)
    for i in range  (1 , len(points)):
        if points[i - 1] is None or points[i] is None:
            continue
        if points[i - 1] == points[i]:
            continue
        cv2.line(canvas,points[i-1],points[i],(0,0,255),20)
    cv2.rectangle(img, (0, 0), (120, 60), (255, 255, 255), cv2.FILLED)
    cv2.putText(img, "CLEAR", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
    imgFinal = cv2.addWeighted(img, 0.8, canvas, 1.0, 0)
    cv2.imshow("Air Canvas", imgFinal)
    cv2.imshow("Mask", maskEroded)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


