import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#skiprows跳过第一行，sep='\s+'列间间隔为空格。
data = pd.read_csv("20160621_BJ_BLNet.txt", skiprows=1, sep='\s+', header=None,
                   names=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o'])
print(data)
plt.scatter(data["h"], #横坐标
            data["g"], #纵坐标
            s = 1, #点的尺寸
            c = data["d"], cmap = 'jet') #点的颜色
plt.title("2016年6月21日0点-23点")
plt.xlabel("纬度")
plt.ylabel("经度")
plt.rcParams['font.sans-serif'] = ['SimHei'] #显示中文
plt.rcParams['axes.unicode_minus'] = False #正常显示负号
plt.colorbar() #绘制颜色对照条
plt.show() #显示所绘图形