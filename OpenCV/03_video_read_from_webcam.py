import cv2 as cv

webcam_capture = cv.VideoCapture(0)

while True:
    is_true, frame = webcam_capture.read()

    cv.imshow('Webcam Video', frame)

    if cv.waitKey(10) and 0xFF==ord('d'):
        break

webcam_capture.release()
cv.destroyWindowAll()