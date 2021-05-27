import os

i = 1;
while(i<30):
    cmd = 'C:\\Users\\CYQ\\Desktop\\wireshark\\tshark.exe -r C:\\Users\\CYQ\\Desktop\\ftp\\'+ str(i) + '.pcapng -T fields -e frame.len -E header=n -E separator=, -E quote=n -E occurrence=f > C:\\Users\\CYQ\\Desktop\\ftp\\' + str(i) + '.csv'
     
    os.system(cmd)
    
    
    ##print(cmd)
    i=i+1
