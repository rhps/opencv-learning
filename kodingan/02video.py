# Python Python 2.7.5
# https://pythonprogramming.net/loading-video-python-opencv-tutorial/?completed=/loading-images-python-opencv-tutorial/

import numpy as np
import cv2

cap = cv2.VideoCapture(0)
# Read the camera

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))
# Set Encoder
# Set Output writer
n = 0
while (True):
	ret, frame = cap.read()
	# get cameras state (ret) and frame
	print(ret, n)
	n = n + 1
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
	# create gray from frame that converted from BGR to Gray

	# COLOR_BGR2BGRA	: BGR -> add Alfa to standar
	# COLOR_BGR2RGB 	: BGR -> RGB
	# COLOR_BGR2GRAY	: BGR -> GRAY
	# COLOR_BGR2HSV		: BGR -> HSV
	# See : https://docs.opencv.org/3.1.0/d7/d1b/group__imgproc__misc.html#gga4e0972be5de079fed4e3a10e24ef5ef0ad3db9ff253b87d02efe4887b2f5d77ee

	out.write(frame)
	# Save the frame

	cv2.imshow('frame', gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
# Close Camera
# Cloas all windows
out.release()
# Close Writer