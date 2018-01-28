# Python 2.7.5
# https://pythonprogramming.net/image-operations-python-opencv-tutorial/

import cv2
import numpy as np

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

img[55,55] = [255,255,255]
px = img[55,55]
print(px)

# Change img in array [55.55] to white
# define a reference 
# Print reference

img[100:150,100:150] = [255,255,255]

# Change img in array [100:150,100:150] to white

print(img.shape)
print(img.size)
print(img.dtype)


watch_face = img[37:111,107:194]
img[0:74,0:87] = watch_face

# Add Cropping Image in Image

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()