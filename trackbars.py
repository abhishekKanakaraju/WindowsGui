import numpy as np
from PIL import ImageGrab
import cv2
import time
import math
import pyautogui

def nothing(x):
	pass
	
cv2.namedWindow('Trackbars')
cv2.createTrackbar('L-H','Trackbars',0,255, nothing)
cv2.createTrackbar('L-S','Trackbars',0,255, nothing)
cv2.createTrackbar('L-V','Trackbars',0,255, nothing)
cv2.createTrackbar('U-H','Trackbars',255,255, nothing)
cv2.createTrackbar('U-S','Trackbars',255,255, nothing)
cv2.createTrackbar('U-V','Trackbars',255,255, nothing)

# Open Camera
capture = cv2.VideoCapture(0)



while capture.isOpened():
    ret, frame = capture.read()
    crop_image = frame[0:384,0:683]
    l_h=cv2.getTrackbarPos('L-H','Trackbars')
    l_s=cv2.getTrackbarPos('L-S','Trackbars')
    l_v=cv2.getTrackbarPos('L-V','Trackbars')
    u_h=cv2.getTrackbarPos('U-H','Trackbars')
    u_s=cv2.getTrackbarPos('U-S','Trackbars')
    u_v=cv2.getTrackbarPos('U-V','Trackbars')
    lower=np.array([l_h,l_s,l_v])
    higher=np.array([u_h,u_s,u_v])
    mask2 = cv2.inRange(crop_image, lower, higher)
    cv2.imshow("lknf", mask2)
    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

