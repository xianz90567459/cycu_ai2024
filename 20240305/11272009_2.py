#https://vipmbr.cpc.com.tw/mbwebs/ShowHistoryPrice_oil2019.aspx
#https://vipmbr.cpc.com.tw/mbwebs/ShowHistoryPrice_oil.aspx
import pandas as pd
import matplotlib.pyplot as plt
import requests

# 網址
urls = ['https://vipmbr.cpc.com.tw/mbwebs/ShowHistoryPrice_oil2019.aspx', 
        'https://vipmbr.cpc.com.tw/mbwebs/ShowHistoryPrice_oil.aspx']

# 使用 pandas 的 read_html 函數讀取網頁中的第二個表格數據
dataframes = [pd.read_html(requests.get(url, verify=False).text)[1] for url in urls]

# 將兩個表格的數據合併為一個 DataFrame
df = pd.concat(dataframes)

# 清理數據，移除不能被解析為日期的值
df = df[df.iloc[:, 0].str.match(r'\d{4}/\d{2}/\d{2}')]

# 將第一列設置為索引，並轉換為日期格式
df.iloc[:, 0] = df.iloc[:, 0].str.slice(0, 10)  # 只保留日期部分
df.set_index(pd.to_datetime(df.iloc[:, 0], format='%Y/%m/%d'), inplace=True)

import matplotlib

# 設置 matplotlib 的字體為 Microsoft YaHei，支援中文
matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei']
matplotlib.rcParams['font.family'] ='sans-serif'

# 將每一種油價的數據分開處理
columns = df.columns[1:5]
for column in columns:
    # 移除該列包含 NaN 的行
    data = df[[column]].dropna()
    # 將數據轉換為數值型
    data[column] = pd.to_numeric(data[column], errors='coerce')
    # 再次移除可能因為轉換數值型產生的 NaN
    data = data.dropna()
    # 將數據按照時間排序
    data = data.sort_index()
    # 繪製圖形
    plt.plot(data.index, data[column], label=column)

# 設定圖片的標題和軸標籤
plt.title('油價走勢')
plt.xlabel('日期')
plt.ylabel('價格')

# 顯示圖例
plt.legend()

# 保存圖片
plt.savefig('oil_price_trend.png')

# 顯示圖片
plt.show()