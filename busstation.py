import pandas as pd
import csv
import requests
import re
import time
url='http://www.zhbuswx.com/Handlers/BusQuery.ashx?handlerName=GetStationList&lineId='
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Referer':'http://www.zhbuswx.com/busline/BusQuery.html?v=2.01',
    'Host':'www.zhbuswx.com',
    'X-Requested-With':'XMLHttpRequest'
}
data=pd.read_csv('fail_ext3.csv',encoding='gbk')
#print(data['id'])
for line_id in data['id']:
    print(line_id)
    data=requests.get(url+line_id+'&_=1540969126228',headers=headers)
    if len(data.text)==0:
        print('id:%s 查询失败' % line_id)
        f=open('fail_ext4.csv','a',encoding='utf-8')
        csv_in=csv.writer(f,dialect='excel')
        csv_in.writerow([line_id])
    else:
        data=data.text

        idlist=re.compile('"Id":"(.*?)"').findall(data)
        namelist=re.compile('"Name":"(.*?)"').findall(data)
        lnglist=re.compile('"Lng":"(.*?)"').findall(data)
        latlist=re.compile('"Lat":"(.*?)"').findall(data)
        print(idlist)
        print(namelist)
        print(lnglist)

        for i in range(len(idlist)):
            id=idlist[i]
            name=namelist[i]
            lng=lnglist[i]
            lat=latlist[i]
            f = open('success_ext4.csv', 'a', encoding='utf-8')
            csv_in = csv.writer(f, dialect='excel')
            csv_in.writerow([id,name,lng,lat])



