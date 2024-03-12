#112年1-10月交通事故簡訊通報資料.csv

import pandas as pd

# 讀取 csv 文件
df = pd.read_csv('112年1-10月交通事故簡訊通報資料.csv')

# 顯示所有標題
print(df.columns.tolist())

# 顯示前五行數據
print(df.head())

#篩選出 欄位名稱 為 國道名稱 的資料，我只要名稱為國道1號的資料
df = df[df['國道名稱'] == '國道1號']

#把欄位 '年' '月' '日' '時' '分' 合併成一個欄位為'事件開始' 並轉換為日期格式
df['事件開始'] = df['年'].astype(str) + '-' + df['月'].astype(str) + '-' + df['日'].astype(str) + ' ' + df['時'].astype(str) + ':' + df['分'].astype(str)

#把欄位 '年' '月' '日' '事件排除' 合併成一個欄位為'事件排除' 並轉換為日期格式
df['事件排除'] = df['年'].astype(str) + '-' + df['月'].astype(str) + '-' + df['日'].astype(str) + ' ' + df['事件排除'].astype(str)

#drop 欄位 '年' '月' '日' '時' '分' 
df = df.drop(columns=['年', '月', '日', '時', '分'])

#將 '事件開始' '事件排除' 兩個欄位轉換成 unix 時間戳 並用整數表示
df['事件開始'] = (pd.to_datetime(df['事件開始']).view('int64') // 10**9).astype('int32')
df['事件排除'] = (pd.to_datetime(df['事件排除']).view('int64') // 10**9).astype('int32')


# 輸出到 Excel 文件
df.to_excel('事件開始_結束.xlsx', index=False)



# 只顯示出 '事件開始' '事件排除' '國道名稱' '里程'  '事件開始' '事件排除' 這些欄位
print(df[['事件開始', '事件排除', '國道名稱', '里程', '事件開始', '事件排除']])

#以 '里程' 為 y軸 , '事件開始' 為 x軸 起點 , '事件排除' 為 x軸 終點 繪製範圍橫條圖
df.plot.barh(x='事件開始', y='里程', xerr='事件排除', alpha=0.5)
plt.show()


