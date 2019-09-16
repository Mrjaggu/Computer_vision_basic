#This code is used to detect facial features i.e 69 facial landmark
from imutils  import face_utils
import numpy as np
import imutils
import dlib
import cv2

def rect_to_bb(rect):
    #take a bounding predicted by dlib and convert it
    #to the format (x,y,w,h) as we would normally do
    # with OpenCV
    x= rect.left()
    y=  rect.top()
    w= rect.right() - x
    h = rect.bottom() - y

    #return a tuple of (x,y,w,h)
    return (x,y,w,h)

def shape_to_np(shape,dtype = 'int'):
    #initialize the list of (x,y)-co-ordinate
    coords = np.zeros((68,2),dtype = dtype)

    #loop over the 68 facial landmark and convert them
    #to a 2-tuple of (x,y)-coordinates
    for i in range(0,68):
        coords[i]=(shape.part(i).x , shape.part(i).y)

        #return the list of (x,y)-coordinates
        return coords


#initialize dlib's face detector (HOG) based and then create
# the facial landmark predictor

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('./shape_predictor_68_face_landmarks.dat')


#load the input image , resize it and convert it to graysacle
image = cv2.imread('./iamge.png')
image = imutils.resize(image,width=400)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#detects faces in the grayscale image
rects = detector(gray , 1) # detects the bounding box in our images
print("rects",rects)
#loop over the face detections
for (i,rect) in enumerate(rects):
    shape = predictor(gray,rect)
    shape = face_utils.shape_to_np(shape)
	# convert dlib's rectangle to a OpenCV-style bounding box
	# [i.e., (x, y, w, h)], then draw the face bounding box
    (x, y, w, h) = face_utils.rect_to_bb(rect)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

	# show the face number
    cv2.putText(image, "Face #{}".format(i + 1), (x - 10, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

	# loop over the (x, y)-coordinates for the facial landmarks
	# and draw them on the image
    for (x, y) in shape:
	       cv2.circle(image, (x, y), 1, (0, 0, 255), -1)

#show the output
cv2.imshow("Output", image)
cv2.waitKey(0)
