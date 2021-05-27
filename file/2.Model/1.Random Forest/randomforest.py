{\rtf1\ansi\ansicpg936\cocoartf2513
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fnil\fcharset134 PingFangSC-Regular;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # coding: utf-8\
\
# In[1]:\
\
import warnings\
warnings.filterwarnings("ignore")\
import pandas as pd\
import numpy as np\
from tqdm import tqdm\
import xgboost\
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier\
from sklearn.tree import DecisionTreeClassifier\
\
\
# In[3]:\
\
p = r'data.xlsx'\
df = pd.read_excel(p)\
print(df.shape)\
print(df.head())\
\
\
# In[6]:\
\
map_label = \{\}\
labels = df['label'].unique()\
for i,j in enumerate(labels):\
    map_label[j] = i\
print(map_label)\
df['target'] = df['label'].apply(lambda x:map_label[x])\
del df['label']\
\
\
# In[7]:\
\
df.head()\
\
\
# In[8]:\
\
from sklearn.metrics import accuracy_score\
from sklearn import metrics\
from sklearn.metrics import confusion_matrix,classification_report\
\
\
# In[9]:\
\
X = np.array(df.iloc[:,:-1])\
y = np.array(df.iloc[:,-1])\
\
\
from sklearn.model_selection import train_test_split\
x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.3)\
print('
\f1 \'d1\'b5\'c1\'b7\'ca\'fd\'be\'dd\'b4\'f3\'d0\'a1
\f0 :',x_train.shape)\
print('
\f1 \'b2\'e2\'ca\'d4\'ca\'fd\'be\'dd\'b4\'f3\'d0\'a1
\f0 :',x_test.shape)\
\
\
# In[10]:\
\
#
\f1 \'cb\'e6\'bb\'fa\'c9\'ad\'c1\'d6\'b5\'c4\'bd\'e1\'b9\'fb
\f0 \
rf = RandomForestClassifier(max_depth=6,n_estimators=70)\
rf.fit(x_train,y_train)\
print('
\f1 \'d1\'b5\'c1\'b7\'be\'ab\'b6\'c8
\f0 :',rf.score(x_train,y_train))\
y_pred = rf.predict(x_test)\
\
#
\f1 \'bb\'ec\'cf\'fd\'be\'d8\'d5\'f3
\f0 \
print('
\f1 \'bb\'ec\'cf\'fd\'be\'d8\'d5\'f3
\f0 :\\n',confusion_matrix(y_test, y_pred))\
print('=================================')\
print('
\f1 \'be\'ab\'d7\'bc\'c2\'ca\'a3\'ba
\f0 ',metrics.precision_score(y_test, y_pred, average='weighted')) # 
\f1 \'ce\'a2\'c6\'bd\'be\'f9\'a3\'ac\'be\'ab\'c8\'b7\'c2\'ca
\f0 \
print('
\f1 \'d7\'bc\'c8\'b7\'c2\'ca\'a3\'ba
\f0 ',metrics.accuracy_score(y_test, y_pred))\
print('
\f1 \'d5\'d9\'bb\'d8\'c2\'ca\'a3\'ba
\f0 ',metrics.recall_score(y_test, y_pred, average='weighted'))\
print('F1
\f1 \'d6\'b5\'a3\'ba
\f0 ',metrics.f1_score(y_test, y_pred, average='weighted'))\
print('
\f1 \'b7\'d6\'c0\'e0\'b1\'a8\'b8\'e6
\f0 :',classification_report(y_test, y_pred))}