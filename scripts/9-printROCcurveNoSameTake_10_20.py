'''
Prints the ROC curve (kinda) generated in script 8
'''

import numpy as np
import csv
import sys
from math import *
import matplotlib
import matplotlib.pylab as plt


TIME = '10s'
#TIME = '20s'
#TIME = 'all'

iFile =  csv.reader(open('8-rocNoSameTake-' + TIME + '.csv', 'r'))

data = []
for l in iFile:
	data.append(l)
data = np.array(data)
data = data.astype(np.float)


CIi = []
CIa = []
for l in data:
	#CI.append([l[0] - (1.96 * (l[1]/sqrt(l[5]))),l[0] + (1.96 * (l[1]/sqrt(l[5])))])
	CIi.append(l[0] - (1.96 * (l[1]/sqrt(l[5]))))
	CIa.append(l[0] + (1.96 * (l[1]/sqrt(l[5]))))


pltz = []
axes = plt.subplot2grid((2,1), (0,0))
pltz.append(axes)
pltz[0].axhline(1.2)
pltz[0].axhline(1.0, color='k', ls='--', alpha=0.25)
pltz[0].axhline(0.9, color='k', ls='--', alpha=0.25)
pltz[0].axhline(0.8, color='k', ls='--', alpha=0.25)
pltz[0].axhline(0.7, color='k', ls='--', alpha=0.25)
pltz[0].axhline(0.6, color='k', ls='--', alpha=0.25)
pltz[0].axhline(0.5, color='k', ls='--', alpha=0.25)
pltz[0].axhline(0.4, color='k', ls='--', alpha=0.25)
pltz[0].axhline(0.3, color='k', ls='--', alpha=0.25)
pltz[0].axhline(0.2, color='k', ls='--', alpha=0.25)
pltz[0].axhline(0.1, color='k', ls='--', alpha=0.25)

Xs = range(5,121,5)

#plt.plot(Xs,data[:,1], label='Standard Deviation')
pltz[0].plot(Xs,data[:,4], label='Maximum')
pltz[0].plot(Xs,data[:,2], label='Median')
pltz[0].plot(Xs,data[:,0], label='Mean')
pltz[0].plot(Xs, CIi, 'k', label='95% Confidence Interval')
pltz[0].plot(Xs, CIa, 'k')
pltz[0].fill_between(Xs, CIi, CIa, facecolor='k', alpha = 0.1)
#plt.plot(Xs,data[:,3], label='Minimum')

pltz[0].set_title(TIME, fontsize=12)
pltz[0].legend(loc='lower right', fontsize=10)
#pltz[0].set_xlabel('# Time Points')
pltz[0].set_ylabel('Accuracy')










#TIME = '10s'
TIME = '20s'
#TIME = 'all'

iFile =  csv.reader(open('8-rocNoSameTake-' + TIME + '.csv', 'r'))

data = []
for l in iFile:
	data.append(l)
data = np.array(data)
data = data.astype(np.float)


CIi = []
CIa = []
for l in data:
	#CI.append([l[0] - (1.96 * (l[1]/sqrt(l[5]))),l[0] + (1.96 * (l[1]/sqrt(l[5])))])
	CIi.append(l[0] - (1.96 * (l[1]/sqrt(l[5]))))
	CIa.append(l[0] + (1.96 * (l[1]/sqrt(l[5]))))


axes = plt.subplot2grid((2,1), (1,0))
pltz.append(axes)
pltz[1].axhline(1.2)
pltz[1].axhline(1.0, color='k', ls='--', alpha=0.25)
pltz[1].axhline(0.9, color='k', ls='--', alpha=0.25)
pltz[1].axhline(0.8, color='k', ls='--', alpha=0.25)
pltz[1].axhline(0.7, color='k', ls='--', alpha=0.25)
pltz[1].axhline(0.6, color='k', ls='--', alpha=0.25)
pltz[1].axhline(0.5, color='k', ls='--', alpha=0.25)
pltz[1].axhline(0.4, color='k', ls='--', alpha=0.25)
pltz[1].axhline(0.3, color='k', ls='--', alpha=0.25)
pltz[1].axhline(0.2, color='k', ls='--', alpha=0.25)
pltz[1].axhline(0.1, color='k', ls='--', alpha=0.25)

Xs = range(5,121,5)

#plt.plot(Xs,data[:,1], label='Standard Deviation')
pltz[1].plot(Xs,data[:,4], label='Maximum')
pltz[1].plot(Xs,data[:,2], label='Median')
pltz[1].plot(Xs,data[:,0], label='Mean')
pltz[1].plot(Xs, CIi, 'k', label='95% Confidence Interval')
pltz[1].plot(Xs, CIa, 'k')
pltz[1].fill_between(Xs, CIi, CIa, facecolor='k', alpha = 0.1)
#plt.plot(Xs,data[:,3], label='Minimum')

pltz[1].set_title(TIME, fontsize=12)
pltz[1].legend(loc='lower right', fontsize=10)
pltz[1].set_xlabel('# Time Points')
pltz[1].set_ylabel('Accuracy')

plt.suptitle("Accyracy Curves", fontsize=16)
plt.show()
