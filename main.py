# import cv2

# cap = cv2.VideoCapture("Resources/object_video.mp4")   # This block of code will show a video and will only stop when the user press 'q'

# def getContours(img, imgContour):
#     contours,hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) # --> It retrieves th extreme outer contours
#     for cnt in contours:
#         area = cv2.contourArea(cnt)
#         print(area)
#         if (area > 500) :
#             cv2.drawContours(imgContour, cnt, -1, (0,0,255), 3)
#             peri = cv2.arcLength(cnt, True)
#             print(peri)
#             approx = cv2.approxPolyDP(cnt,0.05*peri, True)
#             print(approx)
#             objCor = len(approx)
#             x, y, w, h = cv2.boundingRect(approx)

#             cv2.rectangle(imgContour, (x,y), (x+w, y+h), (0,255,0), 2)

# while True:
#     success, img = cap.read()
#     if not success:
#         print("End of video or cannot read video file")
#         break
#     lower = np.array([h_min, s_min, v_min])
#     imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#     mask = cv2.inRange(imgHSV)
#     imgCanny = cv2.Canny(imgHSV, 50, 150)
    

#     getContours(imgCanny, imgContour)

#     cv2.imshow("Object detection", imgContour)
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows

import cv2
import numpy as np

cap = cv2.VideoCapture("Resources/object_video.mp4")

def rescaleFrame(frame, scale=0.75): # the video width and height will be resized to be 75% of its original
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

while True:
    success, frame = cap.read()

    frame_resized = rescaleFrame(frame)

    cv2.imshow("Object Detection", frame_resized)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows

