import cv2

img = cv2.imread('C:/Users/tiwar/Desktop/image1.png')
width = 400
height = 550
dim = (width, height)
resized = cv2.resize(img, dim)
cv2.imshow('Original', resized)

# Horizontal
hor = cv2.flip(resized, 0) # Code 0 is for horizontal
cv2.imshow('Horizontal', hor)

# Vertical
ver = cv2.flip(resized, 1) # Code 1 is for Vertical
cv2.imshow('Vertical', ver)

# Horizontal and Vertical
hor_ver = cv2.flip(resized, -1) # Code 0 is for horizontal
cv2.imshow('Hor_Ver', hor_ver)

cv2.waitKey(0)
cv2.destroyAllWindows()
