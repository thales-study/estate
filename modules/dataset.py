import pandas as pd

df = pd.read_excel("estate.xlsx", sheet_name="粗加工")
df.drop(0, inplace = True)

columns = [
  # '宗地编号',
  # '成交时间',
  '区域',
  '规划用途',
  '占地面积',
  '建筑面积',
  '成交总价（万元）',
  '成交单价（元/㎡）', 
  '楼面地价（元/㎡）',
  '容积率',
  '溢价率',
  '竞得品牌分级',
  # '项目验证（标签）'
]
X = df.loc[:, columns].values
y = df.loc[:,  '项目验证（标签）'].values