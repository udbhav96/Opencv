import cv2 as cv
'''Reading Image'''
img = cv.imread('P/1.jpeg')
cv.imshow('1' , img)
cv.waitKey(0) #wait for specific delay or time in millisecond for a key to passed
# Note;- i had a large images bigger than my monitor size then it will go out of screen 
'''Reading Videos'''
capture = cv.VideoCapture('V/2.mp4')
while True:
    isTrue  , frame = capture.read()
    cv.imshow('V' , frame)
    if cv.waitKey(20) and  0xFF==('ord'):
        break
capture.release()
cv.destroyAllWindows
