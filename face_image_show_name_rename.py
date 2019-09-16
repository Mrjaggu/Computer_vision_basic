#this code is used to show image form folder by observing iamge than saving it into directory
import os
import cv2
import imutils

image_path = './output/'

img_dir = os.listdir(image_path)
destination_path = ''
cnt = 1000000000
for image_name in img_dir:
    image = cv2.imread('./output/' + image_name)
    image = imutils.resize(image,width=400)
    cv2.imshow("Image",image)
    key = cv2.waitKey(0) & 0xFF

    if key ==ord("c"):
        print("key c is pressed")
        p=os.path.sep.join(['./output1',"c_{}.png".format(str(cnt))])
        cv2.imwrite(p,image)
        cnt+=1

    elif key ==ord('p'):
        print('pass is pressed')
        pass;
    elif key == ord("q"):
        print("key q is pesssed")
        break;
        cv2.destroyAllWindows()

print("{} face images stored".format(cnt))
print("Cleaning up")
cv2.destroyAllWindows()
