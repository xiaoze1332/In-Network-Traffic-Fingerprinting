import xlwt
import pandas as pd
import numpy as np

# get bin range using frequency bin
        
dataSet = pd.read_csv('data.csv')
dataSetNP = np.array(dataSet)  
#get the range of the first attribute
pkn = dataSetNP[:,0]
pkn_s = dataSetNP[:,0]
pkn_s.sort()
#get the range of the rest attribute
ap = dataSetNP[:,1]
ap_s = dataSetNP[:,1]
 ap_s.sort()

aps = dataSetNP[:,2]
aps_s = dataSetNP[:,2]
aps_s.sort()

psd = dataSetNP[:,3]
psd_s = dataSetNP[:,3]
psd_s.sort()
    
pv = dataSetNP[:,4]
pv_s = dataSetNP[:,4]
pv_s.sort()

pt = dataSetNP[:,5]
pt_s = dataSetNP[:,5]
pt_s.sort()

pts = dataSetNP[:,6]
pts_s = dataSetNP[:,6]
pts_s.sort()

ptv = dataSetNP[:,7]
ptv_s = dataSetNP[:,7]
ptv_s.sort()

#process original data
for i in range(len(pkn)):
    if pkn[i] < pkn_s[30]:
        pkn[i] = 1
    elif pkn[i] >pkn_s[60]:
        pkn[i] = 3
    else:
        pkn[i] = 2

for i in range(len(aps)):
    if aps[i] < aps_s[30]:
        aps[i] = 1
    elif aps[i] >aps_s[60]:
        aps[i] = 3
    else:
        aps[i] = 2
        
for i in range(len(ap)):
    if ap[i] < ap_s[30]:
        ap[i] = 1
    elif ap[i] >ap_s[60]:
        ap[i] = 3
    else:
        ap[i] = 2

for i in range(len(psd)):
    if psd[i] < psd_s[30]:
        psd[i] = 1
    elif psd[i] >psd_s[60]:
        psd[i] = 3
    else:
        psd[i] = 2

for i in range(len(pt)):
    if pt[i] < pt_s[30]:
        pt[i] = 1
    elif pt[i] >pt_s[60]:
        pt[i] = 3
    else:
        pt[i] = 2

for i in range(len(pv)):
    if pv[i] < pv_s[30]:
        pv[i] = 1
    elif pv[i] >pv_s[60]:
        pv[i] = 3
    else:
        pv[i] = 2

for i in range(len(pts)):
    if pts[i] < pts_s[30]:
        pts[i] = 1
    elif pts[i] >pts_s[60]:
        pts[i] = 3
    else:
        pts[i] = 2

for i in range(len(ptv)):
    if ptv[i] < ptv_s[30]:
        ptv[i] = 1
    elif ptv[i] >ptv_s[60]:
        ptv[i] = 3
    else:
        ptv[i] = 2

#write processed data into file

workbook = xlwt.Workbook()
dataset = workbook.add_sheet('s1')
for i in range(len(pkn)):
    dataset.write(i,0,pkn[i])

for i in range(len(pkn)):
    dataset.write(i,1,ap[i])

for i in range(len(pkn)):
    dataset.write(i,2,aps[i])

for i in range(len(pkn)):
    dataset.write(i,3,psd[i])
            
for i in range(len(pkn)):
    dataset.write(i,4,pv[i])

for i in range(len(pkn)):
    dataset.write(i,5,pt[i])

for i in range(len(pkn)):
    dataset.write(i,6,pts[i])

for i in range(len(pkn)):
    dataset.write(i,7,ptv[i])
workbook.save('dataset.xls')


    
    
    
