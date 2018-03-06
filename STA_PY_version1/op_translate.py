#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import random as rd
import matplotlib.pyplot as plt


def op_translate(oldBest,newBest,SE,beta):
	n = oldBest.size
	oldBest = oldBest.reshape(n,1)
	newBest = newBest.reshape(n,1)    # 定义局部变量
	# newBest.shape=(n,1)             # 实际为全局变量操作，在执行函数之后会产生永久性改变
	diff = (newBest - oldBest)
	a = np.tile(newBest,SE)
	b = beta/(np.linalg.norm(diff) + 2e-16) # 需要加上一个极小值
	c = np.tile(np.random.uniform(0,1,(1,SE)),n).reshape(n,SE)* np.tile(diff,SE)
	y = a + b * c
	y = y.transpose()
	return y

if __name__ == '__main__':
	oldBest = np.array([1,1])
	newBest = np.array([2,2])
	SE = 200
	beta = 1
	state = op_translate(oldBest,newBest,SE,beta)
	print(state)
	plt.plot(state[:,0],state[:,1],'g*-') # 画出各点
	Best = np.vstack((oldBest,newBest))  # 组合   newBest 和Best 仍然没有变，为行向量
	plt.plot(Best[:,0],Best[:,1],'ro-')  # 画出两点连线
	plt.plot(oldBest[0],oldBest[1],'ro-')# 画出旧点
	plt.plot(newBest[0],newBest[1],'ro-')# 画出新点
	plt.show()
