import cv2

video = cv2.VideoCapture('C:/Users/tiwar/Desktop/videoplayback.mp4')

while video.isOpened():
    _,frame = video.read()
    frame = cv2.resize(frame,(600,400))

    cv2.imshow('Output',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()