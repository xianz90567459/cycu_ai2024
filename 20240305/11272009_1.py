import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
# 獲取網頁的HTML內容
url = 'https://vipmbr.cpc.com.tw/mbwebs/ShowHistoryPrice_oil.aspx'
response = requests.get(url)

# 解析HTML內容
soup = BeautifulSoup(response.text, 'html.parser')

# 找到我們需要的數據並提取出來
# 這裡假設我們需要的數據在兩個表格中
tables = soup.find_all('table')
dataframes = []
for i, table in enumerate(tables):
    rows = table.find_all('tr')
    data = []
    for row in rows:
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)
    # 創建一個DataFrame並儲存數據
    df = pd.DataFrame(data)
    dataframes.append(df)
    # 將資料存成csv檔，每個表格有一個唯一的文件名
    df.to_csv(f'oil_{i}.csv', index=False, encoding='utf-8-sig')
    print(df)
    print('=====================')

# 現在，dataframes[0]和dataframes[1]分別包含兩個表格的數據
    
# 將第二個表格的第一列改為 datetime 格式
dataframes[1][0] = pd.to_datetime(dataframes[1][0], format='%Y/%m/%d')
#幫我把第二個表格的第二列標題改成無鉛汽油92
dataframes[1] = dataframes[1].rename(columns={dataframes[1].columns[1]: '無鉛汽油92'})
#x軸為日期，y軸為無鉛汽油92
dataframes[1] = dataframes[1].rename(columns={dataframes[1].columns[0]: '日期'})

from matplotlib.font_manager import FontProperties

# 設定字體為 Microsoft JhengHei
myfont = FontProperties(fname=r"c:\windows\fonts\msjh.ttc", size=14)
plt.rcParams['axes.unicode_minus'] = False


# 修改特定的列標題
dataframes[1] = dataframes[1].rename(columns={dataframes[1].columns[1]: '無鉛汽油92',
                                              dataframes[1].columns[2]: '無鉛汽油95',
                                              dataframes[1].columns[3]: '無鉛汽油98',
                                              dataframes[1].columns[4]: '超級/高級柴油'})

# 將每一種油價的數據分開處理
columns = ['無鉛汽油92', '無鉛汽油95', '無鉛汽油98', '超級/高級柴油']
for column in columns:
    # 移除該列包含 NaN 的行
    data = dataframes[1][['日期', column]].dropna()
    # 將數據轉換為數值型
    data[column] = pd.to_numeric(data[column], errors='coerce')
    # 再次移除可能因為轉換數值型產生的 NaN
    data = data.dropna()
    # 繪製圖形
    plt.plot(data['日期'], data[column], label=column)

# 設定圖片的標題和軸標籤
plt.title('油價走勢', fontproperties=myfont)
plt.xlabel('日期', fontproperties=myfont)
plt.ylabel('價格', fontproperties=myfont)

# 顯示圖例，並設定圖例的字體
plt.legend(prop=myfont)

# 將圖片存成png
plt.savefig('油價走勢.png')

# 顯示圖片
plt.show()