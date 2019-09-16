# this code is used to read images from multiple folders and saving it new single directory
import os
import cv2
import imutils

folder_path = os.listdir('./lfw/')
cnt=0
for image_folder in folder_path:
    print(image_folder)
    for image_file in os.listdir('./lfw/' + image_folder + '/'):
        print(image_file)
        image_read = './lfw/' + image_folder + '/' + image_file
        print(image_read)
        image = cv2.imread(image_read)
        image = imutils.resize(image,width=400)
        cv2.imshow("Image",image)
        key = cv2.waitKey(0) & 0xFF

        if key ==ord("c"):
            print("key k is pressed")
            p=os.path.sep.join(['./output',"c_{}.png".format(str(cnt))])
            cv2.imwrite(p,image)
            cnt+=1

        elif key == ord("q"):
            print("key q is pesssed")
            break;
            cv2.destroyAllWindows()

    print("{} face images stored".format(cnt))
    print("Cleaning up")
    cv2.destroyAllWindows()
