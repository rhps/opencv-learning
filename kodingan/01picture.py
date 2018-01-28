# Python 2.7.13
# https://pythonprogramming.net/loading-video-python-opencv-tutorial/?completed=/loading-images-python-opencv-tutorial/

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./watch.jpg', 0)
# IMREAD_COLOR			: 1
# IMREAD_GRAYSCALE		: 0
# IMREAD_UNCHANGED		: -1

# Plot with CV2
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
# Plot With Matplotlib

plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])
plt.show()
'''