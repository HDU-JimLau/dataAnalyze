from matplotlib import pyplot as plt
from pylab import mpl


# 任务
# 多个折线时候，添加图例,设置线条样式

#设置显示中文
mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
x=range(11,31)
a=[1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
b=[1,0,3,1,2,2,3,3,2,1,2,1,1,1,1,1,1,1,1,1]

plt.figure(dpi=200)

# label 设置标记 color 设置线条颜色 linestyle 设置线条形状 linewidth设置线条宽度 ,alpha 设置线条清晰度
plt.plot(x,a,label="自己",color="blue",linestyle=":",linewidth=2,alpha=0.2)
plt.plot(x,b,label="同桌",color="black")

x_labe=["{}岁".format(i) for i in  x]
plt.xticks(x,x_labe,rotation=45)
plt.yticks(range(min(a),max(a)+1))

plt.xlabel("年龄")
plt.ylabel("女朋友个数")
plt.title("女朋友个数变化表")
plt.grid(alpha=0.8,linestyle=":")

# 添加图例,注意需要在plt.plot()中添加参数,label="标记"
plt.legend()

plt.show()