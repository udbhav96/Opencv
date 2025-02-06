import cv2 as cv
img = cv.imread('P/1.jpeg')
cv.imshow('1' , img)
# Converting into greyscale
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
cv.imshow('Gray' , gray)
# Blur
blur = cv.GaussianBlur(img , (3,3) , cv.BORDER_DEFAULT) # Kernel size have to be a odd integer
cv.imshow('Blur' , blur)
# Egde Cascade
canny = cv.Canny(blur , 125 , 175)
cv.imshow('Edge' , canny)
# Dialating the image
dilat = cv.dilate( canny , (3,3) , iterations=100)
cv.imshow('Dilat' , dilat)
# Eroding
eroded = cv.erode(dilat , (3,3) , iterations=100)
cv.imshow('Erod' , eroded)
# Resize
resize  = cv.resize(img , (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resize' , resize)
# Cropping
crop = img[50:200 , 200:400]
cv.imshow('Crop', crop)
cv.waitKey(0)
# Erosion:
# - Erosion works by sliding a kernel (a small matrix) over the image.
# - For each position of the kernel, it replaces the central pixel with the minimum value
#   (in case of binary images, if any pixel under the kernel is 0, the central pixel becomes 0).
# - This operation causes the foreground (usually white) regions to shrink.
# - It is useful for removing small white noises, disconnecting two connected objects,
#   or detaching small unwanted artifacts.
#
# Dilation:
# - Dilation also slides a kernel over the image, but replaces the central pixel with the maximum value.
# - In binary images, if any pixel under the kernel is 1, the central pixel becomes 1.
# - This operation causes the foreground regions to expand or thicken.
# - It is useful for closing small holes, connecting adjacent objects, or emphasizing features.
#
# Key Differences:
# - Effect on Image:
#   * Erosion "shrinks" or thins the foreground (white) regions.
#   * Dilation "grows" or thickens the foreground (white) regions.
#
# - Usage:
#   * Use erosion when you need to remove small noise, separate two touching objects,
#     or reduce the size of the foreground.
#   * Use dilation when you need to enlarge objects, fill in small holes,
#     or connect disjointed parts of the foreground.
#
# - Practical Example:
#   * When processing an image of text, erosion can help remove small isolated dots (noise),
#     while dilation can help make the letters thicker for better visibility.
#
# Note: The operations are often used in combination (like opening and closing) to achieve desired results.
