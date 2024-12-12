import cv2
import os 
### 61
vidcap = cv2.VideoCapture('/home/alam/Downloads/Project_7/siamfc-master/data/Final Results/RGB5.mp4')
result = vidcap.isOpened()
success,image = vidcap.read()
print("result = ", result)
count = 0
os.mkdir("/home/alam/Downloads/Project_7/siamfc-master/data/Final Results/Saved_video5")
while success:
        print('1 Read a new frame: ', success)

        cv2.imwrite("/home/alam/Downloads/Project_7/siamfc-master/data/Final Results/Saved_video5/image_%05d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        print('2 Read a new frame: ', success)
        count += 1

