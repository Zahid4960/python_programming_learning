import cv2 as cv

img = cv.imread('F:\Python_Programming_Learning\OpenCV\Data\Photos\cat_large.jpg')

cv.imshow('cat', img)

cv.waitKey(0)
