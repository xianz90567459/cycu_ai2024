#/workspaces/cycu_ai2024/20240430/11272009_2.csv

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# 讀取CSV檔案
df = pd.read_csv('/workspaces/cycu_ai2024/20240430/11272009_2.csv')

# 找出18:00的資料
df_18pm = df[df['時間'] == 217]

# 選取需要的欄位
df_selected = df_18pm.iloc[:, [1, 2, 3, 8]]

# 提取北向的數據
df_north = df_selected[df_selected.iloc[:, 1] == 1]
x_north = df_north.iloc[:, 0]
y_north = df_north.iloc[:, 2]

# 使用CubicSpline來擬合北向的數據
cs_north = CubicSpline(x_north, y_north)

# 提取南向的數據
df_south = df_selected[df_selected.iloc[:, 1] == 2]
x_south = df_south.iloc[:, 0]
y_south = df_south.iloc[:, 2]

# 使用CubicSpline來擬合南向的數據
cs_south = CubicSpline(x_south, y_south)

# 繪製擬合後的曲線
x_min = min(x_north.min(), x_south.min())  # 找出最小值
x_max = max(x_north.max(), x_south.max())  # 找出最大值
x_new = np.linspace(x_min, x_max, 1000)  # 使用最小值和最大值來設定範圍

plt.figure(figsize=(10, 5))

# 繪製北向和南向的擬合曲線
plt.plot(x_new, cs_north(x_new), label='North Fitted')
plt.plot(x_new, cs_south(x_new), label='South Fitted')

# 繪製北向和南向的原始數據點
plt.scatter(x_north, y_north, label='North Original', color='blue', s=10)
plt.scatter(x_south, y_south, label='South Original', color='orange', s=10)

plt.title('North and South')
plt.xlabel('Mileage')  # 添加x軸標籤
plt.ylabel('Number of Cars')  # 添加y軸標籤
plt.legend()

# 儲存圖片
plt.savefig('/workspaces/cycu_ai2024/20240514/class/plot.png')

plt.show()