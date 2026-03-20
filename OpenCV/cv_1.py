import cv2

img = cv2.imread('C:/Users/tiwar/Desktop/image1.png', 0) # URL of image which is to be read.
print("Dimension:", img.shape)

width = img.shape[1]
height = 400
dim = (width, height)
resized = cv2.resize(img, dim)
cv2.imshow("window", resized)

# To read Image:
# cv2.imshow("window", img) # to see the image. The window is name of window.
cv2.waitKey(0) # The "0" let the window open, until closed. This is in ms, so 1000 = 1sc.
cv2.destroyAllWindows() # to open only the image I wnat to see and close others.

# # To Write image/Save image:
# cv2.imwrite("black_white.png", img)








