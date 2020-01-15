from matplotlib import pyplot as plt
from pylab import mpl
import random

# 任务
# 设置坐标轴显示中文，显示角度,添加x轴y轴的描述信息,设置显示点的网格
# 直接google去找方法“matplotlib如何设置显示中文”就可以设置



#设置显示中文
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

x=range(0,120)
y=[random.randint(20,35) for i in range(120)]

plt.figure(figsize=(20,8),dpi=200)

plt.plot(x,y)

x_lable=["10点{}分".format(i) for i in range(0,60)]
x_lable+=["11点{}分".format(i) for i in range(0,60)]
print(x_lable)
#让列表x中的数据和x_lable上的数据都传入，最终会在x轴上一一对应的显示出来
#两组数据的长度必须一样，否则不能完全覆盖整个轴
#使用列表切片，每隔5个选一个数据进行展示
#为了让字符串不会覆盖，使用rotation选项，让字符串旋转90度
plt.xticks(x[::5],x_lable[::5],rotation=45)

#添加描述信息
plt.xlabel("时间")
plt.ylabel("温度")
plt.title("10点到12点每分钟的气温变化情况")
#绘制网格
plt.grid(alpha=0.5)
plt.savefig("test.png")
plt.show()
