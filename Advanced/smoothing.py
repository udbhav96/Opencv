
import cv2 as cv

img = cv.imread('P/3.jpg')
cv.imshow('3' , img )


# Averaging
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)
"""
Image Blurring Techniques Summary:

1. Average Blur (cv2.blur or cv2.boxFilter)
   - Replaces each pixel with the average of surrounding pixels.
   - Fast but does NOT preserve edges.
   - Use: Simple smoothing.

2. Median Blur (cv2.medianBlur)
   - Replaces each pixel with the median value of the neighborhood.
   - Great for removing salt-and-pepper noise.
   - Preserves edges better than average blur.

3. Gaussian Blur (cv2.GaussianBlur)
   - Uses a Gaussian kernel (weighted average).
   - Center pixel has highest influence; edge pixels less.
   - Natural-looking blur, but still smooths edges.
   - Use: Preprocessing, noise reduction.

4. Bilateral Blur (cv2.bilateralFilter)
   - Considers both spatial closeness and pixel intensity similarity.
   - Only averages pixels that are close AND similar in value.
   - Preserves edges while smoothing.
   - Slower than others but great for beauty filters, stylization, etc.

Quick Comparison:
-----------------
| Type      | Edge Preservation | Noise Removal | Speed    |
|-----------|-------------------|---------------|----------|
| Average   | ❌                | ✅ Medium     | ✅ Fast  |
| Median    | ✅                | ✅ Strong     | ⚠️ Medium|
| Gaussian  | ❌                | ✅ Good       | ✅ Fast  |
| Bilateral | ✅✅              | ✅ Good       | ❌ Slow  |
"""
