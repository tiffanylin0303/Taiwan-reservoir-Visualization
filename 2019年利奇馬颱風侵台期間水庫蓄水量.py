import matplotlib.pyplot as plt
import numpy as np


# 設定字體
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei'] # 使用中文字體
plt.rcParams['axes.unicode_minus'] = False  # 解決座標軸負號顯示問題

time = ['08-03', '08-04', '08-05', '08-06', '08-07', '08-08', '08-09', '08-10', '08-11', '08-12']
water1 = [70.43, 70.15, 69.96, 69.23, 67.67, 66.89, 73.61, 75.07, 75.24, 75.09]
water2 = [75.77, 75.98, 75.8, 75.26, 73.51, 71.37, 69.05, 77.37, 84.56, 89.97]
water3 = [84.68, 85.42, 86.04, 86.11, 85, 85.71, 83.21, 87.58, 94.95, 90.66]
water4 = [97.61, 97.61, 97.61, 97.61, 97.61, 97.61, 97.61, 97.61, 97.61, 97.61]
plt.plot(time, water1, 'b', label='翡翠水庫')
plt.plot(time, water2, 'r', label='德基水庫')
plt.plot(time, water3, 'c', label='曾文水庫')
plt.plot(time, water4, 'g', label='太湖水庫')
plt.xlabel('Date') # 設定x軸標題
plt.ylabel('百分比(%)') # 設定x軸標題
plt.xticks(time, fontsize = 8) # 設定x軸label以及垂直顯示
plt.yticks(fontsize = 8) # 設定x軸label以及垂直顯示
plt.title("2019年利奇馬颱風侵台期間水庫蓄水量") # 設定圖表標題
plt.legend(loc = 'best', prop = {'size': 10})
plt.figure(figsize=(20, 15))
plt.show()



