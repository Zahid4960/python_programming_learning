import cv2 as cv
import numpy as np

image = cv.imread('./Data/Photos/cat.jpg')
cv.imshow('Cat', image)

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# paint the image in a certain color
# blank[:] = 0, 0, 255 # for all the pixels
# blank[100:300, 100:400] = 0, 0, 255
# cv.imshow('Red', blank)

# draw a rectangle
# cv.rectangle(blank, (0,0), (250, 250), (0, 255, 0), thickness=2) # create green color border
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness=cv.FILLED) # fill teh green rectangle.
cv.imshow('Rectangle', blank)

# draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 50, (0,0,255), thickness=cv.FILLED)
cv.imshow('Circle', blank)

# draw a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (250,0,0), thickness=2)
cv.imshow('Line', blank)

cv.waitKey(0)