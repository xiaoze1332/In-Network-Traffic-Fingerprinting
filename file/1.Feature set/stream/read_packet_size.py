import os

i = 0;
while(i<30):
    cmd = 'C:\\Users\\CYQ\\Desktop\\wireshark\\tshark.exe -r C:\\Users\\CYQ\\Desktop\\stream\\'+ str(i) + '.pcapng -T fields -e frame.len -E header=n -E separator=, -E quote=n -E occurrence=f > C:\\Users\\CYQ\\Desktop\\stream\\size\\' + str(i) + '.csv'
     
    os.system(cmd)
    
    
    ##print(cmd)
    i=i+1
