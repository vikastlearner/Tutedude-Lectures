import cv2
import numpy as np

# img = cv2.imread('C:/Users/tiwar/Desktop/image1.png', cv2.IMREAD_COLOR)
img = np.zeros((700,700,3), np.uint8)

cv2.line(img, (10,10), (10,150), (255,0,0), 2)
cv2.rectangle(img, (10,20), (150,150), (255,0,0), 2)
cv2.circle(img, (300,300), 200, (0,0,255), 5)

pts_polygon = np.array([[10,170], [100,300], [500, 50], [500,300]], np.int32)
cv2.polylines(img, [pts_polygon], True, (0,0,255), 2)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "Hello", (10,500), font, 2, (0,0,255), 2, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()