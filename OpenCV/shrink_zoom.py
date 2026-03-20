import cv2

img = cv2.imread('C:/Users/tiwar/Desktop/image1.png')
print("Dimension of original image: ", img.shape)
cv2.imshow("Original Image", img)
scale = 150 # to Scale up or down, change the value.

width = int(img.shape[1] * scale/100)
height = int(img.shape[0] * scale/100)
dim = (width, height)
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
# interpolation is used to fill the pixel resized image.

print("Dimension of resized image: ", resized.shape)
cv2.imshow("Resized Image", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()

