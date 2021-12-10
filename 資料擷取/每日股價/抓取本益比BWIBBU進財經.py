from datetime import date , datetime ,timedelta
import DataGet.BWIBBU as bwi
import database.CreateOneBWIBBUTable as bwibbu
import time
if __name__ == '__main__':
    today = date.today()
    begin_day = date(2021, 11, 30)
    print(today, begin_day)
    diff = today-begin_day
    print('diff:', diff)

    for single_date in (begin_day + timedelta(n) for n in range (diff.days+1)):
        print(single_date.strftime("%Y"),single_date.strftime("%m"),single_date.strftime("%d"))
        yyyy=single_date.strftime("%Y")
        mm=single_date.strftime("%m")
        dd=single_date.strftime("%d")
        list = bwi.getdata(yyyy, mm, dd)
        #print(len(list), list)
        bwibbu.create_table()
        bwibbu.create_record(list)
        time.sleep(7)  # 每次爬完之後要停10秒