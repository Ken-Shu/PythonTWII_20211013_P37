import sqlite3
import matplotlib.pyplot as plt
symbol = '2330'
kind = 'yield'
conn = sqlite3.connect('tw_stock.db')
cursor = conn.cursor()
sql = 'select strftime("%Y-%m", ts) as "ts", ROUND(AVG('+kind+'), 2) as "'+kind+'" ' \
      'from BWIBBU  ' \
      'where symbol="' + symbol + '" ' \
      'group by strftime("%Y-%m", ts)'

cursor.execute(sql)
datas = cursor.fetchall()
print(datas)
#繪圖前準備
x_data = [] #軸時間序列資料
y_data = [] #軸本益比序列資料
for data in datas:
    x_data.append(data[0])
    y_data.append(data[1])
print(x_data)
print(y_data)
#繪圖
plt.plot_date(x_data , y_data,'-')
plt.title('%s Stock Info %s' %(symbol,kind) )
plt.xlabel('date')
plt.ylabel('PE')
plt.grid(True)
plt.show()