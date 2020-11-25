import modules.svm as svm
import pandas as pdw
import time

dfw = pdw.DataFrame({"id":[], "准确":[], "精确":[], "召回":[]})
print(r"{0:-^50}".format("开始执行"))
start = time.perf_counter()
num = 50
feagures = [2,3,4,5,6,9]
for i in range(1, num + 1):
  res = svm.run(i, 10, feagures)
  row = { "id": res["seed"], "准确": res["accuracy"], "精确": res["precision"], "召回": res["recall"] }
  dfw.loc[i] = row
  now = time.perf_counter() - start
  per = (i/num)*100
  star = "*" * int(per)
  dot = "." * (num - int(per))
  print("\r{:.2f}%[{}->{}]{:.2f}s".format(per, star, dot, now), end='')

dfw.to_excel("out/check.xlsx", sheet_name='明细', index=False)
print("\n"+"{0:-^50}".format("执行结束"))
print("{0:-^50}".format("check.xlsx生成"))