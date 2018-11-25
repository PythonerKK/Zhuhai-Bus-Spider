import matplotlib .pyplot as plt
import pandas as pd
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['simhei'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
# data=pd.read_csv('success_station.csv',encoding='gbk')
#
# data=data.head(10)
# print(data)
# plt.style.use('ggplot')
# plt.bar(data['name'],data['count'])
# plt.title('珠海公交站点日均客流量前10位(总站点数：1840)KK',fontsize=16,color='blue')
# plt.xticks(rotation=20)
# plt.ylabel('比例系数')
# plt.show()

data=pd.read_csv('busline.csv',encoding='gbk')
data=data.head(10)
data['line']=data['line'].apply(lambda x:str(x)+'路')
print(data)
plt.bar(data['line'],data['count'])
plt.title('珠海公交途径站点最多线路（TOP10）',fontsize=16)
plt.show()