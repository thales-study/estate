from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.metrics import accuracy_score,precision_score, recall_score
from sklearn.svm import SVC
from modules.dataset import X, y, columns
import matplotlib.pyplot as plt
import numpy as np

tol = 1e-4 #float, default=1e-4 Tolerance for stopping criteria.
C = 0.5 #float, default=1.0 Regularization parameter. The strength of the regularization is inversely proportional to C. Must be strictly positive.

pipe = make_pipeline(
  StandardScaler(),
  SVC(random_state = 0, tol = tol, C = C)
)

X_train, X_test, y_train, y_test = train_test_split(X[:,2:9], y, random_state = 1)
pipe.fit(X_train, y_train)
print(pipe.named_steps['svc'].intercept_)
predictions = pipe.predict(X_test)
print("真实数据：\n{}\n 预测数据：\n{}".format(y_test, predictions))
print("准确率：{} 精确率：{}".format(accuracy_score(y_test, predictions), precision_score(y_test, predictions)))

# 图表
plt.rcParams['font.family'] = ['SimHei']  # 中文字体设置
plt.rcParams['axes.unicode_minus'] = False

#使用ggplot的风格绘图
plt.style.use('ggplot')

#构造数据

minmaxTransformer = MinMaxScaler(feature_range=(0,1))
X_test_trans = minmaxTransformer.fit_transform(X_test)

figure = columns[2:9]
N = len(figure)

#设置雷达图的角度，用于平分切开一个平面
angles = np.linspace(0,2*np.pi,N,endpoint=False)

#绘图
fig = plt.figure()
#设置为极坐标格式
ax = fig.add_subplot(111, polar=True)
#添加每个特质的标签
ax.set_thetagrids(angles*180/np.pi, figure)
#设置极轴范围
ax.set_ylim(0,1)
#添加标题
plt.title('拿地预测')
#增加网格纸
ax.grid(True)
#绘制折线图
for i in range(len(predictions)):
  values = X_test_trans[i]
  # values = np.concatenate((values,[values[0]]))
  fmt = 'o-' if predictions[i] == y_test[i] else '.-.'
  ax.plot(angles, values, fmt, linewidth = 1)

plt.show()