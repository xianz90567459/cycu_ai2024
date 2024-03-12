#112年1-10月交通事故簡訊通報資料.csv

import pandas as pd

# 讀取 csv 文件
df = pd.read_csv('112年1-10月交通事故簡訊通報資料.csv')

# 顯示所有標題
print(df.columns.tolist())

# 顯示前五行數據
print(df.head())