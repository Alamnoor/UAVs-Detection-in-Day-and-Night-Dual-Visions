# UAVs-Detection-in-Day-and-Night-Dual-Visions
## How to Prepare the Custom dataset:

a) Convert videos to frames by using the python script file with name and location:
convert_to_frames_copy.py

b) Convert Json to csv for all video each and individuality by using:
json_to_csv.py or Json_to_csv30t.py or Json_to_csv_test.py

c) Add file name/path_to_frames to csv file for each video by using:
add_file_nameCopy.py or add_file_name_copy.py or add_file_name.py

d) Create a Drone.csv file with data of :
Drone 0 (Drone and 0 should be in row)

e) Each video frames folder should have a folder of that video with csv file Like:
.../data/VideosIRTest/IR1/Label/IR1.csv
The folder Label also have IR.csv file but it is before preprocessed and IR1 after preprocessed. So every video have same files likes IR1 folder with subfolder of Label/ IR* .csv or RGB*.csv file.

f) The folder name with VideosIR and VideosRGBTrain are the training folder for the training data
and .../data
While
VideosIRTest and VideosTest are the testing folder for the testing data and should be located in the: .../data

g) A single file of csv for the training of both RGB+IR should be located:
.../data/IR-RGBTrain.csv and for testing is:
.../data/IR-RGBTest.csv
## Training with EfficientDet
Using the following Script for the training:
python train.py --snapshot imagenet --phi 4 --gpu 0 --random-transform --compute-val-loss --freeze-backbone --batch-size 8 --steps 100 --epochs 600  csv {path to}/data/IR-RGBTrain.csv {path to}/data/Drone.csv --val-annotations-path {path to}/data/IR-RGBTest.csv

Note: Where –phi 4 indicates the EfficientDet-4 and need to be change with the GPU memory and --batch-size 8 also part of the gpu memory.	 
