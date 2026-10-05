import cv2
from stackImages import stackImages
import numpy as np

def getContours(imgMask , imgDisplay):
    contours, hierarchy = cv2.findContours(imgMask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cx, cy = None, None
    if len(contours) > 0:
        biggestContour = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(biggestContour)
        if area > 1000:
            x, y, w, h = cv2.boundingRect(biggestContour)
            cx = x + (w // 2)
            cy = y + (h // 2)
            cv2.rectangle(imgDisplay, (x , y ), (x + w, y + h),2)
            cv2.circle(imgDisplay, (cx, cy), 5, (0, 0, 255), cv2.FILLED)
    return cx , cy



def initalizeTrackbars():
    def empty(a):
        pass

    cv2.namedWindow("BGR(original)")
    cv2.resizeWindow("BGR(original)", 600, 400)
    cv2.createTrackbar("Hue Min", "BGR(original)", 0, 179, empty)
    cv2.createTrackbar("Hue Max", "BGR(original)", 179, 179, empty)
    cv2.createTrackbar("Sat Min", "BGR(original)", 0, 255, empty)
    cv2.createTrackbar("Sat Max", "BGR(original)", 255, 255, empty)
    cv2.createTrackbar("Val Min", "BGR(original)", 0, 255, empty)
    cv2.createTrackbar("Val Max", "BGR(original)", 255, 255, empty)

def getTrackbarValue():
    h_min = cv2.getTrackbarPos("Hue Min", "BGR(original)")
    h_max = cv2.getTrackbarPos("Hue Max", "BGR(original)")
    s_min = cv2.getTrackbarPos("Sat Min", "BGR(original)")
    s_max = cv2.getTrackbarPos("Sat Max", "BGR(original)")
    v_min = cv2.getTrackbarPos("Val Min", "BGR(original)")
    v_max = cv2.getTrackbarPos("Val Max", "BGR(original)")
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    return lower , upper

