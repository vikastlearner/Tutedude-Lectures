'''
1. Noised reduction
2. Intensity of the gradient of the image
3. Non-maximum suppression
4. Thresholding
'''

import cv2
import numpy as np

img = cv2.imread('C:/Users/tiwar/Desktop/image1.png')
resized = cv2.resize(img,(600,400))
min_threshold = 100
max_threshold = 200
edges = cv2.Canny(resized,min_threshold,max_threshold)

cv2.imshow('orig',resized)
cv2.imshow('edges',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()