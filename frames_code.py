

import cv2
import os
########### 1 to unward 
###### 1
vidcap = cv2.VideoCapture('/home/alam/Downloads/Project_7/siamfc-master/data/test-dev/20190925_101846_1_7/RGB.mp4')
result = vidcap.isOpened()
success,image = vidcap.read()
print("result = ", result)
count = 0
os.mkdir("/home/alam/Downloads/Project_7/siamfc-master/data/VideosTest/RGB1")
while success:
        print('1 Read a new frame: ', success)

        cv2.imwrite("/home/alam/Downloads/Project_7/siamfc-master/data/VideosTest/RGB1/image_%05d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        print('2 Read a new frame: ', success)
        count += 1
######### 2
vidcap = cv2.VideoCapture('/home/alam/Downloads/Project_7/siamfc-master/data/test-dev/20190925_101846_1_8/RGB.mp4')
result = vidcap.isOpened()
success,image = vidcap.read()
print("result = ", result)
count = 0
os.mkdir("/home/alam/Downloads/Project_7/siamfc-master/data/VideosTest/RGB2")
while success:
        print('1 Read a new frame: ', success)

        cv2.imwrite("/home/alam/Downloads/Project_7/siamfc-master/data/VideosTest/RGB2/image_%05d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        print('2 Read a new frame: ', success)
        count += 1

#### 3
vidcap = cv2.VideoCapture('/home/alam/Downloads/Project_7/siamfc-master/data/test-dev/20190925_130434_1_4/RGB.mp4')
result = vidcap.isOpened()
success,image = vidcap.read()
print("result = ", result)
count = 0
os.mkdir("/home/alam/Downloads/Project_7/siamfc-master/data/VideosTest/RGB3")
while success:
        print('1 Read a new frame: ', success)

        cv2.imwrite("/home/alam/Downloads/Project_7/siamfc-master/data/VideosTest/RGB3/image_%05d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        print('2 Read a new frame: ', success)
        count += 1
##### 4
vidcap = cv2.VideoCapture('/home/alam/Downloads/Project_7/siamfc-master/data/test-dev/20190925_130434_1_7/RGB.mp4')
result = vidcap.isOpened()
success,image = vidcap.read()
print("result = ", result)
count = 0
os.mkdir("/home/alam/Downloads/Project_7/siamfc-master/data/VideosTest/RGB4")
while success:
        print('1 Read a new frame: ', success)

        cv2.imwrite("/home/alam/Downloads/Project_7/siamfc-master/data/VideosTest/RGB4/image_%05d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        print('2 Read a new frame: ', success)
        count += 1



#####  5
vidcap = cv2.VideoCapture('/home/alam/Downloads/Project_7/siamfc-master/data/test-dev/20190925_130434_1_9/RGB.mp4')
result = vidcap.isOpened()
success,image = vidcap.read()
print("result = ", result)
count = 0
os.mkdir("/home/alam/Downloads/Project_7/siamfc-master/data/VideosTest/RGB5")
while success:
        print('1 Read a new frame: ', success)

        cv2.imwrite("/home/alam/Downloads/Project_7/siamfc-master/data/VideosTest/RGB5/image_%05d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        print('2 Read a new frame: ', success)
        count += 1        

######## 
####### 6

vidcap = cv2.VideoCapture('/home/alam/Downloads/Project_7/siamfc-master/data/test-dev/20190925_131530_1_1/RGB.mp4')
result = vidcap.isOpened()
success,image = vidcap.read()
print("result = ", result)
count = 0
os.mkdir("/home/alam/Downloads/Project_7/siamfc-master/data/VideosTest/RGB6")
while success:
        print('1 Read a new frame: ', success)

        cv2.imwrite("/home/alam/Downloads/Project_7/siamfc-master/data/VideosTest/RGB6/image_%05d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        print('2 Read a new frame: ', success)
        count += 1
######### 7
vidcap = cv2.VideoCapture('/home/alam/Downloads/Project_7/siamfc-master/data/test-dev/20190925_131530_1_4/RGB.mp4')
result = vidcap.isOpened()
success,image = vidcap.read()
print("result = ", result)
count = 0
os.mkdir("/home/alam/Downloads/Project_7/siamfc-master/data/VideosTest/RGB7")
while success:
        print('1 Read a new frame: ', success)

        cv2.imwrite("/home/alam/Downloads/Project_7/siamfc-master/data/VideosTest/RGB7/image_%05d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        print('2 Read a new frame: ', success)
        count += 1

#### 8
vidcap = cv2.VideoCapture('/home/alam/Downloads/Project_7/siamfc-master/data/test-dev/20190925_131530_1_5/RGB.mp4')
result = vidcap.isOpened()
success,image = vidcap.read()
print("result = ", result)
count = 0
os.mkdir("/home/alam/Downloads/Project_7/siamfc-master/data/VideosTest/RGB8")
while success:
        print('1 Read a new frame: ', success)

        cv2.imwrite("/home/alam/Downloads/Project_7/siamfc-master/data/VideosTest/RGB8/image_%05d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        print('2 Read a new frame: ', success)
        count += 1
