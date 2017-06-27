import csv
from math import *
import matplotlib.pylab as plt
import numpy as np


def function(v0, v1, v2, v3, v4, v5, v6, v7, v8): return sin( ( v7 - ( (cos( ( v0 - v4 ) )- v0 ) / 4.183120259437608 ) ) )

data = []

iFile = csv.reader(open('../Walking_6_1_Z.csv','r'))

for l in iFile:
	data.append(l)

data = np.array(data).astype(np.float)

Ys = []
ABE = []

for i in range(len(data)):
	y = function(data[i,0], data[i,1], data[i,2], data[i,3], data[i,4], data[i,5], data[i,6], data[i,7], data[i,8]) 
	Ys.append(y)
	ABE.append(abs(data[i,8] - y))


print np.mean(ABE)
plt.plot(Ys)
plt.plot(data[:,8])
plt.show()

