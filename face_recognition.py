# This code is used to detect faces in image and storing them in directory
#import the necessary packages
from imutils.video import VideoStream
import imutils
import time
import cv2
import os
# create a output name directory

#load OpenCV's Haar cascade for face detection from disk
detector = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

#initialize the video stream allow the camera sensor to warm up
print("Starting video stream")
vs = VideoStream(src=0).start()
# time.sleep(2.0)
total=105000 # initialize for counting total number of face

#Now we have to loop over our VideoStream output

while True:
    frame = vs.read()
    origin = frame.copy()
    frame = imutils.resize(frame,width=400)

    #detects faces in the grayscale frame
    reacts = detector.detectMultiScale(cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY), scaleFactor=1.1,
                                        minNeighbors=5, minSize=(30,30))
    # loop over the face detections and draw them on faces
    for (x,y,w,h) in reacts:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("Frame",frame)
    key = cv2.waitKey(1) & 0xFF


    if key ==ord("c"):
        print("key k is pressed")
        p=os.path.sep.join(['./output',"c_{}.png".format(str(total))])
        cv2.imwrite(p,origin)
        total+=1
    elif key == ord("q"):
        print("key q is pesssed")
        break;
        cv2.destroyAllWindows()
print("{} face images stored".format(total))
print("Cleaning up")
cv2.destroyAllWindows()
vs.stop()
