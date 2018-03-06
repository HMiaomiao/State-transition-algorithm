#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import random as rd
import matplotlib.pyplot as plt
from Benchmark import Sphere,Rastrigin,Rosenbrock,Griewank,Michalewicz

from STA import *
SE = 30
Dim = 5
Range = np.tile([[-30],[30]],Dim)
Iterations = 500
Best0 = np.array(Range[0,:] + (Range[1,:]-Range[0,:]*np.random.uniform(0,1,(1,Dim))))

xmin,fxmin,history = STA(Griewank,Best0,SE,Range,Iterations)
# print("此函数最小值点:",xmin,'\n',"此函数最小值:",fxmin)# python3.5
print "此函数最优解:",xmin,'\n',"此函数最优值:",fxmin# python2.7
plt.plot(history,'b.-')
# plt.semilogy(history,'b.-') # 对数曲线
plt.xlabel('Iterations')
plt.ylabel('fitness')
plt.show()
