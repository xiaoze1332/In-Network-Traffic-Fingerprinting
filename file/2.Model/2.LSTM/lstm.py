{\rtf1\ansi\ansicpg936\cocoartf2513
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fnil\fcharset134 PingFangSC-Regular;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww28300\viewh15200\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # In[11]:\
\
from keras.models import Sequential\
from keras.layers import Dense\
from keras.layers import LSTM\
from sklearn.preprocessing import MinMaxScaler,Normalizer\
from sklearn.metrics import mean_squared_error,mean_absolute_error\
\
\
# In[17]:\
\
mms = MinMaxScaler()\
X_new = mms.fit_transform(X)\
\
from keras.utils import to_categorical\
y_new = to_categorical(y,3)\
print(y_new.shape)\
\
x_train,x_test,y_train,y_test = train_test_split(X,y_new,test_size=0.3)\
\
\
# In[18]:\
\
#reshape the data for the LSTM\
# reshape input to be [samples, time steps, features]\
trainX = np.reshape(x_train, (x_train.shape[0], 1, x_train.shape[1]))\
testX = np.reshape(x_test, (x_test.shape[0], 1, x_test.shape[1]))\
print(trainX.shape)\
print(testX.shape)\
\
\
# In[15]:\
\
from keras.callbacks import EarlyStopping,ModelCheckpoint,History\
history = History()\
\
es = EarlyStopping(monitor='loss',patience=5)\
\
\
# In[30]:\
\
# create and fit the LSTM network\
model = Sequential()\
model.add(LSTM(64, input_shape=(1, 8),return_sequences=True))\
model.add(LSTM(32,activation='relu'))\
model.add(Dense(3,activation='softmax'))\
model.summary()\
model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['acc'])\
H = model.fit(trainX, y_train, epochs=10, batch_size=16,callbacks=[history],verbose=2)\
\
\
# In[31]:\
\
y_pred\
\
\
# In[28]:\
\
y_true = np.argmax(y_test,axis=1)\
y_true\
\
\
# In[33]:\
\
y_pred_ = model.predict(testX)\
y_pred = np.argmax(y_pred_,axis=1)\
y_true = np.argmax(y_test,axis=1)\
#
\f1 confusion matrix
\f0 \
print(\'91
\f1 confusion_matrix
\f0 :\\n\'92,confusion_matrix(y_true, y_pred))\
print('=================================')\
print(\'91
\f1 precision\'a3\'ba
\f0 \'92,metrics.precision_score(y_true, y_pred, average='weighted')) # 
\f1 \'ce\'a2\'c6\'bd\'be\'f9\'a3\'ac\'be\'ab\'c8\'b7\'c2\'ca
\f0 \
print(\'91
\f1 accuracy\'a3\'ba
\f0 \'92,metrics.accuracy_score(y_true, y_pred))\
print(\'91
\f1 recall\'a3\'ba
\f0 \'92,metrics.recall_score(y_true, y_pred, average='weighted'))\
print('F1
\f1 score\'a3\'ba
\f0 \'92,metrics.f1_score(y_true, y_pred, average='weighted'))\
print(\'91
\f1 report
\f0 :\'92,classification_report(y_true, y_pred))\
\
\
# In[ ]:\
\
}