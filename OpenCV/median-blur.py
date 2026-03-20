import cv2

img = cv2.imread('C:/Users/tiwar/Desktop/image1.png')

resized = cv2.resize(img,(400,600))

ksize = 3 # This is diff Gaussion and median. It take both value as 3 3.

blur = cv2.medianBlur(resized,ksize)

cv2.imshow('Orig', img)
cv2.imshow('blur', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()