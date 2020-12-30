import modules.svm as svm
import matplotlib.pyplot as plt
import numpy as np


plt.rcParams['font.family'] = ['SimHei']  # 中文字体设置
plt.rcParams['axes.unicode_minus'] = False

c = np.array([-3, -2, -1, 0, 1, 2, 3])
gamma = np.array([-3, -2, -1, 0, 1, 2, 3])
c = 10.0 ** c
gamma = 10.0 ** gamma
feagures = [2,3,4,9]

arr = []
for m, y in enumerate(gamma):
  for n, x in enumerate(c):
    ids = []
    for seed in range(1, 50):
      res = svm.run(seed, x,feagures, y)
      accuracy = res["accuracy"]
      ids.append(accuracy)
    arr.append(np.mean(ids))
harvest = np.array(arr)
harvest = harvest * 255
harvest = harvest.astype(np.int8)
harvest = np.reshape(harvest, (len(gamma), len(c)))

fig, ax = plt.subplots()
im = ax.imshow(harvest)

ax.set_xticks(np.arange(len(c)))
ax.set_yticks(np.arange(len(gamma)))

ax.set_xticklabels(c)
ax.set_yticklabels(gamma)

ax.set_xlabel("c 10 ** n")
ax.set_ylabel("gamma 10 ** n")

for i in range(len(gamma)):
  for j in range(len(c)):
    text = ax.text(j, i, "%.2f" % arr[j + i * len(gamma)], ha="center", va="center", color="w")

ax.set_title("c & gamma")
fig.tight_layout()
plt.show()
