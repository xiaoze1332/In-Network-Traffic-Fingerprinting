import csv
import pandas as pd


i = 1
mean_val = []
STD = []
VAR = []

while(i < 30):

    location = "C:\\Users\\CYQ\\Desktop\\ftp\\" + str(i) + ".csv"
    df = pd.read_csv(location,header=None)    #第一个参数为文件地址，第二个参数设置没有列名称，也就是no header。
    
    mean_val.append(df.mean())      #将计算的平均数，导入到list
    STD.append(df.std())            #将计算的标准差，导入到list
    VAR.append(df.var())            #将计算的方差，导入到list
    #print(VAR[i-1])
    #print(df.mean())
    i += 1
    if  i==30:
        break

###start to ouput the value###

##mean##
df_mean = pd.DataFrame(mean_val)
#df_mean.head()
loc = "C:\\Users\\CYQ\\Desktop\\ftp\\size\\mean.csv"    #输出平均值到csv文件
df_mean.to_csv(loc,sep=",")

##STD##
df_STD = pd.DataFrame(STD)
#df_mean.head()
loc = "C:\\Users\\CYQ\\Desktop\\ftp\\size\\STD.csv"    #输出平均值到csv文件
df_STD.to_csv(loc,sep=",")

##VAR##
df_VAR = pd.DataFrame(VAR)
#df_mean.head()
loc = "C:\\Users\\CYQ\\Desktop\\ftp\\size\\VAR.csv"    #输出平均值到csv文件
df_VAR.to_csv(loc,sep=",")