'''
Plots the best function on all data from that subject/task

'''

import csv
from math import *
import matplotlib.pylab as plt
import numpy as np

# function for Running, subject 6, take 2:
def func_85_10(v0,v1,v2,v3,v4,v5,v6,v7,v8): return  ( ( ( v5 -sin( v7 )) / ( -10.781012233177547 / ( ( v3 - v0 ) + ( v7 + v5 ) ) ) ) +sin( v7 )) 
def func_85_20(v0,v1,v2,v3,v4,v5,v6,v7,v8): return  (sin( v7 )+ (sin( ( ( v4 +sin( v0 )) -sin(exp(tan( v7 )))) )/ (exp(tan( v7 ))- ( (tan( v7 )+sin(exp(tan( v7 )))) - (exp(exp(tan( v7 )))+ (exp(tan( v7 ))* v0 ) ) ) ) ) ) 

pltz = []
pltz.append(plt.subplot2grid((3,2), (0,0), colspan=2))
plt.title("Subject 6 Running Take 2 --- Model Fit To This Data")
plt.xlabel("Time Point")
plt.ylabel("Signal Intensity")
pltz.append(plt.subplot2grid((3,2), (1,0)))

pltz.append(plt.subplot2grid((3,2), (1, 1)))

pltz.append(plt.subplot2grid((3,2), (2, 0)))

pltz.append(plt.subplot2grid((3,2), (2, 1)))


takes = [1,2,3,4,5]

for i in range(len(takes)):

	iFile = csv.reader(open('../Walking_6_' + str(takes[i]) + '_Z.csv', 'r'))
	data = []
	for l in iFile:
		data.append(l)
	data = np.array(data)
	data = data.astype(np.float)
	signal = data.T[-1]
	expected_10 = []
	expected_20 = []
	err10 = []
	err20 = []
	for r in data:
		try:
			expected_10.append(func_85_10(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8]))
		except OverflowError:
			expected_10.append(float('NaN'))
		err10.append(abs(r[8] - expected_10[-1]))
		try:
			expected_20.append(func_85_20(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8]))
		except OverflowError:
			expected_20.append(float('NaN'))
		err20.append(abs(r[8] - expected_20[-1]))

	print np.nanmean(err10)
	print '\t', np.nanmean(err20)
	if i == 0:
		pltz[i].set_title("Subject 6 Walking Take " + str(takes[i]) + " --- Model Fit To This Data")
	else:
		pltz[i].set_title("Subject 6 Walking Take " + str(takes[i]))
	if i != 1 and i != 2:
		pltz[i].set_xlabel("Time Point")
	pltz[i].set_xlim([0,750])
	pltz[i].set_ylabel("Gyro_z Signal")
	pltz[i].plot(signal, label='Signal')
	#pltz[i].scatter(range(len(signal)),signal)
	pltz[i].plot(expected_10, label='Model-10s')
	pltz[i].plot(expected_20, label='Model-20s')
	pltz[i].legend(fontsize=8)


#plt.tight_layout()
plt.show()
