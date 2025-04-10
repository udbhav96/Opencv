"""
detectMultiScale Parameters:

- scaleFactor=1.1:
  Controls how much image size is reduced at each scale.
  Smaller = better accuracy, more time. Larger = faster, less accurate.

- minNeighbors=1:
  Sets how many nearby rectangles (detections) are needed to confirm a face.
  Higher = fewer false positives, lower = may detect noise as faces.
"""

import cv2 as cv

img = cv.imread('P/lady.jpg')
cv.imshow('lady' , img )


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray People', gray)

haar_cascade = cv.CascadeClassifier('/home/udbhav-purwar/Documents/Project/Opencv/Faces/haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Faces', img)



cv.waitKey(0)