import cv2 as cv 

capture_video = cv.VideoCapture('./Data/Videos/dog.mp4')

def resize_frame(frame, scale=0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

while True:
    is_true, frame = capture_video.read()

    cv.imshow('Dog Video', frame)
    
    resized_frame = resize_frame(frame, 0.25)
    cv.imshow('Resized Dog Video', resized_frame)

    if cv.waitKey(20) and 0xFF==ord('d'):
        break

capture_video.close()
cv.destroyWindowAll()