'''
from sklearn.metrics import accuracy_score, f1_score
import numpy as np
'''
from sklearn.metrics import classification_report
import xgboost as xgb
import numpy as np
'''
def calAcc(y, y_pre, x):
    y_pre = np.where(y_pre > x, 1, 0)
    return accuracy_score(y, y_pre)

def calF1(y, y_pre, x):
    y_pre = np.where(y_pre > x, 1, 0)
    return f1_score(y, y_pre, average='binary')
'''

def calConrepot(y, y_pre):
    y_pre = y_pre.argmax(axis=1)
    return classification_report(y, y_pre, target_names=['FTP', 'VOIP', 'Stream'])


def test(sample, cols, model):
    data_map ={'Packets':0,
                 'Average_pps':1,
                 'Average_packet_size':2,
                 'size_var':3,
                 'size_std':4,
                 'ave_time':5,
                 'time_std':6,
                 'time_var':7
                }
    sample_select = []
    for col in cols:
        sample_select.append(sample[data_map[col]])
    sample_select = np.array([sample_select])
    sample_select = xgb.DMatrix(sample_select)
    result = model.predict(sample_select).argmax()
    return result