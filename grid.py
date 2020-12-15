import modules.svm as svm
import matplotlib.pyplot as plt
import numpy as np

params = [-3, -2, -1, 0, 1, 2, 3]
feagures = [2,3,4,9]
plt.rcParams['font.family'] = ['SimHei']  # 中文字体设置
plt.rcParams['axes.unicode_minus'] = False
fig, ax = plt.subplots()
ax.set_xlabel('c')
ax.set_ylabel('gamma')
ax.set_title('c & gamma')
# ax.grid(True)

utmost = {
  "accuracy": 0,
  "x": 0,
  "y": 0
}
for m in range(len(params)):
  for n in range(len(params)):
    x = params[n]
    y = params[m]
    res = svm.run(1, 10 ** x, feagures, 10 ** y)
    accuracy = res["accuracy"]
    if accuracy > utmost["accuracy"]:
      utmost["accuracy"] = accuracy
      utmost["x"] = x
      utmost["y"] = y

    scale = (accuracy * 5) ** 3
    plt.scatter(params[n], params[m], scale, c="r")
print(utmost)

fig.tight_layout()
plt.show()

