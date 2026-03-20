import cv2

img = cv2.imread('C:/Users/tiwar/Desktop/image1.png')

resized = cv2.resize(img,(400,600))

ksize = (7, 7) # It should be positive
sigmax = 0
sigmay = 0
blur = cv2.GaussianBlur(resized,ksize, sigmax)

cv2.imshow('Orig', img)
cv2.imshow('blur', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()