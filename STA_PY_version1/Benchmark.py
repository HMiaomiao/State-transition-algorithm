#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce
from operator import mul
import numpy as np
import math

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt


def Sphere(s):
	square = map(lambda y: y * y ,s)
	return sum(square)

def Rosenbrock(s):
	square = map(lambda x, y: 100 * (y - x**2)**2 + (x - 1)**2 , s[:len(s)-1],s[1:len(s)])
	return  sum(square)

def Rastrigin(s):
	square = map(lambda x: x**2 - 10 * math.cos(2*math.pi*x) + 10, s)
	return  float(sum(square))

def Michalewicz(s):
	n = len(s)
	t1 = -sum(map(lambda x, y: math.sin(x) * (math.sin( y*x**2/math.pi ))**20, s, range(1,n+1)))
	return t1

def Griewank(s): 
	t1 = sum(map(lambda x: 1/4000 * x**2, s))
	n = len(s)
	t2 = map(lambda x, y: math.cos(x/np.sqrt(y)), s, range(1,n+1))
	t3 = reduce(mul, t2)
	return t1 - t3 + 1
	
if __name__ == '__main__':
	s = [[8,9]][0]       # 将其转换为list
	func = Michalewicz

	print(func(s))


	# 画三维图
	fig = plt.figure()
	ax = fig.gca(projection='3d')  # 创建画布，get current axis
	X = Y = np.arange(0, 3.5, 0.05)
	X, Y = np.meshgrid(X, Y)       # 创建网格
	Z = np.empty(X.shape)
	for l in range(len(X[1])):
		for h in range(len(Y[1])):
			Z[h,l] = func(np.append(X[h,l],Y[h,l])) # Z共有80*80个点
	surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,linewidth=0, antialiased=False) 
	# 行、列、颜色分配图、antialiased 曲线的反锯齿效果 linewidth 线宽
	# ax.set_zlim(-1.01, 1.01) # 设置z轴刻度
	fig.colorbar(surf, shrink=0.5, aspect=5) # 调整调色板 调整长度和刻度值
	plt.show()