# this code uses mtcnn library to detect faces from images and than writing it into directory
from mtcnn.mtcnn import MTCNN
import cv2
import os


image_path = os.listdir('./data')
destination_path = '/final'
face_detector = MTCNN()

for image_file in image_path:
    image_name=image_file.split('.')[0]
    img = cv2.imread('./data' + '/' + image_file)
    detect_boxes = face_detector.detect_faces(img)

    for i in range(len(detect_boxes)):
        face_img = img[detect_boxes[i]["box"][1]:detect_boxes[i]["box"][1] + detect_boxes[i]["box"][3], detect_boxes[i]["box"][0]:detect_boxes[i]["box"][0] + detect_boxes[i]["box"][2]]
        # cv2.imwrite(destination_path + '/' + image_name + ".jpg", face_img)
        cv2.imshow('image',face_img)

    for box in detect_boxes:
        pt1 = (box["box"][0], box["box"][1]) # top left
        pt2 = (box["box"][0] + box["box"][2], box["box"][1] + box["box"][3]) # bottom right
        cv2.rectangle(img, pt1, pt2, (0,255,0), 2)
    cv2.imwrite(destination_path +'/'+ "detected-boxes.jpg", img)

print("{} face images stored".format(cnt))
print("Cleaning up")
cv2.destroyAllWindows()
