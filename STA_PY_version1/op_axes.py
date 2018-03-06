#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import random as rd
import matplotlib.pyplot as plt

def op_axes(Best,SE,delta):
	n = Best.size
	A = np.zeros((n,SE))
	index = np.random.randint(0,n,(1,SE))
	A[index,list(range(SE))] = 1
	Best = Best.reshape(n,1)
	a = np.tile(Best,SE)
	b = np.array([rd.gauss(0,1) for _ in range(n*SE)]).reshape(n,SE)
	c = delta*b*A*a
	y = a + c
	y = y.transpose()
	return y

if __name__ == '__main__':
	Best = np.array([2,2])
	SE = 200
	delta = 1
	state = op_axes(Best,SE,delta)
	print(state)
	plt.plot(state[:,0],state[:,1],'g*')
	plt.plot(Best[0],Best[1],'or')
	plt.axis('equal')
	plt.show()
