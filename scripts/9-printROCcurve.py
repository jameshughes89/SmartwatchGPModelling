'''
Prints the ROC curve (kinda) generated in script 8
'''

import numpy as np
import csv
import sys
from math import *
import matplotlib
import matplotlib.pylab as plt


#TIME = '10s'
#TIME = '20s'
TIME = 'all'

iFile =  csv.reader(open('8-roc-' + TIME + '.csv', 'r'))

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

plt.axhline(1.2)
plt.axhline(1.0, color='k', ls='--', alpha=0.25)
plt.axhline(0.9, color='k', ls='--', alpha=0.25)
plt.axhline(0.8, color='k', ls='--', alpha=0.25)
plt.axhline(0.7, color='k', ls='--', alpha=0.25)
plt.axhline(0.6, color='k', ls='--', alpha=0.25)
plt.axhline(0.5, color='k', ls='--', alpha=0.25)
plt.axhline(0.4, color='k', ls='--', alpha=0.25)
plt.axhline(0.3, color='k', ls='--', alpha=0.25)
plt.axhline(0.2, color='k', ls='--', alpha=0.25)
plt.axhline(0.1, color='k', ls='--', alpha=0.25)

Xs = range(5,121,5)

#plt.plot(Xs,data[:,1], label='Standard Deviation')
plt.plot(Xs,data[:,4], label='Maximum')
plt.plot(Xs,data[:,2], label='Median')
plt.plot(Xs,data[:,0], label='Mean')
plt.plot(Xs, CIi, 'k', alpha=0.2, label='95% Confidence Interval')
plt.plot(Xs, CIa, 'k', alpha=0.2)
plt.fill_between(Xs, CIi, CIa, facecolor='k', alpha = 0.1)
plt.plot(Xs,data[:,3], label='Minimum')

plt.title('Accuracy Curves for ' + TIME)
plt.legend()
plt.xlabel('Time Points')
plt.ylabel('Accuracy')
plt.show()
