import os

i = 1;
while(i<30):
    cmd = 'C:\\Users\\CYQ\\Desktop\\wireshark\\tshark.exe -r C:\\Users\\CYQ\\Desktop\\ftp\\'+ str(i) + '.pcapng -qz io,stat,0,"COUNT(frame) frame"'
     
    os.system(cmd)
    
    
    ##print(cmd)
    i=i+1


#   C:\\Users\\CYQ\\Desktop\\wireshark\\tshark.exe -r C:\\Users\\CYQ\\Desktop\\ftp\\1.pcapng -qz io,stat,0,"COUNT(frame) frame"