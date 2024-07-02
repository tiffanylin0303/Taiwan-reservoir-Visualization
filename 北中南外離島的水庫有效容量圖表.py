#北中南外離島的水庫有效容量圖表

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

# 設定字體
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei'] # 使用中文字體
plt.rcParams['axes.unicode_minus'] = False  # 解決座標軸負號顯示問題

#北部
objects_n = ('翡翠水庫', '石門水庫', '寶山第二水庫', '新山水庫', '大埔水庫', '寶山水庫','西勢水庫')
y_pos = np.arange(len(objects_n))
performance_n = [36997.57, 20526.01, 3147.18, 995.96, 529.90, 500.83, 39.57]

plt.bar(y_pos, performance_n, align='center', alpha=0.5)
plt.xticks(y_pos, objects_n)

plt.ylabel('有效容量(萬立方公尺)')
plt.title('北部水庫有效容量圖表')
plt.xlabel('水庫名稱')
plt.figure(figsize=(20, 12))
plt.show()

#中部
objects_m = ('德基水庫', '日月潭水庫', '鯉魚潭水庫', '湖山水庫', '霧社水庫', '永和山水庫','明德水庫','石岡壩')
y_pos = np.arange(len(objects_m))
performance_m = [18866.03, 12949.09, 11550.54, 5060.76, 2868.56, 2993.5, 1250.98, 143.28]

plt.bar(y_pos, performance_m, align='center', alpha=0.5)
plt.xticks(y_pos, objects_m, fontsize = 10)
plt.xlabel('水庫名稱')
plt.ylabel('有效容量(萬立方公尺)')
plt.title('中部水庫有效容量圖表')
plt.figure(figsize=(15, 10))
plt.show()

#南部
objects_s = ('曾文水庫', '南化水庫', '烏山頭水庫', '牡丹水庫', '仁義潭水庫', '阿公店水庫','白河水庫','蘭潭水庫','鳳山水庫', '澄清湖水庫', '鏡面水庫')
y_pos = np.arange(len(objects_s))
performance_s = [50474.63, 8920.11, 7846.77, 2652.09, 2480.27, 1502.7, 1387.5, 921.8, 716.04, 259.5, 97.61]

plt.bar(y_pos, performance_s, align='center', alpha=0.5)
plt.xticks(y_pos, objects_s, fontsize = 10)

plt.ylabel('有效容量(萬立方公尺)')
plt.xlabel('水庫名稱')
plt.title('南部水庫有效容量圖表')
plt.figure(figsize=(15, 10))
plt.show()

#外離島
objects_o = ('成功水庫', '興仁水庫', '太湖水庫', '田埔水庫', '金沙水庫', '后沃水庫')
y_pos = np.arange(len(objects_o))
performance_o = [121.1, 72.1, 148.1, 48.6, 43.5, 41.6]

plt.bar(y_pos, performance_o, align='center', alpha=0.5)
plt.xticks(y_pos, objects_o)
plt.xlabel('水庫名稱')
plt.ylabel('有效容量(萬立方公尺)')
plt.title('外離島水庫有效容量圖表')
plt.figure(figsize=(15, 10))
plt.show()
