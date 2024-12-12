import pandas as pd
df = pd.read_json (r'/home/alam/Downloads/Project_7/siamfc-master/data/test-dev/20190925_131530_1_7/RGB_label.json')
export_csv = df.to_csv (r'/home/alam/Downloads/Project_7/siamfc-master/data/Videos/RGB1/Label/RGB1.csv', index = None, header=True)

#### 2
df = pd.read_json (r'/home/alam/Downloads/Project_7/siamfc-master/data/test-dev/20190925_133630_1_1/RGB_label.json')
export_csv = df.to_csv (r'/home/alam/Downloads/Project_7/siamfc-master/data/Videos/RGB2/Label/RGB2.csv', index = None, header=True)

####### 3
df = pd.read_json (r'/home/alam/Downloads/Project_7/siamfc-master/data/test-dev/20190925_133630_1_2/RGB_label.json')
export_csv = df.to_csv (r'/home/alam/Downloads/Project_7/siamfc-master/data/Videos/RGB3/Label/RGB3.csv', index = None, header=True)

####### 4
df = pd.read_json (r'/home/alam/Downloads/Project_7/siamfc-master/data/test-dev/20190925_133630_1_3/RGB_label.json')
export_csv = df.to_csv (r'/home/alam/Downloads/Project_7/siamfc-master/data/Videos/RGB4/Label/RGB4.csv', index = None, header=True)
####### 5

df = pd.read_json (r'/home/alam/Downloads/Project_7/siamfc-master/data/test-dev/20190925_133630_1_4/RGB_label.json')
export_csv = df.to_csv (r'/home/alam/Downloads/Project_7/siamfc-master/data/Videos/RGB5/Label/RGB5.csv', index = None, header=True)

########  6
df = pd.read_json (r'/home/alam/Downloads/Project_7/siamfc-master/data/test-dev/20190925_133630_1_7/RGB_label.json')
export_csv = df.to_csv (r'/home/alam/Downloads/Project_7/siamfc-master/data/Videos/RGB6/Label/RGB6.csv', index = None, header=True)

####### 7
df = pd.read_json (r'/home/alam/Downloads/Project_7/siamfc-master/data/test-dev/20190925_133630_1_8/RGB_label.json')
export_csv = df.to_csv (r'/home/alam/Downloads/Project_7/siamfc-master/data/Videos/RGB7/Label/RGB7.csv', index = None, header=True)

####### 8
df = pd.read_json (r'/home/alam/Downloads/Project_7/siamfc-master/data/test-dev/20190925_140917_1_2/RGB_label.json')
export_csv = df.to_csv (r'/home/alam/Downloads/Project_7/siamfc-master/data/Videos/RGB8/Label/RGB8.csv', index = None, header=True)

######## 9
df = pd.read_json (r'/home/alam/Downloads/Project_7/siamfc-master/data/test-dev/20190925_140917_1_4/RGB_label.json')
export_csv = df.to_csv (r'/home/alam/Downloads/Project_7/siamfc-master/data/Videos/RGB9/Label/RGB9.csv', index = None, header=True)

####### 10
df = pd.read_json (r'/home/alam/Downloads/Project_7/siamfc-master/data/test-dev/20190925_140917_1_5/RGB_label.json')
export_csv = df.to_csv (r'/home/alam/Downloads/Project_7/siamfc-master/data/Videos/RGB10/Label/RGB10.csv', index = None, header=True)
 
