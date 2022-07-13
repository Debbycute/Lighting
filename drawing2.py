import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#skiprows跳过第一行，sep='\s+'列间间隔为空格。
data = pd.read_csv("20160621_BJ_BLNet.txt", skiprows=1, sep='\s+', header=None,
                   names=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o'])
print(data)
plt.scatter(data["d"], #横坐标
            data["i"],#纵坐标
            s = 1)
plt.title("2016年6月21日0点-23点")
plt.xlabel("时间/h")
plt.ylabel("对地高度/km")
plt.rcParams['font.sans-serif'] = ['SimHei'] #显示中文
plt.rcParams['axes.unicode_minus'] = False #正常显示负号
plt.show() #显示所绘图形