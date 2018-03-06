#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import random as rd
import matplotlib.pyplot as plt



def op_rotate(Best,SE,alpha):
	n = Best.size
	Best = Best.reshape(n,1) # 重新定义，则为局部变量
	a = np.tile(Best,SE)
	b = np.dot(np.random.uniform(-1,1,(SE*n,n)),Best).reshape(n,SE)
	c = 1.0/n/(np.linalg.norm(Best) + 2e-16) # 需要加上一个极小数
	y = a + alpha * c * b
	y = y.transpose()
	return y

if __name__ == '__main__':
	Best = np.array([2,2])
	SE = 1000
	alpha = 1
	state = op_rotate(Best,SE,alpha)
	print(state)
	plt.plot(state[:,0],state[:,1],'g*')
	plt.plot(Best[0],Best[1],'or-')
	x = np.arange(Best[0]-alpha-0.1,Best[0]+alpha+0.1, 0.01)
	y = np.arange(Best[1]-alpha-0.1,Best[1]+alpha+0.1, 0.01)
	x, y = np.meshgrid(x,y)
	plt.contour(x, y, (x-Best[0])**2 + (y-Best[1])**2, [alpha]) # contour绘制的等值线
	plt.axis('equal')
	plt.show()