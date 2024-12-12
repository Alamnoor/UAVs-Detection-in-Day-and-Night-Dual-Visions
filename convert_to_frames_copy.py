import cv2
import os 
### 61
vidcap = cv2.VideoCapture('/home/alam/Downloads/Project_7/siamfc-master/data/test-dev/20190926_142435_1_3/IR.mp4')
result = vidcap.isOpened()
success,image = vidcap.read()
print("result = ", result)
count = 0
os.mkdir("/home/alam/Downloads/Project_7/siamfc-master/data/VideosIR/IR61")
while success:
        print('1 Read a new frame: ', success)

        cv2.imwrite("/home/alam/Downloads/Project_7/siamfc-master/data/VideosIR/IR61/image_%05d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        print('2 Read a new frame: ', success)
        count += 1
######### 62
vidcap = cv2.VideoCapture('/home/alam/Downloads/Project_7/siamfc-master/data/test-dev/20190926_142435_1_4/IR.mp4')
result = vidcap.isOpened()
success,image = vidcap.read()
print("result = ", result)
count = 0
os.mkdir("/home/alam/Downloads/Project_7/siamfc-master/data/VideosIR/IR62")
while success:
        print('1 Read a new frame: ', success)

        cv2.imwrite("/home/alam/Downloads/Project_7/siamfc-master/data/VideosIR/IR62/image_%05d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        print('2 Read a new frame: ', success)
        count += 1

#### 63
vidcap = cv2.VideoCapture('/home/alam/Downloads/Project_7/siamfc-master/data/test-dev/20190926_142435_1_5/IR.mp4')
result = vidcap.isOpened()
success,image = vidcap.read()
print("result = ", result)
count = 0
os.mkdir("/home/alam/Downloads/Project_7/siamfc-master/data/VideosIR/IR63")
while success:
        print('1 Read a new frame: ', success)

        cv2.imwrite("/home/alam/Downloads/Project_7/siamfc-master/data/VideosIR/IR63/image_%05d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        print('2 Read a new frame: ', success)
        count += 1
##### 64
vidcap = cv2.VideoCapture('/home/alam/Downloads/Project_7/siamfc-master/data/test-dev/20190926_142435_1_7/IR.mp4')
result = vidcap.isOpened()
success,image = vidcap.read()
print("result = ", result)
count = 0
os.mkdir("/home/alam/Downloads/Project_7/siamfc-master/data/VideosIR/IR64")
while success:
        print('1 Read a new frame: ', success)

        cv2.imwrite("/home/alam/Downloads/Project_7/siamfc-master/data/VideosIR/IR64/image_%05d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        print('2 Read a new frame: ', success)
        count += 1



#####  65
vidcap = cv2.VideoCapture('/home/alam/Downloads/Project_7/siamfc-master/data/test-dev/20190926_142435_1_8/IR.mp4')
result = vidcap.isOpened()
success,image = vidcap.read()
print("result = ", result)
count = 0
os.mkdir("/home/alam/Downloads/Project_7/siamfc-master/data/VideosIR/IR65")
while success:
        print('1 Read a new frame: ', success)

        cv2.imwrite("/home/alam/Downloads/Project_7/siamfc-master/data/VideosIR/IR65/image_%05d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        print('2 Read a new frame: ', success)
        count += 1        

######## 
####### 66

vidcap = cv2.VideoCapture('/home/alam/Downloads/Project_7/siamfc-master/data/test-dev/20190926_143632_1_5/IR.mp4')
result = vidcap.isOpened()
success,image = vidcap.read()
print("result = ", result)
count = 0
os.mkdir("/home/alam/Downloads/Project_7/siamfc-master/data/VideosIR/IR66")
while success:
        print('1 Read a new frame: ', success)

        cv2.imwrite("/home/alam/Downloads/Project_7/siamfc-master/data/VideosIR/IR66/image_%05d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        print('2 Read a new frame: ', success)
        count += 1
######### 67
vidcap = cv2.VideoCapture('/home/alam/Downloads/Project_7/siamfc-master/data/test-dev/20190926_143632_1_6/IR.mp4')
result = vidcap.isOpened()
success,image = vidcap.read()
print("result = ", result)
count = 0
os.mkdir("/home/alam/Downloads/Project_7/siamfc-master/data/VideosIR/IR67")
while success:
        print('1 Read a new frame: ', success)

        cv2.imwrite("/home/alam/Downloads/Project_7/siamfc-master/data/VideosIR/IR67/image_%05d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        print('2 Read a new frame: ', success)
        count += 1

#### 68
vidcap = cv2.VideoCapture('/home/alam/Downloads/Project_7/siamfc-master/data/test-dev/20190926_143632_1_7/IR.mp4')
result = vidcap.isOpened()
success,image = vidcap.read()
print("result = ", result)
count = 0
os.mkdir("/home/alam/Downloads/Project_7/siamfc-master/data/VideosIR/IR68")
while success:
        print('1 Read a new frame: ', success)

        cv2.imwrite("/home/alam/Downloads/Project_7/siamfc-master/data/VideosIR/IR68/image_%05d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        print('2 Read a new frame: ', success)
        count += 1
##### 69
vidcap = cv2.VideoCapture('/home/alam/Downloads/Project_7/siamfc-master/data/test-dev/20190926_144550_1_2/IR.mp4')
result = vidcap.isOpened()
success,image = vidcap.read()
print("result = ", result)
count = 0
os.mkdir("/home/alam/Downloads/Project_7/siamfc-master/data/VideosIR/IR69")
while success:
        print('1 Read a new frame: ', success)

        cv2.imwrite("/home/alam/Downloads/Project_7/siamfc-master/data/VideosIR/IR69/image_%05d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        print('2 Read a new frame: ', success)
        count += 1



#####  70
vidcap = cv2.VideoCapture('/home/alam/Downloads/Project_7/siamfc-master/data/test-dev/20190926_144550_1_3/IR.mp4')
result = vidcap.isOpened()
success,image = vidcap.read()
print("result = ", result)
count = 0
os.mkdir("/home/alam/Downloads/Project_7/siamfc-master/data/VideosIR/IR70")
while success:
        print('1 Read a new frame: ', success)

        cv2.imwrite("/home/alam/Downloads/Project_7/siamfc-master/data/VideosIR/IR70/image_%05d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        print('2 Read a new frame: ', success)
        count += 1   


########### 71 to unward 
###### 71
vidcap = cv2.VideoCapture('/home/alam/Downloads/Project_7/siamfc-master/data/test-dev/20190926_144550_1_5/IR.mp4')
result = vidcap.isOpened()
success,image = vidcap.read()
print("result = ", result)
count = 0
os.mkdir("/home/alam/Downloads/Project_7/siamfc-master/data/VideosIR/IR71")
while success:
        print('1 Read a new frame: ', success)

        cv2.imwrite("/home/alam/Downloads/Project_7/siamfc-master/data/VideosIR/IR71/image_%05d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        print('2 Read a new frame: ', success)
        count += 1
######### 72
vidcap = cv2.VideoCapture('/home/alam/Downloads/Project_7/siamfc-master/data/test-dev/20190926_144550_1_8/IR.mp4')
result = vidcap.isOpened()
success,image = vidcap.read()
print("result = ", result)
count = 0
os.mkdir("/home/alam/Downloads/Project_7/siamfc-master/data/VideosIR/IR72")
while success:
        print('1 Read a new frame: ', success)

        cv2.imwrite("/home/alam/Downloads/Project_7/siamfc-master/data/VideosIR/IR72/image_%05d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        print('2 Read a new frame: ', success)
        count += 1

#### 73
vidcap = cv2.VideoCapture('/home/alam/Downloads/Project_7/siamfc-master/data/test-dev/20190926_144550_1_9/IR.mp4')
result = vidcap.isOpened()
success,image = vidcap.read()
print("result = ", result)
count = 0
os.mkdir("/home/alam/Downloads/Project_7/siamfc-master/data/VideosIR/IR73")
while success:
        print('1 Read a new frame: ', success)

        cv2.imwrite("/home/alam/Downloads/Project_7/siamfc-master/data/VideosIR/IR73/image_%05d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        print('2 Read a new frame: ', success)
        count += 1
##### 74
vidcap = cv2.VideoCapture('/home/alam/Downloads/Project_7/siamfc-master/data/test-dev/20190926_183400_1_3/IR.mp4')
result = vidcap.isOpened()
success,image = vidcap.read()
print("result = ", result)
count = 0
os.mkdir("/home/alam/Downloads/Project_7/siamfc-master/data/VideosIR/IR74")
while success:
        print('1 Read a new frame: ', success)

        cv2.imwrite("/home/alam/Downloads/Project_7/siamfc-master/data/VideosIR/IR74/image_%05d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        print('2 Read a new frame: ', success)
        count += 1



#####  75
import os 
vidcap = cv2.VideoCapture('/home/alam/Downloads/Project_7/siamfc-master/data/test-dev/20190926_183400_1_5/IR.mp4')
result = vidcap.isOpened()
success,image = vidcap.read()
print("result = ", result)
count = 0
os.mkdir("/home/alam/Downloads/Project_7/siamfc-master/data/VideosIR/IR75")
while success:
        print('1 Read a new frame: ', success)

        cv2.imwrite("/home/alam/Downloads/Project_7/siamfc-master/data/VideosIR/IR75/image_%05d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        print('2 Read a new frame: ', success)
        count += 1          

######## 
####### 76

vidcap = cv2.VideoCapture('/home/alam/Downloads/Project_7/siamfc-master/data/test-dev/20190926_183400_1_8/IR.mp4')
result = vidcap.isOpened()
success,image = vidcap.read()
print("result = ", result)
count = 0
os.mkdir("/home/alam/Downloads/Project_7/siamfc-master/data/VideosIR/IR76")
while success:
        print('1 Read a new frame: ', success)

        cv2.imwrite("/home/alam/Downloads/Project_7/siamfc-master/data/VideosIR/IR76/image_%05d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        print('2 Read a new frame: ', success)
        count += 1
######### 77
vidcap = cv2.VideoCapture('/home/alam/Downloads/Project_7/siamfc-master/data/test-dev/20190926_183400_1_9/IR.mp4')
result = vidcap.isOpened()
success,image = vidcap.read()
print("result = ", result)
count = 0
os.mkdir("/home/alam/Downloads/Project_7/siamfc-master/data/VideosIR/IR77")
while success:
        print('1 Read a new frame: ', success)

        cv2.imwrite("/home/alam/Downloads/Project_7/siamfc-master/data/VideosIR/IR77/image_%05d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        print('2 Read a new frame: ', success)
        count += 1

#### 78
vidcap = cv2.VideoCapture('/home/alam/Downloads/Project_7/siamfc-master/data/test-dev/20190926_183941_1_2/IR.mp4')
result = vidcap.isOpened()
success,image = vidcap.read()
print("result = ", result)
count = 0
os.mkdir("/home/alam/Downloads/Project_7/siamfc-master/data/VideosIR/IR78")
while success:
        print('1 Read a new frame: ', success)

        cv2.imwrite("/home/alam/Downloads/Project_7/siamfc-master/data/VideosIR/IR78/image_%05d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        print('2 Read a new frame: ', success)
        count += 1
##### 79
vidcap = cv2.VideoCapture('/home/alam/Downloads/Project_7/siamfc-master/data/test-dev/20190926_183941_1_4/IR.mp4')
result = vidcap.isOpened()
success,image = vidcap.read()
print("result = ", result)
count = 0
os.mkdir("/home/alam/Downloads/Project_7/siamfc-master/data/VideosIR/IR79")
while success:
        print('1 Read a new frame: ', success)

        cv2.imwrite("/home/alam/Downloads/Project_7/siamfc-master/data/VideosIR/IR79/image_%05d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        print('2 Read a new frame: ', success)
        count += 1



#####  80
vidcap = cv2.VideoCapture('/home/alam/Downloads/Project_7/siamfc-master/data/test-dev/20190926_183941_1_6/IR.mp4')
result = vidcap.isOpened()
success,image = vidcap.read()
print("result = ", result)
count = 0
os.mkdir("/home/alam/Downloads/Project_7/siamfc-master/data/VideosIR/IR80")
while success:
        print('1 Read a new frame: ', success)

        cv2.imwrite("/home/alam/Downloads/Project_7/siamfc-master/data/VideosIR/IR80/image_%05d.jpg" % count, image)     # save frame as JPEG file      
        success,image = vidcap.read()
        print('2 Read a new frame: ', success)
        count += 1   
