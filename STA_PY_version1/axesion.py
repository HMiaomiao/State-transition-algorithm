#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import random as rd
from op_axes import *
from op_translate import *
from Benchmark import Sphere
from fitness import *


def axesion(funfcn,Best,fBest,SE,Range,beta,delta):
	Pop_Lb = np.tile(Range[0],(SE,1))
	Pop_Ub = np.tile(Range[1],(SE,1))
	oldBest = Best
	State = op_axes(Best,SE,delta)
	changeRows = State > Pop_Ub
	State[changeRows] = Pop_Ub[changeRows]
	changeRows = State < Pop_Lb
	State[changeRows] = Pop_Lb[changeRows]
	newBest,fGBest = fitness(funfcn,State)
	if fGBest < fBest:
		fBest,Best = fGBest,newBest
		State = op_translate(oldBest,Best,SE,beta)
		changeRows = State > Pop_Ub
		State[changeRows] = Pop_Ub[changeRows]
		changeRows = State < Pop_Lb
		State[changeRows] = Pop_Lb[changeRows]
		newBest,fGBest = fitness(funfcn,State)
		if fGBest < fBest:
			fBest,Best = fGBest,newBest
	return Best,fBest

if __name__ == '__main__':

	funfcn = Sphere
	Best = np.array([2,2])
	fBest = funfcn(Best)
	SE = 4
	n = len(Best)
	Range = np.tile([[-30],[30]],n)
	delta = 1
	beta = 1

	Best,fBest = axesion(funfcn,Best,fBest,SE,Range,beta,delta)
	print(Best,fBest)