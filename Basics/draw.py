import cv2 as cv
import numpy as np
blank = np.zeros((500,500,3) , dtype = 'uint8') #(hight , width , color channel ) 
cv.imshow('Blank' , blank)
#1. Paint the blank img with diff color
blank[:] = 0 , 0 , 225
cv.imshow('Color' , blank)
#2. Draw  rectangle 
cv.rectangle(blank , (0,0) , (250,250) , (0,255,0) , thickness=2)
cv.imshow('Rect' , blank)
#3. Draw a circle
cv.circle(blank , (blank.shape[1]//2 , blank.shape[0]//2) , 40 , (0,255,0) , thickness=-1)
cv.imshow('Circle' , blank)
#4. Draw a line
cv.line(blank , (0,0) , (250 , 250) , (0,250,0), thickness=2)
cv.imshow('Line' , blank)
#5. Write text
cv.putText(blank , 'Hello' , (225 , 225) , cv.FONT_HERSHEY_TRIPLEX  , 1.0 , (0,225,0), 2)
cv.imshow('Text' , blank)

cv.waitKey(0)