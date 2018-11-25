import pandas as pd
import csv
import requests
import re
import time
from datetime import datetime
url=''
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Referer':'http://www.zhbuswx.com/busline/BusQuery.html?v=2.01',
    'Host':'www.zhbuswx.com',
    'X-Requested-With':'XMLHttpRequest'
}

data=pd.read_csv('busline.csv',encoding='gbk')
linelist=data['line']
fromlist=data['from']
tolist=data['to']
fail_count=0
success_count=0
for i in range(len(linelist)):
    line=linelist[i]
    fromstation=fromlist[i]
    tostation=tolist[i]
    print(line)

    stationlist=[fromstation,tostation]
    print(stationlist)
    for j in stationlist:
        response=requests.get('http://www.zhbuswx.com/Handlers/BusQuery.ashx?handlerName=GetBusListOnRoad&lineName='+str(line)+'路'+'&fromStation='+j)
        if len(response.text)==0:
            print('始发站：%s 查询失败！' % (j))
            fail_count+=1
            continue
        else:
            print('始发站：%s 成功！' % (j))
            response=response.text
            print(response)
            numberlist=re.compile('"BusNumber":"(.*?)"').findall(response)
            success_count=len(numberlist)

            # for number in numberlist:

                # f = open('busnumber_ext.csv', 'a', encoding='utf-8')
                # csv_in = csv.writer(f, dialect='excel')
                # csv_in.writerow([str(line)+'路',number])

count=fail_count*5+success_count
print(str(count))