# Python Python 2.7.5
# https://pythonprogramming.net/drawing-writing-python-opencv-tutorial/?completed=/loading-video-python-opencv-tutorial/

import cv2
import numpy as np

img = cv2.imread('./watch.jpg', 1)

# cv2.line(img, (0,0),(100,100),(0,0,255),15)
# Plot Line (image_name, start coordinate, finish coordinate, color, thicknes)

# cv2.rectangle(img, (15,25), (200,150), (0,0,255), 15)
# Plot Rectangle (image_name, start coordinate one side, finish coordinate other side, color, thicknes)

# cv2.circle(img, (100,63), 55, (0,255,0), 12)
# Plot Rectangle (image_name, center circle coordinate, radius of circle, color, thicknes)
# -1 thickeness mean fill all

#pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
#cv2.polylines(img, [pts], True, (0,255,255), 3)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV Tuts!',(0,130), font, 1, (200,255,155), 2, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()