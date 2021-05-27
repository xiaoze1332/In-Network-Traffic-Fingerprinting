import pandas as pd
from sklearn.model_selection import StratifiedKFold
import numpy as np
from sklearn.model_selection import train_test_split
from copy import copy

class DataProcess:

    def __init__(self, data_path):
        self.data = pd.read_excel(data_path)
        self.cols = ['Packets',
                        'Average_pps',
                        'Average_packet_size',
                        'size_var',
                        'size_std',
                        'ave_time',
                        'time_std',
                        'time_var',
                        'target']

        self.cols_x = ['Packets',
                        'Average_pps',
                        'Average_packet_size',
                        'size_var',
                        'size_std',
                        'ave_time',
                        'time_std',
                        'time_var']

        self.data = self.data.iloc[:, 1:]
        self.data.columns = self.cols

        self.outlier = 0.99
        self.corr = 0.95

    '''
    def split(self, X, y):
        skf = StratifiedKFold(n_splits=2)

        for train_index, test_index in skf.split(X, y):
            X_train, X_test = X[train_index], X[test_index]
            y_train, y_test = y[train_index], y[test_index]

        return X_train, X_test, y_train, y_test

    def run(self):
        target_map = {'FTP': 1, 'VOIP': 2, 'Stream': 3}
        self.data['target'].replace(target_map, inplace=True)

        data1 = self.data[self.data['target'] != 1]
        target_map = {2: 0, 3: 1}
        data1['target'].replace(target_map, inplace=True)
        X1 = np.array(data1[self.cols_x])
        y1 = np.array(data1['target'])
        X1_train, X1_test, y1_train, y1_test = self.split(X1, y1)

        data2 = self.data[self.data['target'] != 2]
        target_map = {1: 0, 3: 1}
        data2['target'].replace(target_map, inplace=True)
        X2 = np.array(data2[self.cols_x])
        y2 = np.array(data2['target'])
        X2_train, X2_test, y2_train, y2_test = self.split(X2, y2)


        data3 = self.data[self.data['target'] != 3]
        target_map = {1: 0, 2: 1}
        data3['target'].replace(target_map, inplace=True)
        X3 = np.array(data3[self.cols_x])
        y3 = np.array(data3['target'])
        X3_train, X3_test, y3_train, y3_test = self.split(X3, y3)

        return X1_train, X1_test, y1_train, y1_test, X2_train, X2_test, y2_train, y2_test, X3_train, X3_test, y3_train, y3_test
'''

class DataProcessMulti(DataProcess):

    def __init__(self, data_path):
        DataProcess.__init__(self, data_path)

    def preprocess(self):

        # clean
        col_up_list = []
        for col in self.cols:
            col_up = self.data[col].quantile(self.outlier)
            col_up_list.append(col_up)

        for k, v in enumerate(self.cols):
            self.data.loc[self.data[v] > col_up_list[k], v] = col_up_list[k]

        # correlation
        cor_feat_list = []
        corr_mat = self.data.corr()
        for col1 in self.cols:
            for col2 in self.cols:
                if col1 == col2:
                    pass
                else:
                    if corr_mat.loc[col1, col2] > self.corr:
                        cor_feat_list.append(col1)
        cor_feat_list = list(set(cor_feat_list))

        self.cols = set(self.cols).difference(set(cor_feat_list))
        self.cols_x = copy(self.cols)
        self.cols_x.remove('target')
        self.data = self.data[self.cols]


    def run(self):
        #label mapping
        target_map = {'FTP': 0, 'VOIP': 1, 'Stream': 2}
        self.data['target'].replace(target_map, inplace=True)

        #clean correlation
        self.preprocess()

        #feature label
        X = np.array(self.data[self.cols_x])
        y = np.array(self.data['target'])

        #train test
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=7)

        return X_train, X_test, y_train, y_test, self.cols_x
