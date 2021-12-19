import sqlite3
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import matplotlib as mat

# 一籃子股票指數:
# 股價淨值比 0.1 < pb < 0.5
# 近三個月營收 > 近一年營收
# 回測驗證
# 計算 ROI 報酬率

if __name__ =='__main__':

    # 這一天需要有交易
    tday = datetime.date(2021, 1, 4)
    conn = sqlite3.connect('../資料擷取/每日股價/財經資料庫.db')
    # 股價 >= 2021 1/4號
    sql = '''
        SELECT 證券代號 , 交易日 ,收盤價 FROM price
        where 交易日 >= '%s'
    ''' % (tday)
    # date -> index , stock_id -> column , 收盤價 -> data
    price = pd.read_sql(sql , conn, parse_dates=['交易日']).pivot(index='交易日',columns='證券代號')['收盤價']
    # print(price)

    # PB 股價淨值比
    sql = '''
            SELECT CAST(symbol as varchar(10)) as 證券代號 ,ts as 交易日 ,pb FROM BWIBBU
            where 交易日 >= '%s'
        ''' % (tday)
    pb = pd.read_sql(sql, conn, parse_dates=['交易日']).pivot(index='交易日', columns='證券代號')['pb']
    # print(pb)

    # 當月營收 < 2021 1/4號
    sql = '''
            SELECT CAST(證券代號 as varchar(10)) as 證券代號 ,交易日,當月營收 FROM monthly_report
            where 交易日 >= '%s'
        ''' % (tday)
    rev = pd.read_sql(sql, conn, parse_dates=['交易日']).pivot(index='交易日', columns='證券代號')['當月營收']
    # print(rev)

    # 策略條件
    condition1 = pb.columns[(pb.iloc[0] > 0.1) & (pb.iloc[0] < 0.5)]
    print("condition1:", condition1)  # 印出符合策略1的股票
    condition2 = rev.columns[rev.iloc[-3:].mean() > rev.iloc[-12:].mean()]
    print("condition2:", condition2)  # 近 3 個月月營收 > 近 12 個月月營收
    # condition1 & condition2 (交集)
    cond = condition1.intersection(condition2)
    print("cond:", cond)

    # 編指數
    index = price[cond].mean(axis=1)
    print(index)

    # ROI
    diff = index.iloc[-1] - index.iloc[0]
    roi = diff / index.iloc[0]
    print(diff, roi)

    print(mat.matplotlib_fname())
    print(mat.get_cachedir)

    plt.rcParams['font.sans-serif'] = 'SimHei'
    plt.rcParams['axes.unicode_minus'] = False
    # 繪圖
    index.plot()
    # 設定字體
    plt.show()
