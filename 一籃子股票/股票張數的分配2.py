import sqlite3

import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt
# 一籃子股票指數:
# 股價淨值比 0.1 < pb < 0.5
# 近三個月營收 > 近一年營收
# 回測驗證
# 計算 ROI 報酬率

# 如何買進
def portfolio(stock_list , money):
    # 取得最新股價
    conn = sqlite3.connect('../資料擷取/每日股價/財經資料庫.db')
    # 股價 >= 2021, 1, 4
    sql = '''
            SELECT 證券代號 , 交易日 ,收盤價 FROM price
            where 交易日 >= '%s'
        ''' % (tday)
    sql = sql.strip() # 去除空白
    sql = sql.replace('\n' , '')
    price = pd.read_sql(sql , conn , parse_dates=['date']).pivot(index='交易日',  columns='證券代號')['收盤價']
    # 得到stock_list 中的最新報價
    stock_list = price.iloc[-1][stock_list]

    # 考慮交易成本

    while True:
        # 平均每一檔股票可以有多少錢買入
        invest_money = (money / len(stock_list))
        # np.floor 往下取整數
        # Ex : -1.2 = -2  , 0.6 = 0 , 1.2 = 1 , 2.7 = 2
        # 取道整數的張數
        ret = np.floor(invest_money / stock_list / 1000)
        if(ret == 0 ).any(): #假設 ret 列表中有 0.0 的情況
            stock_list = stock_list[stock_list != stock_list.max()]
        else:
            break

        # 最終 portfolio 的結果
        # 總金額
    sum = (ret * stock_list * 1000).sum()
    # print(stock_list ,'\n建議買入張數 :' , ret ,'\n總投資金額 :', sum)
    return ret , sum

if __name__ == '__main__':
    # 這一天需要有交易
    tday = datetime.date(2021, 1, 4)
    conn = sqlite3.connect('../資料擷取/每日股價/財經資料庫.db')
    # 股價 >= 2021 1/4號
    sql = '''
           SELECT 證券代號 , 交易日 ,收盤價 FROM price
           where 交易日 >= '%s'
       ''' % (tday)
    # date -> index , stock_id -> column , 收盤價 -> data
    price = pd.read_sql(sql, conn, parse_dates=['交易日']).pivot(index='交易日', columns='證券代號')['收盤價']
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
    condition1 = pb.columns[(pb.iloc[0] > 5) & (pb.iloc[0] < 6)]
    # print('condition1 : ', condition1)  # 印出符合策略1的股票

    condition2 = rev.columns[rev.iloc[-3:].mean() > rev.iloc[-12:].mean()]
    # print('condition2 : ', condition2)  # 進3個月營收 > 進12月營收
    # condition1 & condition2(交集)
    cond = condition1.intersection(condition2)
    print('cond : ', cond)

    index = price[cond].mean(axis=1)
    # 指數
    diff = index.iloc[-1] - index.iloc[0]
    roi = diff/index.ilox[0]
    money = int(input('請輸入最大投資金額(萬)')) * 10000

    ret,sum = portfolio(cond, money)
    print('=============================================')
    print('買進標的張數 : ' , ret)
    print('買進標的的價格 : ' , price.iloc[-1][ret.index])
    print('實際投資金額 : ', sum)
    if(len(ret) >= 5):
        print('報酬率: %.2f%%' %(roi * 100))
    else:
        print('報酬率 : 無(股價不足五檔)')
