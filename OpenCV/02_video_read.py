import cv2 as cv

video_capture = cv.VideoCapture('F:\Python_Programming_Learning\OpenCV\Data\Videos\dog.mp4')

while True:
    isTrue, frame = video_capture.read()

    cv.imshow('Video', frame)

    if cv.waitKey(20) and 0xFF==ord('d'):
        break

video_capture.release()
cv.destroyAllWindows()