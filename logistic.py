import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

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

train = pd.read_excel("estate.xlsx", sheet_name="粗加工")
train.drop(0, inplace = True)
train_X = train.loc[:, columns].values
train_y = train.loc[:,  '项目验证（标签）'].values

model = LogisticRegression(max_iter=5000)
model.fit(train_X, train_y)

reality = pd.read_excel("estate.xlsx", sheet_name="2020粗加工")
reality.drop(0, inplace = True)
real_X = reality.loc[:, columns].values
real_y = reality.loc[:,  '项目验证（标签）'].values


predictions = model.predict(real_X)


print(accuracy_score(real_y, predictions))
print(predictions)
print(real_y)
