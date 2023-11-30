import cv2 as cv 

image = cv.imread('./Data/Photos/cat.jpg')

def re_size_image(image, scale=0.5):
    width = int(image.shape[1] * scale)
    height = int(image.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(image, dimensions, interpolation=cv.INTER_AREA)

cv.imshow('Cat', image)

resized_image = re_size_image(image, 0.75)
cv.imshow('Resize Image', resized_image)

cv.waitKey(0)