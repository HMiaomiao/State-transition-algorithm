#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import random as rd
from op_rotate import *
from Benchmark import Sphere


def fitness(funfcn,State):
	SE = State.shape[0]
	fState = np.empty((SE,1)) # 函数empty创建一个内容随机并且依赖与内存状态的数组
	fState = list(map(funfcn,State)) # 调用
	fGBest = np.min(fState)
	Best = State[fState.index(fGBest)] # 这个列表中第一次此值的索引
	return Best,fGBest


if __name__ == '__main__':
	funfcn = Sphere
	Best = np.array([2,2])
	SE = 4
	alpha = 1
	State = op_rotate(Best,SE,alpha)
	print(State)
	newBest,fGBest = fitness(funfcn,State)
	print(newBest,fGBest)