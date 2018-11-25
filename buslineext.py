import requests
import json
import csv
import time
import re
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Referer':'http://www.zhbuswx.com/busline/BusQuery.html?v=2.01',
    'Host':'www.zhbuswx.com',
    'X-Requested-With':'XMLHttpRequest'
}
line_url='http://www.zhbuswx.com/Handlers/BusQuery.ashx?handlerName=GetLineListByLineName&key='
for i in range(1,50):
    response=requests.get(line_url+str(i)+'A',headers=headers)
    response.encoding='utf-8'
    print(len(response.text))
    if '{"flag":1004}' in response.text:
        print('无%d路公交车' % i)
        continue
    elif len(response.text)==0:
        print('%d路查询失败' % i)
        continue
    else:
        data=response.text
        id=re.compile('"Id":"(.*?)"').findall(data)
        name=re.compile('"Name":"(.*?)"').findall(data)
        fromstation=re.compile('"FromStation":"(.*?)"').findall(data)
        tostation=re.compile('"ToStation":"(.*?)"').findall(data)
        begintime=re.compile('"BeginTime":"(.*?)"').findall(data)
        endtime=re.compile('"EndTime":"(.*?)"').findall(data)
        count=re.compile('"StationCount":(\d+)').findall(data)
        #print(data)
        print(id[0])
        print(name[0])
        print(fromstation[0])
        print(tostation[0])
        print(begintime[0])
        print(endtime[0])
        print(count[0])

        f=open('busline_ext.csv','a',encoding='utf-8')
        csv_in=csv.writer(f,dialect='excel')
        csv_in.writerow([id[0]+'A',name[0],fromstation[0],tostation[0],begintime[0],endtime[0],count[0]])
        print('%d路公交车数据已写入' % i)
    # print(data)
