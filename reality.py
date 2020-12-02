import modules.svm as svm
import pandas as pd
import numpy as np

feagures = [2, 3, 4, 9]
res = svm.predict(10, feagures, 15)

df = pd.read_excel("estate.xlsx", sheet_name="2020粗加工")
df = df.drop(df.columns[-3:], axis=1)

df["预测"] = np.insert(res["predictions"], 0, -1, axis=0) 
writer = pd.ExcelWriter("./out/reality.xlsx") # pylint: disable=abstract-class-instantiated
df.to_excel(writer, sheet_name="数据", index=False)

factor = pd.DataFrame({"准确度":[res["accuracy"]], "精确度":[res["precision"]], "召回率":[res["recall"]]},)
factor.to_excel(writer, sheet_name="精确", index=False)
writer.save()

