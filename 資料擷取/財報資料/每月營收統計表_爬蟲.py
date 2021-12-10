import sqlite3

import requests
import pandas as pd
import time
from io import StringIO

def get_monthly_report(year,month):
    url = 'https://mops.twse.com.tw/nas/t21/sii/t21sc03_%d_%d_0.html' % (year-1911, month)
    # 抓取網頁
    r = requests.get(url)
    # 編碼 (如果看不到中文 就加入以下編碼 : big5 或 utf-8)
    r.encoding= 'big5'
    # 把網頁資料透過StringIO包裝成一個檔案給 pandas 讀取
    # 要安裝 lxml 套件 for import StringIO
    dfs = pd.read_html(StringIO(r.text))

    # 顯示所有列
    pd.set_option('display.max_columns', None)
    # 顯示所有欄
    pd.set_option('display.max_rows', None)
    # 設定欄寬
    pd.set_option('display.width', 5000)

    '''
    for df in dfs:
        if df.shape[1] == 11:
            print(df.shape)
            print(df)
    #轉換 不加[]就只會印出物件
    print([df for df in dfs if df.shape[1] == 11])
    '''
    df = pd.concat(df for df in dfs if df.shape[1] == 11)
    # 設定 columns 名稱
    # print(df.columns.get_level_values(0))
    # print(df.columns.get_level_values(1)) #這是我們要的欄位
    df.columns = df.columns.get_level_values(1)
    # print(df)

    # 過濾資料
    # 刪除公司代號欄位中有出現 合計 或 總計 的列
    df = df[df['公司代號'] != '合計']
    df = df[df['公司代號'] != '總計']
    # 當月營收不能變成數字的以 NAN 取代 (error = 'coerce')
    df['當月營收'] = pd.to_numeric(df['當月營收'], 'coerce')
    #print(df)
    # 將交易日與公司代號共列 df 的 indexes
    df['交易日'] = '%d-%d-10' % (year, month)
    df = df.set_index(['交易日', '公司代號'])
    #變更 index 名稱
    df.index.names = ['交易日', '證券代號']
    return df

def import_monthly_report(df,db_path):
    # 將 df 存成 CSV
    df.to_csv('monthly_report.csv', encoding='utf_8_sig')
    # csv 轉 df 並指定 index
    df = pd.read_csv('monthly_report.csv',index_col=['交易日','證券代號'])
    # 存入 sqlite
    conn = sqlite3.connect(db_path)
    df.to_sql('monthly_report', conn , if_exists='append')

#測試
def test():
    year = 2021
    month = 10
    df = get_monthly_report(year, month)
    print(df)
    # 匯入資料庫
    import_monthly_report(df , '財報_Test.db')

if __name__ == '__main__':
    # test()
    for year in range(2019 , 2021+1):
        for month in range(1, 12+1):
            time.sleep(7)
            try:
                df = get_monthly_report(year, month)
                print(df)
                # 匯入資料庫
                import_monthly_report(df, '../每日股價/財經資料庫.db')
                print(year, month, "OK")
            except Exception as e:
                print(year, month ,"Fail:",str(e))