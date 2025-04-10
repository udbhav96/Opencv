
import cv2 as cv
import numpy as np

img = cv.imread('P/3.jpg')
cv.imshow('3' , img )

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)
 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)
# ------------------------------------------
# cv2.findContours(image, mode, method)
# ------------------------------------------

# 1. mode → How contours are **retrieved**
# This controls WHICH contours to get and HOW they are organized

# cv2.RETR_EXTERNAL : Retrieves only the outermost contours
# cv2.RETR_LIST     : Retrieves all contours without any hierarchy (flat list)
# cv2.RETR_TREE     : Retrieves all contours and builds a full hierarchy (parent/child)
# cv2.RETR_CCOMP    : Retrieves contours in a two-level hierarchy (external and internal)

# Example:
# Outer shape 🟠 and inner shape ⚪️
# - RETR_EXTERNAL → Only 🟠
# - RETR_LIST     → 🟠 and ⚪️ (no relation)
# - RETR_TREE     → 🟠 is parent, ⚪️ is child
# - RETR_CCOMP    → Two levels: outer and inner

# 2. method → How contours are **approximated**
# This controls HOW MUCH DETAIL to keep in each contour (number of points)

# cv2.CHAIN_APPROX_NONE   : Keeps every boundary point (more detailed, more data)
# cv2.CHAIN_APPROX_SIMPLE : Removes redundant points (simplified shape, e.g., corners only)

# Example:
# Rectangle → CHAIN_APPROX_SIMPLE gives 4 corner points
#          → CHAIN_APPROX_NONE gives all edge pixels

# In summary:
# - mode   = what contours to retrieve and how to organize them
# - method = how simplified or detailed each contour is
