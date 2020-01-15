import matplotlib
from matplotlib import pyplot as plt
from pylab import mpl



#设置显示中文
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

x=range(11,31)
y=[1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]

# plt.figure(figsize=(10,8),dpi=80)
plt.plot(x,y)

x_lable=["{}岁".format(i) for i in x]
plt.xticks(x,x_lable,rotation=45)

plt.yticks(range(min(y),max(y)+1))

plt.xlabel("年龄")
plt.ylabel("女朋友的个数")
plt.title("11岁到30岁女朋友的波动变化表")
#设置网格,alpha设置网格清晰度
plt.grid(alpha=0.5)
plt.show()