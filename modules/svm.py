from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.metrics import accuracy_score,precision_score, recall_score
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_excel("estate.xlsx", sheet_name="粗加工") # 读取xlsx数据
df.drop(0, inplace = True) # 标题有两个，需要去掉一个

def run(seed = 0, C = 1, feagures = []):
  """运行svm
  Parameters
  ----------
  seed: 随机种子
  C: 学习力度，过小会“欠学习”，过大会“过学习”
  feagues: 特征选择
  """
  pipe = make_pipeline(
    StandardScaler(),
    SVC(random_state = 0, C = C)
  )

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
  if feagures and len(feagures) > 0:
    arr = []
    for i in feagures:
      arr.append(columns[i])
    columns = arr
  X = df.loc[:, columns].values
  y = df.loc[:,  '项目验证（标签）'].values


  X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = seed)
  pipe.fit(X_train, y_train)
  predictions = pipe.predict(X_test)
  return {
    "seed": seed,
    "accuracy": accuracy_score(y_test, predictions),
    "precision": precision_score(y_test, predictions)
  }