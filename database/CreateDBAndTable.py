import sqlite3

conn = sqlite3.connect("tw_stock.db")
create_table_sql ='''
create table if not exists portfolio(
    id integer not null primary key autoincrement,
    symbol text not null,
    cost float,
    amount integer,
    ts date
    )
'''
cursor = conn.cursor()
cursor.execute(create_table_sql)
print('Table 建立完成')
conn.commit()
conn.close()