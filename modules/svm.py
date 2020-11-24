from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.metrics import accuracy_score,precision_score, recall_score
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_excel("estate.xlsx", sheet_name="粗加工")
df.drop(0, inplace = True)

columns = [
  # '宗地编号',
  # '成交时间',
  '区域',
  '规划用途',
  '占地面积',
  '建筑面积',
  '成交总价（万元）',
  '成交单价（元/㎡）', 
  '楼面地价（元/㎡）',
  '容积率',
  '溢价率',
  '竞得品牌分级',
  # '项目验证（标签）'
]
X = df.loc[:, columns].values
y = df.loc[:,  '项目验证（标签）'].values

tol = 1e-4 #float, default=1e-4 Tolerance for stopping criteria.
C = 0.5 #float, default=1.0 Regularization parameter. The strength of the regularization is inversely proportional to C. Must be strictly positive.

def run(seed):
  pipe = make_pipeline(
    StandardScaler(),
    SVC(random_state = 0, tol = tol, C = C)
  )

  X_train, X_test, y_train, y_test = train_test_split(X[:,2:9], y, random_state = seed)
  pipe.fit(X_train, y_train)
  predictions = pipe.predict(X_test)
  return {
    "seed": seed,
    "accuracy": accuracy_score(y_test, predictions),
    "precision": precision_score(y_test, predictions)
  }