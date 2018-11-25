import matplotlib .pyplot as plt
import pandas as pd
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['simhei'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
data=pd.read_csv('success.csv',encoding='gbk')
xiangzhou=data[data['lng']>113.42]
doumen=data[(data['lat']>=22.2) & (data['lng']<113.42)]
jinwan=data[(data['lat']<22.2) & (data['lng']<113.42)]
print(xiangzhou['lng'])
print(xiangzhou['lat'])
# img=plt.imread('zhuhai.png')

plt.title('珠海公交站点分布图KK制(共1156个公交站)',fontsize=16)
plt.xlabel('经度')
plt.ylabel('纬度')

plt.scatter(xiangzhou['lng'],xiangzhou['lat'],15,c='b',label='香洲区',marker='+')
plt.scatter(doumen['lng'],doumen['lat'],15,c='r',label='斗门区',marker='>')
plt.scatter(jinwan['lng'],jinwan['lat'],15,c='g',label='金湾区',marker='^')
plt.legend()

# plt.imshow(img)
plt.show()