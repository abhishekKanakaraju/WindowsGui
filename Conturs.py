import numpy as np
from PIL import ImageGrab
import cv2
import time
Frame = np.array(ImageGrab.grab(bbox=(8,48,635,364)))
Gray = cv2.cvtColor(Frame, cv2.COLOR_BGR2GRAY)
Frame1 = np.array(ImageGrab.grab(bbox=(8,48,635,364)))
Gray1 = cv2.cvtColor(Frame1, cv2.COLOR_BGR2GRAY)

while(True):
	last_time = time.time()  
	d= cv2.absdiff(Gray,Gray1)
	#blur = cv2.GaussianBlur(d, (3, 3),0)
	kernel = np.ones((4, 4))
	closing=cv2.morphologyEx(d,cv2.MORPH_CLOSE,kernel)
	opening=cv2.morphologyEx(d,cv2.MORPH_OPEN,kernel)
	mask2 = cv2.inRange(closing, np.array([5]), np.array([255]))

	
	dilation = cv2.dilate(opening, kernel, iterations=1)
	
	#closing=cv2.morphologyEx(dilation,cv2.MORPH_CLOSE,kernel)
	filtered = cv2.GaussianBlur(closing, (3, 3), 0)
	ret, thresh = cv2.threshold(filtered, 5, 255, 0)
	contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	cv2.drawContours(d,contours,-1,(0,0,255),2)
	Gray=Gray1
	Frame1 = np.array(ImageGrab.grab(bbox=(8,48,635,364)))
	Gray1 = cv2.cvtColor(Frame1, cv2.COLOR_BGR2GRAY)
	cv2.imshow('close',d)
	cv2.imshow('open',dilation)
	if cv2.waitKey(25) & 0xFF == ord('q'):
		cv2.destroyAllWindows()
		break


