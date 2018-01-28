# Python Python 2.7.5
# https://pythonprogramming.net/thresholding-image-analysis-python-opencv-tutorial/?completed=/image-arithmetics-logic-python-opencv-tutorial/

import cv2
import numpy as np

img = cv2.imread('bookpage.jpg')
cv2.imshow('original',img)

retval, threshold = cv2.threshold(img, 10, 255, cv2.THRESH_BINARY)
cv2.imshow('threshold',threshold)
# image_name, threshold, maximum, value, threshold type

grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval, gray_threshold = cv2.threshold(grayscaled, 10, 255, cv2.THRESH_BINARY)
cv2.imshow('gray_threshold',gray_threshold)
# Convert to Grayscale
# Set Threshold

th = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow('Adaptive threshold',th)

retval2,threshold2 = cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('Otsu threshold',threshold2)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Learn More : 
# 1. https://docs.opencv.org/3.3.1/d7/d4d/tutorial_py_thresholding.html
# 2. http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html