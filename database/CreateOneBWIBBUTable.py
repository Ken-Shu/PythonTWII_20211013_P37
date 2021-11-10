import sqlite3
import time

import DataGet.BWIBBU as bwi

def create_table():
    sql = '''
            create table if not exists BWIBBU(
                id integer primary key not null,
                symbol varchar(20) not null,
                name varchar(20) not null,
                yield float not null,
                pe float not null,
                pb float not null,
                ts date 
              ) 
        '''
    conn = sqlite3.connect("tw_stock.db")
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()

def create_record(list):
    sql = "insert into BWIBBU(symbol,name,yield,pe,pb,ts) values(?,?,?,?,?,?)"
    conn = sqlite3.connect("tw_stock.db")
    cursor = conn.cursor()
    cursor.executemany(sql,list)
    conn.commit()
    conn.close()
    print('OK')
if __name__ == '__main__':
    list = bwi.getdata(2021,11,3)

    print(len(list),list)
    create_table()
    create_record(list)
    time.sleep(10)  # 每次爬完之後要停10秒
