import cv2 as cv 
import numpy as np
img = cv.imread('P/3.jpg')
cv.imshow('3' , img )
# Translation
def translate(img , x , y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimension = (img.shape[0] , img.shape[1])
    return cv.warpAffine(img , transMat , dimension)
# -x --> Left
# -y --> Up 
# x --> Right
# y --> Down
Translated = translate(img , 100 , 100)
cv.imshow('Translated' , Translated)
# Rotation
def rotate(img , angle , rotPoint=None):
    (height , width )= img.shape[:2]
    if rotPoint is None :
        rotPoint = (width//2,height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)
    return cv.warpAffine(img, rotMat, dimensions)
rotated = rotate(img , 45)
cv.imshow('Rotated' , rotated)
# Resizing 
resize = cv.resize(img , (500,500) , interpolation=cv.INTER_CUBIC) 
cv.imshow('Resize', resize)
#Filpping
flip = cv.flip(img , 0)
cv.imshow('Flip' , flip)
cv.waitKey(0)
