import cv2 as cv
'''Usr for changing res of photo , video and live video'''
def rescaleFrame(frame, scale=0.75):
    # Calculate new dimensions based on the scale factor
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    # Create a tuple for dimensions: (width, height)
    dimension = (width, height)
    # Resize the frame using cv.INTER_AREA for downscaling
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

# Open the video file
capture = cv.VideoCapture('V/2.mp4')

while True:
    isTrue, frame = capture.read()
    # Check if a frame was successfully read
    if not isTrue or frame is None:
        print("No frame read, exiting the loop.")
        break

    # Resize the frame using the rescaleFrame function
    frame_resize = rescaleFrame(frame, scale=0.2)
    
    # Display the resized frame
    cv.imshow('V', frame_resize)
    
    # Wait for 20 ms and check if the 'q' key is pressed to quit
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

# Release video capture and close all windows
capture.release()
cv.destroyAllWindows()
'''same with image'''

def changeRes(width,hight):
    '''Only for live video'''
    capture.set(3,width)
    capture.set(4,hight)