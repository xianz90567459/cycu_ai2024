#112年1-10月交通事故簡訊通報資料.csv

import pandas as pd
import matplotlib.pyplot as plt

# 讀取 csv 文件
df = pd.read_csv('/workspaces/cycu_ai2024/20240312/112年1-10月交通事故簡訊通報資料.csv')

# 顯示所有標題
print(df.columns.tolist())

# 顯示前五行數據
print(df.head())

#篩選出 欄位名稱 為 國道名稱 的資料，我只要名稱為國道1號的資料，且只要方向有'南'這個字的資料
df = df[(df['國道名稱'] == '國道3號') & (df['方向'].str.contains('北'))]


#把欄位 '年' '月' '日' '時' '分' 合併成一個欄位為'事件開始' 並轉換為日期格式
df['事件開始'] = df['年'].astype(str) + '-' + df['月'].astype(str) + '-' + df['日'].astype(str) + ' ' + df['時'].astype(str) + ':' + df['分'].astype(str)

#把欄位 '年' '月' '日' '事件排除' 合併成一個欄位為'事件排除' 並轉換為日期格式
df['事件排除'] = df['年'].astype(str) + '-' + df['月'].astype(str) + '-' + df['日'].astype(str) + ' ' + df['事件排除'].astype(str)

#drop 欄位 '年' '月' '日' '時' '分' 
df = df.drop(columns=['年', '月', '日', '時', '分'])

# 將 '事件開始' 和 '事件排除' 兩個欄位轉換為 datetime 對象
df['事件開始'] = pd.to_datetime(df['事件開始'])
df['事件排除'] = pd.to_datetime(df['事件排除'])

# 將 datetime 對象轉換為時間戳
df['事件開始1'] = df['事件開始'].apply(lambda x: x.timestamp())
df['事件排除1'] = df['事件排除'].apply(lambda x: x.timestamp())


# 輸出到 Excel 文件
df.to_excel('事件開始_結束.xlsx', index=False)


#只印出 '事件開始' '事件排除' '國道名稱' '事件類型' '事件描述'
print(df[['事件開始', '事件排除', '國道名稱','里程','事件開始1','事件排除1']])

#以 '里程' 為 y軸 , '事件開始1' 為 x軸 起點 , '事件排除1' 為 x軸 終點 繪製線段
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 使用支援中文的字體
font = FontProperties(fname=r"/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", size=14)

# 假設 df 是您的 DataFrame
for index, row in df.iterrows():
    plt.plot([row['事件開始1'], row['事件排除1']], [row['里程'], row['里程']])

plt.xlabel('事件時間', fontproperties=font)
plt.ylabel('里程', fontproperties=font)

# 設置圖片標題
plt.title('國道3號北向_學號:11272009', fontproperties=font)

# 儲存圖片
plt.savefig('國道3號北向_學號11272009.png')

plt.show()









