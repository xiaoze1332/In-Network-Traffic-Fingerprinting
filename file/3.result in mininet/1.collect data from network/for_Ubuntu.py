import os
import pandas as pd
import numpy as np
import pickle

with open('/home/test/Desktop/rf.pickle','rb') as fr:
    rf = pickle.load(fr)

#   eth name
eth = 'ens33'

#   tshark path
tshark_path = 'tshark'

#   eth flow file
test_path = '/home/test/Desktop/test.pcapng'

#   flow size file
size_path = '/home/test/Desktop/size.csv'

#   flow time file
time_path = '/home/test/Desktop/time.csv'

#   output
data_path = '/home/test/Desktop/data.csv'


#   collect 10s data flow from eth
def getPacket():
    cmd = tshark_path + ' -i ' + eth + ' -w ' + test_path + ' -a duration:10'
    os.system(cmd)
    cmd = 'chmod 777 /home/test/Desktop/*'
    os.system(cmd)
    return


#   read size from packet
def read_package_value():
    cmd = tshark_path + ' -r ' + test_path + ' -T fields -e frame.len -E header=n -E separator=, -E quote=n -E occurrence=f > ' + size_path
    os.system(cmd)
    return


#   read time from packet
def read_package_time():
    cmd = tshark_path + ' -r ' + test_path + ' -T fields -e frame.time_delta > ' + time_path
    os.system(cmd)

    return


#####   
# def read_package_size():
#    cmd = 'C:\\"Program Files"\\Wireshark\\tshark.exe -r C:\\Users\\CYQ\\Desktop\\test.pcapng -qz io,stat,0,"COUNT(frame) frame"'
#    os.system(cmd)
#    return


#   
def calculate_package_size():
    global number, mean, std, var, pps

    df = pd.read_csv(size_path, header=None)
    # print(df.iloc[:,[0]])
    # print(df.iloc[:,0])

    # 
    temp = df.iloc[:, 0].to_numpy()

    
    mean = temp.mean()
    std = temp.std()
    var = temp.var()

    # 
    number = np.size(temp, 0)
    # package per second(10s)
    pps = number / 10

    print(mean)
    print(std)
    print(var)
    print(number)
    print(pps)
    return


#   
def calculate_package_time():
    global mean, std, var

    df = pd.read_csv(time_path, header=None)

    # 
    temp = df.iloc[:, 0].to_numpy()

    # 
    mean = temp.mean()
    std = temp.std()
    var = temp.var()

    print(mean)
    print(std)
    print(var)

    return


def do_it():
    getPacket()
    read_package_value()
    calculate_package_size()
    read_package_time()
    calculate_package_time()

    sample = list([[number, pps, mean, std, var, mean, std, var]])

    print(rf.predict_proba(sample).reshape(-1).argmax())
    f=open('/home/test/Desktop/1.txt','w')
    f.write(str(rf.predict_proba(sample).reshape(-1).argmax()))
    f.close()

do_it()
