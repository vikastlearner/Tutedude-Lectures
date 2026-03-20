import cv2
import numpy as np

img = cv2.imread('C:/Users/tiwar/Desktop/image1.png')

threshold = 150

_,binary_threshold = cv2.threshold(img,threshold,255,cv2.THRESH_BINARY)

cv2.imshow('Original',img)
cv2.imshow('binary',binary_threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()