import modules.svm as svm
import pandas as pdw
import time

dfw = pdw.DataFrame({"id":[], "0.1":[], "0.5":[], "1":[], "2":[], "10":[]})
print(r"{0:-^50}".format("开始执行"))
start = time.perf_counter()
num = 50
feagures = [2,3,4,5,6,9]
for i in range(1, num + 1):
  res01 = svm.run(i, 0.1, feagures)
  res05 = svm.run(i, 0.5, feagures)
  res1 = svm.run(i, 1, feagures)
  res2 = svm.run(i, 2, feagures)
  res10 = svm.run(i, 10, feagures)
  row = { "id": res1["seed"], "0.1": res01["accuracy"], "0.5": res05["accuracy"], "1": res1["accuracy"], "2": res2["accuracy"], "10": res10["accuracy"] }
  dfw.loc[i] = row
  now = time.perf_counter() - start
  per = (i/num)*100
  star = "*" * int(per)
  dot = "." * (num - int(per))
  print("\r{:.2f}%[{}->{}]{:.2f}s".format(per, star, dot, now), end='')

dfw.to_excel("out/c.xlsx", sheet_name='明细', index=False)
print("\n"+"{0:-^50}".format("执行结束"))
print("{0:-^50}".format("c.xlsx生成"))