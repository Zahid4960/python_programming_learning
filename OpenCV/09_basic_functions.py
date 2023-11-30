import cv2 as cv

img = cv.imread('./Data/Photos/park.jpg')
cv.imshow('Cat', img)

# conver to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# blur
blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# edge cascade
edge = cv.Canny(blur, 125, 175)
cv.imshow('Edge', edge)

# Dilate
dilate = cv.dilate(edge, (5, 5), iterations=5)
cv.imshow('Dilate', dilate)

# erode
erode = cv.erode(dilate, (5, 5), iterations=5)
cv.imshow('erode', erode)

# crop
crop = img[20:100, 100:300]
cv.imshow('Crop', crop)

# Resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)

cv.waitKey(0)