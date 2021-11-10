import sqlite3
import matplotlib.pyplot as plt
symbol = '2330'
conn = sqlite3.connect('tw_stock.db')
cursor = conn.cursor()
sql = "select ts,pe,yield from BWIBBU where symbol='%s'" %symbol

cursor.execute(sql)
datas = cursor.fetchall()
print(datas)
#繪圖前準備
x_data = [] #x軸時間序列資料
y_data = [] #y軸本益比序列資料
y2_data = [] #y軸殖利率序列資料
for data in datas:
    x_data.append(data[0])
    y_data.append(data[1])
    y2_data.append(data[2])
print(x_data)
print(y_data)
print(y2_data)
#繪圖
fig , ax1 = plt.subplots()
ax2 = ax1.twinx()
plt.title('%s Stock Info'%symbol )
plt.xlabel('date')
#第一條線
ax1.set_ylabel('pe', color='tab:blue')
ax1.plot_date(x_data, y_data ,'-',color='blue')
#第二條線
ax2.set_ylabel('pe', color='tab:blue')
ax2.plot_date(x_data, y2_data ,'-',color='orange')
plt.grid(True)
plt.show()