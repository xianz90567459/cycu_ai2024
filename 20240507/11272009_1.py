import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

# 讀取 CSV 檔案
df = pd.read_csv('/workspaces/cycu_ai2024/20240507/11272009_2.csv')

# 根據 '小客車旅行速度' 的數值範圍來設定顏色
def speed_to_color(speed):
    if speed < 20:
        return 'purple'
    elif 20 <= speed < 40:
        return 'red'
    elif 40 <= speed < 60:
        return 'orange'
    elif 60 <= speed < 80:
        return 'yellow'
    else:
        return 'green'

df['顏色碼'] = df['小客車旅行速度'].apply(speed_to_color)

# 根據 '方向' 欄位的值將數據分成兩部分
df_north = df[df['方向'] == 1]
df_south = df[df['方向'] == 2]

# 創建兩個 3D 圖形
fig1 = plt.figure()
ax1 = fig1.add_subplot(111, projection='3d')

fig2 = plt.figure()
ax2 = fig2.add_subplot(111, projection='3d')

# 繪製北向的 3D 散點圖
ax1.scatter(df_north['時間'], df_north['地點'], df_north['小客車'], c=df_north['顏色碼'], s=5)

# 設定軸標籤
ax1.set_xlabel('Time')
ax1.set_ylabel('Mileage')
ax1.set_zlabel('Number of cars')

# 顯示圖表
plt.show()

#下載圖片
fig1.savefig('/workspaces/cycu_ai2024/20240507/11272009_2_north.png')

# 繪製南向的 3D 散點圖
ax2.scatter(df_south['時間'], df_south['地點'], df_south['小客車'], c=df_south['顏色碼'], s=5)

# 設定軸標籤
ax2.set_xlabel('Time')
ax2.set_ylabel('Mileage')
ax2.set_zlabel('Number of cars')

# 顯示圖表
plt.show()

#下載圖片
fig2.savefig('/workspaces/cycu_ai2024/20240507/11272009_2_south.png')