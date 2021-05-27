
'''
from utils import calAcc, calF1
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
'''
import xgboost as xgb
from utils import calConrepot, test
from data_process import DataProcess, DataProcessMulti


'''
data_process = DataProcess('data/data.xlsx')
X1_train, X1_test, y1_train, y1_test, X2_train, X2_test, y2_train, y2_test, X3_train, X3_test, y3_train, y3_test = data_process.run()


clf1 = LogisticRegression(solver='liblinear', random_state=0).fit(X1_train, y1_train)
y1_pre = clf1.predict_proba(X1_test)[:, 1]


clf2 = LogisticRegression(solver='liblinear', random_state=0).fit(X2_train, y2_train)
y2_pre = clf2.predict_proba(X2_test)[:, 1]


clf3 = LogisticRegression(solver='liblinear', random_state=0).fit(X3_train, y3_train)
y3_pre = clf3.predict_proba(X3_test)[:, 1]

print("ROC_AUC score for each model:")
print(roc_auc_score(y1_test, y1_pre))
print(roc_auc_score(y2_test, y2_pre))
print(roc_auc_score(y3_test, y3_pre))

print("Accuracy for each model:")
print(calAcc(y1_test, y1_pre, 0.6))
print(calAcc(y2_test, y2_pre, 0.45))
print(calAcc(y3_test, y3_pre, 0.45))

print("F1 measure for each model:")
print(calF1(y1_test, y1_pre, 0.6))
print(calF1(y2_test, y2_pre, 0.45))
print(calF1(y3_test, y3_pre, 0.45))
'''
#read
data_process = DataProcessMulti('data/data.xlsx')

#process data
X_train, X_test, y_train, y_test, cols = data_process.run()

params = {
    'booster': 'gbtree',
    'objective': 'multi:softprob',
    'num_class': 3,
    'gamma': 0.1,
    'max_depth': 2,
    'lambda': 1,
    'subsample': 0.7,
    'colsample_bytree': 0.7,
    'min_child_weight': 0,
    'silent': 0,
    'eta': 0.1,
    'seed': 1000,
    'nthread': 4,
}

dtrain = xgb.DMatrix(X_train, y_train)
num_rounds = 40
plst = params
model = xgb.train(plst, dtrain, num_rounds)

dtest = xgb.DMatrix(X_test)
ans = model.predict(dtest)
print(calConrepot(y_test, ans))

test_sample = [1241,81.76846544,15063.77357,21043.33623,442821999.6,0.01219901,0.031012641,0.000961784]
print(test(test_sample, cols, model))