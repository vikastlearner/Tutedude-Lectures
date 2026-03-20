import cv2
import numpy as np

img = cv2.imread('C:/Users/tiwar/Desktop/image1.png')

column = img.shape[0]
row = img.shape[1]
center = (column/2, row/2)
angle = 90

r = cv2.getRotationMatrix2D(center, angle, 1)

rotate = cv2.warpAffine(img, r, (column, row))

cv2.imshow('Original', img)
cv2.imshow('shifted', rotate)
cv2.waitKey(0)
cv2.destroyAllWindows()