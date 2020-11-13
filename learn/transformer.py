from sklearn.preprocessing import StandardScaler

x = [
  [0, 15],
  [-1, -10]
]
res = StandardScaler().fit(x).transform(x)
print(res)