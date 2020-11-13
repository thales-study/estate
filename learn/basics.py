from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

clf = RandomForestClassifier(random_state=0)
X = [[1,2,3, "wo"], [11, 12, 13, "我"]]
y = [0, 1]
clf.fit(X, y)
x_test = [
  [1, 1, 1],
  [10, 14, 15],
  [22, 22, 22],
  [20, 10, 1]
]
print(clf.predict(x_test))
