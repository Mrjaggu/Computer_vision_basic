from imutils  import face_utils
import numpy as np
import imutils
import dlib
import cv2
import os

detector = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
image_path = os.listdir('./data')

destination_path = './final'
for image_file in image_path:
    print(image_file)
    image_name=image_file.split('.')[0]
    img = cv2.imread('./data' + '/' + image_file)
    image = imutils.resize(img,width=400)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        face_clip = img[y:y+h, x:x+w]  #cropping the face in image
        cv2.resize(face_clip, (224, 224))
        cv2.imwrite( destination_path + '/' + image_name + ".jpg", face_clip)
