import modules.svm as svm
import pandas as pdw
import time

dfw = pdw.DataFrame({"id":[], "全部":[], "选定特征":[], "削峰":[]})
print(r"{0:-^50}".format("开始执行"))
start = time.perf_counter()
num = 50
for i in range(1, num + 1):
  whole = svm.run(i)
  selected = svm.run(i, feagures = [2,3,4,9])
  flat = svm.run(i, feagures = [2,3,4])
  row = { "id": whole["seed"], "全部": whole["accuracy"], "选定特征": selected["accuracy"], "削峰": flat["accuracy"] }
  dfw.loc[i] = row

  now = time.perf_counter() - start
  per = (i/num)*100
  star = "*" * int(per)
  dot = "." * (num - int(per))
  print("\r{:.2f}%[{}->{}]{:.2f}s".format(per, star, dot, now), end='')

dfw.to_excel("out/feagure.xlsx", sheet_name='明细', index=False)
print("\n"+"{0:-^50}".format("执行结束"))
print("{0:-^50}".format("feagure.xlsx生成"))