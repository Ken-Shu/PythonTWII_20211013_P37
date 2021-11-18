import time
from datetime import date ,datetime , timedelta
import DataGet.抓取每日股價3_寫入工具 as writeutil


begin_day = date(2011,1,1)
today = date.today()
print(begin_day , today)
diff = today - begin_day
print(diff)

for single_date in (begin_day + timedelta(n) for n in range(diff.days+1)):
    print(single_date.strftime("%Y"), single_date.strftime("%m"), single_date.strftime("%d"))
    yyyy = single_date.strftime("%Y")
    mm = single_date.strftime("%m")
    dd = single_date.strftime("%d")
    print(yyyy, mm, dd)
    try:
        writeutil.dataget(yyyy, mm, dd)
    except:
        print('無資料')
    time.sleep(7)