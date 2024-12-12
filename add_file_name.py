import glob
import pandas

files = glob.glob("/home/alam/Downloads/Project_7/siamfc-master/data/VideosTest/RGB10/*")
files.sort()
df=pandas.read_csv('RGB10.csv',sep=',',skiprows=1,header=None)
ind=(df.iloc[:,0]==1)
df.iloc[:,0]=files
df=df[ind]
for i in range(1,5):
    df.iloc[:,i]=df.iloc[:,i].astype(int)

df.iloc[:,3]=df.iloc[:,1]+df.iloc[:,3]
df.iloc[:,4]=df.iloc[:,2]+df.iloc[:,4]



df.to_csv('RGB.csv',header=None,index=False)
############

