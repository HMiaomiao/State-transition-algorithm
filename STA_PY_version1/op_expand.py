#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import random as rd
import matplotlib.pyplot as plt


def op_expand(Best,SE,gamma):
	n = Best.size # 数组中元素的个数,不能用len，因为下一个best为矩阵形式，len[[1,2]] = 1
	Best = Best.reshape(n,1)
	a = np.tile(Best,SE)
	b = np.array([rd.gauss(0,1) for _ in range(n*SE)]).reshape(n,SE)
	y = a + gamma * b * a
	y = y.transpose()
	return y

if __name__ == '__main__':
	Best = np.array([2,2])
	SE = 1000
	gamma = 1
	state = op_expand(Best,SE,gamma)
	print(state)
	plt.plot(state[:,0],state[:,1],'g*')
	plt.plot(Best[0],Best[1],'or-')
	plt.axis('equal')
	plt.show()
