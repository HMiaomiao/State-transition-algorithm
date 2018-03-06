#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import random as rd
import math

from rotate import *
from expand import *
from axesion import *
from Benchmark import Sphere


def STA(funfcn,Best,SE,Range,Iterations):
	alpha_max = 1
	alpha_min = 1e-4
	alpha = alpha_max
	beta = 1
	gamma = 1
	delta = 1
	fc = 2
	history = np.empty((Iterations,1))
	fBest = funfcn(Best[0])            # 用一种奇怪的方式调用矩阵中的数 

	for iter in range(Iterations):
		Best,fBest = expand(funfcn,Best,fBest,SE,Range,beta,gamma)
		Best,fBest = rotate(funfcn,Best,fBest,SE,Range,alpha,beta)
		Best,fBest = axesion(funfcn,Best,fBest,SE,Range,beta,delta)
		history[iter] = fBest
		alpha = alpha/fc if alpha > alpha_min else alpha_max

	return Best,fBest,history

if __name__ == '__main__':
	funfcn = Sphere
	SE = 10
	# Best0 = np.array([2,2,2,2,2])
	# n = Best0.size
	# Range = np.tile([[-30],[30]],n)
	Dim = 10
	Range = np.repeat([-30,30],Dim).reshape(2,Dim)
	print(Range)
	Best0 = Range[0,:] + (Range[1,:]-Range[0,:]*np.random.uniform(0,1,(1,Dim)))
	print(Best0)

	Iterations = 1000
	Best,fBest,history = STA(funfcn,Best0,SE,Range,Iterations)
	print(Best,fBest)