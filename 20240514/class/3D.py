#/workspaces/cycu_ai2024/20240430/11272009_2.csv

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import CubicSpline

# 讀取CSV檔案
df = pd.read_csv('/workspaces/cycu_ai2024/20240430/11272009_2.csv')

# 選取需要的欄位
df_selected = df.iloc[:, [0, 1, 2, 3, 8]]


# 找出所有的時間段
times = df_selected.iloc[:, 0].unique()


# 提取北向和南向的數據
df_north = df_selected[df_selected.iloc[:, 2] == 1]
df_south = df_selected[df_selected.iloc[:, 2] == 2]

# 顯示提取的數據
print(df_north)
print(df_south)

for time in times:
    # 提取特定時間的數據
    df_time_north = df_north[df_north.iloc[:, 0] == time]
    df_time_south = df_south[df_south.iloc[:, 0] == time]

    # 使用CubicSpline來擬合數據
    cs_north = CubicSpline(df_time_north.iloc[:, 1], df_time_north.iloc[:, 3])
    cs_south = CubicSpline(df_time_south.iloc[:, 1], df_time_south.iloc[:, 3])

    # 計算新的x值
    x_new = np.linspace(df_time_north.iloc[:, 1].min(), df_time_north.iloc[:, 1].max(), 500)

    # 繪製擬合曲線
    plt.plot(x_new, cs_north(x_new), label=f'North Fitted {time}')
    plt.plot(x_new, cs_south(x_new), label=f'South Fitted {time}')


import numpy as np
from scipy.interpolate import griddata
from mpl_toolkits.mplot3d import Axes3D

# 將數據轉換為numpy數組
data = np.concatenate([df_north.iloc[:, [0, 1, 3]].values, df_south.iloc[:, [0, 1, 3]].values])

# 創建網格
grid_x, grid_y = np.mgrid[min(data[:, 0]):max(data[:, 0]):100j, min(data[:, 1]):max(data[:, 1]):100j]

# 進行插值
grid_z = griddata(data[:, :2], data[:, 2], (grid_x, grid_y), method='linear')

# 創建四個視圖角度
views = [(30, 45), (30, 135), (30, 225), (30, 315)]

# 創建一個新的圖形
fig = plt.figure(figsize=(12, 12))

# 繪製四個視圖
for i, view in enumerate(views, 1):
    ax = fig.add_subplot(2, 2, i, projection='3d')
    ax.plot_surface(grid_x, grid_y, grid_z, color='blue', alpha=0.5)
    ax.view_init(*view)
    ax.set_xlabel('Time')
    ax.set_ylabel('Mileage')
    ax.set_zlabel('Number of Cars')
    ax.set_title(f'View {i}')

# 添加大標題
plt.suptitle('11272009', fontsize=16)

# 儲存圖片
plt.savefig('/workspaces/cycu_ai2024/20240514/class/3D.png')

# 顯示圖形
plt.show()