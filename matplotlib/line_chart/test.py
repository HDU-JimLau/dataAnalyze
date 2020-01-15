#matplotlib 的基本要点
#matplotlib 的散点图、直方图、柱状图

# 任务
# 基本画图，设置图形大小，清晰度，设置X，Y轴刻度，展示图形，保存图形

#导包
from matplotlib import pyplot as plt



# x轴的值
x=range(2,26,2)
# y轴的值
y=[15,13,14.5,17,20,25,26,26,27,22,18,15]

# figure图形图标的意思，这里指我们画的图，通过实例化一个figure并且传递参数，能够在后台自动使用该figure实例
# figuresize是图片长宽，dpi越高图片越清晰
fig=plt.figure(figsize=(10,7),dpi=80)

#设置x轴的刻度
plt.xticks(range(1,26))
# 设置y轴的刻度
plt.yticks(range(min(y),max(y)+1))
#绘图
plt.plot(x,y)

#展示图形
plt.show()
#保存图形,可以保存为svg这种矢量图格式
plt.savefig("plt.png")


