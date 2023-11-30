import cv2 as cv 

capture_webcam = cv.VideoCapture(0)

def resize_frame(frame, scale=0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

while True:
    is_true, frame = capture_webcam.read()

    cv.imshow('Webcam Video', frame)
    
    resized_frame = resize_frame(frame, 0.25)
    cv.imshow('Resized Webcam Video', resized_frame)

    if cv.waitKey(20) and 0xFF==ord('d'):
        break

capture_webcam.close()
cv.destroyWindowAll()