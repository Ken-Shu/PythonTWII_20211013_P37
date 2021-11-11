'''
同時繪出2檔股票的本益比走勢圖
ex 2330 vs 2303
'''
import sqlite3
import matplotlib.pyplot as plt

symbol = '2330'
symbol2 = '2303'
conn = sqlite3.connect('tw_stock.db')
cursor = conn.cursor()
sql = "SELECT ts ,name , pe ,symbol from BWIBBU where (symbol =%s)OR (symbol = %s)  ORDER BY symbol"%(symbol,symbol2)
cursor.execute(sql)
datas = cursor.fetchall()
print(datas)
#繪圖前準備
x_data = [] #x軸時間序列資料
y_data = [] #y軸本益比序列資料 2330
y2_data = [] #y軸本益比序列資料 2327

for data in datas:
    if(data[3] == symbol2):
        x_data.append(data[0])
        y2_data.append(data[2])
    else:
        y_data.append(data[2])

print(len(x_data))
print(len(y_data))
print(len(y2_data))

#繪圖
fig , ax1 = plt.subplots()
ax2 = ax1.twinx()
plt.title('%s and %s Stock Info'%(symbol,symbol2))
plt.xlabel('date')
#第一條線
ax1.set_ylabel('pe', color='tab:blue')
ax1.plot_date(x_data, y_data ,'-',color='blue')
#第二條線
ax2.set_ylabel('pe', color='tab:blue')
ax2.plot_date(x_data, y2_data ,'-',color='orange')
plt.grid(True)
plt.show()