import cv2

img = cv2.imread('C:/Users/tiwar/Desktop/image1.png')

resized = cv2.resize(img,(400,600))

d = 7
sigmacolor = 100
sigmaspace = 100

b = cv2.bilateralFilter(img,d,sigmacolor,sigmaspace)

cv2.imshow('Input',resized)
cv2.imshow('bilateral',b)
cv2.waitKey(0)
cv2.destroyAllWindows()