#112年1-10月交通事故簡訊通報資料.csv

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 讀取 Excel 文件
df = pd.read_csv('112年1-10月交通事故簡訊通報資料.csv', dtype={30: str, 47: str, 48: str})

# 過濾資料
filtered_df = df[(df['國道名稱'] == '國道1號') & (df['方向'].str.contains('南'))]

# 根據 '里程' 分組並計算每個里程的事件數量
mileage_counts = filtered_df.groupby('里程').size()

# 將 Series 轉換為 DataFrame，並指定列名
mileage_counts_df = mileage_counts.reset_index(name='發生次數')

# 輸出到 Excel 文件
mileage_counts_df.to_excel('國道1號南下里程事件.xlsx', index=False)

# 設定字體
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14) 

# 繪製所有里程數的長條圖
plt.figure(figsize=(20,10)) # 設定圖表大小
plt.bar(mileage_counts_df['里程'], mileage_counts_df['發生次數'])
plt.xlabel('里程', fontproperties=font)
plt.ylabel('發生次數', fontproperties=font)
plt.title('所有里程數的事件數量', fontproperties=font)
plt.show()
#儲存圖表
plt.savefig('所有里程數的事件數量.png')

#列出發生事件最高的5個里程數
top_5 = mileage_counts_df.nlargest(5, '發生次數')
print(top_5)