from sklearn.feature_selection import SelectKBest, f_classif, f_regression, chi2
from modules.dataset import X, y, columns
import matplotlib.pyplot as plt
import numpy as np

d = {}


# f_classif
selector = SelectKBest(score_func=f_classif, k=3)
selector.fit(X, y)

d["f_classif"] = selector.scores_
print("f_classif")
print('pvalues_:',selector.pvalues_)
print('selected index:',selector.get_support(True))



# f_regression
selector = SelectKBest(score_func=f_regression, k=3)
selector.fit(X, y)

d["f_regression"] = selector.scores_
print('pvalues_:',selector.pvalues_)
print('selected index:',selector.get_support(True))



# chi
selector = SelectKBest(score_func=chi2, k=3)
selector.fit(X, y)

d["chi2"] = selector.scores_
print("chi2")
print('pvalues_:',selector.pvalues_)
print('selected index:',selector.get_support(True))


plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文字体设置
plt.rcParams['axes.unicode_minus'] = False
fig, ax = plt.subplots()

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('特征选择')
x = np.arange(len(columns))  # the label locations
ax.set_xticks(x)
ax.set_xticklabels(columns)
for tick in ax.get_xticklabels():
  tick.set_rotation(90)

width = 0.20  # the width of the bars
ax.bar(x - width, d["f_classif"], width, label='方差分析')
ax.bar(x, d["f_regression"], width, label='单量线性回归')
ax.bar(x + width, d["chi2"]/10000, width, label='卡方检验')
ax.legend()

fig.tight_layout()

plt.show()
