
###################################################
##  import package
###################################################
import os
import pandas as pd
import numpy as np


#   网卡名称
eth = '\\Device\\NPF_{04156C99-089A-46DA-B65B-85BC13289032}'

#   tshark路径
tshark_path = 'C:\\"Program Files"\\Wireshark\\tshark.exe'

#   网卡流量文件
test_path = 'C:\\Users\\CYQ\\Desktop\\test.pcapng'

#   流量大小文件
size_path = 'C:\\Users\\CYQ\\Desktop\\size.csv'

#   流量时间文件
time_path = 'C:\\Users\\CYQ\\Desktop\\time.csv'


#   将我们计算后的数值输出
data_path = 'C:\\Users\\CYQ\\Desktop\\data.csv'


#   通过tshark对interface的截取10s数据包
def getPacket():
    cmd = tshark_path + ' -i ' + eth  +  ' -w '+ test_path  +' -a duration:10'
    os.system(cmd)
    return

#   读取文件中各个package大小
def read_package_value():
    cmd = tshark_path + ' -r ' + test_path + ' -T fields -e frame.len -E header=n -E separator=, -E quote=n -E occurrence=f > ' +  size_path 
    os.system(cmd)
    return

#   读取pcapng中两个包间隔时间
def read_package_time():
    cmd = tshark_path + ' -r ' +  test_path +   ' -T fields -e frame.time_delta > ' + time_path
    os.system(cmd)

    return
    
#####   读取pcapng中的包数量，已被替代   
#def read_package_size():
#    cmd = 'C:\\"Program Files"\\Wireshark\\tshark.exe -r C:\\Users\\CYQ\\Desktop\\test.pcapng -qz io,stat,0,"COUNT(frame) frame"'
#    os.system(cmd)
#    return
    


#   根据size.csv，计算包大小的平均数，header参数用于设置csv第一行不作为属性。
def calculate_package_size():
    global number,mean,std,var,pps
    
    df = pd.read_csv(size_path,header=None)
    #print(df.iloc[:,[0]])
    #print(df.iloc[:,0])
    
    #将读取的第一列数值，转化为numpy数组
    temp=df.iloc[:,0].to_numpy()
    
    
    #平均数mean，标准差std，方差var
    mean = temp.mean()
    std = temp.std()
    var = temp.var()
    
    #统计这个文件中包含的包数
    number = np.size(temp,0)
    #package per second(10s)
    pps = number/10
    
    
    print(mean)
    print(std)
    print(var)
    print(number)
    print(pps)
    return
    
#   根据time.csv计算对应平均数，方差等
def calculate_package_time():
    global mean,std,var


    df = pd.read_csv(time_path,header=None)
    
    #将读取的第一列数值，转化为numpy数组
    temp=df.iloc[:,0].to_numpy()
    
    #平均数mean，标准差std，方差var
    mean = temp.mean()
    std = temp.std()
    var = temp.var()

    print(mean)
    print(std)
    print(var)

    return





def do_it():
    fo = open(data_path, "w")
    fo.write('Packets,Average pps,Average packet size,std package size,var package size,average time,std package time, var package time\n')

    getPacket()

    read_package_value()
    calculate_package_size()
    s = str(number) +','+ str(pps) +','+ str(mean) +','+ str(std) +','+ str(var)+','
    fo.write(s)

    read_package_time()
    calculate_package_time()
    s = str(mean) +','+ str(std) +','+ str(var) +'\n'
    fo.write(s)

    fo.close()
    return
    
    
do_it()