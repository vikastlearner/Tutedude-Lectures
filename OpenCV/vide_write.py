import cv2

video = cv2.VideoCapture('C:/Users/tiwar/Desktop/flower.mp4')

fourcc = cv2.VideoWriter_fourcc(*'mpv4')
output = cv2.VideoWriter('Output.mp4', fourcc, 30.0, (608,1080))

while video.isOpened():
    ret,frame = video.read()
    if ret:
        output.write(frame)
        cv2.imshow('frame',frame)

        if  cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cv2.destroyAllWindows()