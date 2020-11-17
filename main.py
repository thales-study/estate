from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC 
import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_excel("estate.xlsx", sheet_name="粗加工")
# print(df.columns)

df.drop(0, inplace = True)

tol = 1e-4 #float, default=1e-4 Tolerance for stopping criteria.
C = 1.0 #float, default=1.0 Regularization parameter. The strength of the regularization is inversely proportional to C. Must be strictly positive.

pipe = make_pipeline(
  StandardScaler(),
  LinearSVC(random_state = 0, tol = tol, C = C)
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
X = df.loc[:, columns].values
y = df.loc[:,  '项目验证（标签）'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
pipe.fit(X_train, y_train.astype('int'))
print(pipe.named_steps['linearsvc'].coef_)
print(pipe.named_steps['linearsvc'].intercept_)
res = pipe.predict(X_test)
print(res)

# plt.rcParams['font.sans-serif']=['SimHei']
# plt.figure()
# plt.ylabel("溢价率")
# for n in range(2, 6):
#   print(columns[n])
#   plt.scatter(X_test[:,n], y_test, label=columns[n])
# plt.legend()
# plt.show()
