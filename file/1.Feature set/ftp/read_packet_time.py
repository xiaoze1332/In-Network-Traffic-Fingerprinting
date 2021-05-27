import os

i = 1;
while(i<30):
    cmd = 'C:\\Users\\CYQ\\Desktop\\wireshark\\tshark.exe -r C:\\Users\\CYQ\\Desktop\\ftp\\'+ str(i) + '.pcapng -T fields -e frame.time_delta > C:\\Users\\CYQ\\Desktop\\ftp\\time\\' + str(i) + '.csv'
     
    os.system(cmd)
    
    
    ##print(cmd)
    i=i+1
