import matplotlib .pyplot as plt
import pandas as pd
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['simhei'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
data=pd.read_csv('busnumber.csv',encoding='gbk')
numberlist=data['number']
count=len(numberlist)
count_D=0
for number in numberlist:
    if number.endswith('D'):
        count_D+=1
print(count_D)
print(count)
print(count-count_D)
plt.title('珠海公交汽车数量KK制(总数：1118辆)',fontsize=16)
plt.style.use('ggplot')
plt.ylabel('数量')
plt.bar('新能源汽车',count_D,width=0.5,color='g',label='银隆新能源汽车(绿牌)')
plt.bar('燃油汽车',count-count_D,width=0.5,label='传统燃油汽车(黄牌)')
plt.ylim(0,800)
plt.legend()
plt.show()