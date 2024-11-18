"""
Step By Step Process
1. resizing the frame of the video
2. finding the color of the object using HSV (Hue, Saturation, Value)
3. after finding the color, use openCV's cv2.inRange() to create a mask:
The mask highlights all pixels within the specified HSV range
4. After creating a mask in HSV, subsequent operations like contour detection (Object detection)
and edge detection become more focused and acurate
5. After that, we use the rectangle() to make a rectangle surrounding the contour/object that we detected 
"""

import cv2
import numpy as np

# Function to rescale frame
def rescaleFrame(frame, scale=0.75): # the video width and height will be resized to be 75% of its original
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

# Open a video
cap = cv2.VideoCapture("Resources/object_video.mp4")    

def findColors(resized_frame):
    # Converting the frame into HSV
    imgHSV = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2HSV)

    # Define the bounds for the HSV image for the object color red
    lower_bound = np.array([167,235,168]) # Adjusted based on the target color
    upper_bound = np.array([179,255,255])
    # We get this bounding area from the colorPicker program
    
    # Create the mask to get the frame that is inside the range lower_bound and upper_bound into white pixel and other than that into black pixel
    return cv2.inRange(imgHSV, lower_bound, upper_bound)

def getContours(mask):
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 500: # This will filter out the small contours
            # This will get the bounding rectangle
            x, y, w, h = cv2.boundingRect(contour)

            # This will draw a bounding rectangle of the object on the original frame
            cv2.rectangle(resized_frame, (x,y), (x+w, y+h), (0,255,0), 2)


while True:
    # Reading each frame of the video
    success, frame = cap.read()
    # Break upon encountering unsuccessful frame reading
    if not success:
        print("End of video or cannot read video file")
        break
    
    # Resizing the frame
    resized_frame = rescaleFrame(frame)

    # This will just make the mask for the object we want to detect
    mask = findColors(resized_frame)

    # This will call the getContours function to make a rectangle around the object
    getContours(mask)

    # Show the frame
    cv2.imshow("Object Detection", resized_frame)

    # Upon clicking "q" the video will stop and will break out of loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows