#this code is used to rename the image name to other name from the directory
import imutils
import time
import cv2
import os

dir = os.listdir('./temp')
total = 111000000000
for image_name in  dir:
    # print(image_name)
    origin = cv2.imread('./temp' + '/' + image_name)
    name = image_name.split('.')[0]
    #create directory name output or if you want to do by code you can use if os.path.isdir...
    p=os.path.sep.join(['./output',"Name_{}.jpg".format(str(total).zfill(5))])
    cv2.imwrite(p,origin)
    total+=1
