import re
import time

from io import StringIO
import pandas as pd
import requests.packages.urllib3
import requests
requests.packages.urllib3.disable_warnings()
headers = {'User-Agent' : 'chrome'}
# 紀錄網頁端的 session 值
rs = requests.session()

# 取得驗證碼
def get_code2(rs):

    res = rs.get('https://bsr.twse.com.tw/bshtm/bsMenu.aspx',verify=False,stream=True, headers=headers)
    #print(res.text)
    # 透過 re 正則表示式來抓取
    viewstate = re.search('__VIEWSTATE"\s+value=.*=',res.text)
    # print("viewstate obj : " , viewstate)
    # print("viewstate.group(0):" , viewstate.group(0))
    # print("viewstate.group(0)[20:]:", viewstate.group(0)[20:])
    viewstate = viewstate.group(0)[20:]

    eventvalidation = re.search('__EVENTVALIDATION"\s+value=.*\w', res.text)
    # print("eventvalidation obj : " , eventvalidation)
    # print("eventvalidation.group(0):" , eventvalidation.group(0))
    # print("eventvalidation.group(0)[26:]:", viewstate.group(0)[26:])
    eventvalidation = eventvalidation.group(0)[26:]

    return viewstate , eventvalidation
# 傳送資料 (表單)

def send_data2(rs, stock_id , viewstate , eventvalidation):
    payload = {
        '__EVENTTARGET': '',
        '__EVENTARGUMENT': '',
        '__LASTFOCUS': '',
        '__VIEWSTATE': viewstate,
        '__EVENTVALIDATION': eventvalidation,
        'RadioButton_Normal': 'RadioButton_Normal',
        'TextBox_Stkno': stock_id,
        'CaptchaControl1 ': '8AJFA',
        'btnOK': '%E6%9F%A5%E8%A9%A2',
    }
    # 模擬按下查詢
    rs.post("https://bsr.twse.com.tw/bshtm/bsMenu.aspx",data=payload,headers=headers, stream=True)
    # 停1秒
    time.sleep(1)
    res = rs.get("https://bsr.twse.com.tw/bshtm/bsContent.aspx",verify=False , stream=True)
    return res

def parse_data2(text):
        lines = text.spilt('\n')
        lines = [line for line in lines if len(line.spilt(',')) == 11]
        df = pd.read_csv(StringIO('\n').join(lines))
        one_df = df[df.columns[:5]]
        two_df = df[df.columns[6:]]
        two_df.columns = two_df.columns.str.replace('.1', '', regex=True)
        df = one_df.append(two_df)
        # 刪除序號欄位
        df.set_index('序號').sort_index().dropna()
        return df
if __name__ == '__main__':
    pd.set_option('display.max_rows',None)

    viewstate , eventvalidation = get_code2(rs)
    print('viewstate = ' + viewstate )
    print('eventvalidation = ' + eventvalidation)

    res = send_data2(rs, '2327', viewstate, eventvalidation)
    res.encoding = 'big5'
    open('test1.txt' , 'w' , encoding='utf-8').write(res.text)

    #df = parse_data2(res.text)
