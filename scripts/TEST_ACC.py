'''
Prints a table form of the accuracy (as opposed to the whole matrix).

Don't forget to change GROUP_SIZE
'''

import numpy as np
import csv
import sys
from math import *
import matplotlib
import matplotlib.pylab as plt

#TIME = '10s'
TIME = '20s'
#TIME = 'all'

GROUP_SIZE = 50		# CHANGE ME

ROCstuff = []

#tasks = ['Down', 'Jogging', 'Running', 'Up', 'Walking']
tasks = ['Down', 'Up', 'Walking', 'Jogging', 'Running']
iFile =  csv.reader(open('5-accMatNoSameTake_G' + str(GROUP_SIZE) + '_' + TIME + '.csv', 'r'))

accMat = []
for l in iFile:
	accMat.append(l)
accMat = np.array(accMat)
accMat = accMat.astype(np.float)



accMatSmall = []
for i in range(0, accMat.shape[0], 1):
	accMatRow = []
	for j in range(0, accMat.shape[1], 5):
		accMatRow.append(np.sum(accMat[i,j:j+5]))
	accMatSmall.append(accMatRow)


accMatSmall = np.array(accMatSmall)
print accMatSmall.shape

accMatSmall = np.array(accMatSmall)
a = []
for i in range(30):
	for j in range(5):
	    a.append(accMatSmall[i*5+j,i])


ROCstuff.append([np.mean(a), np.std(a), np.median(a), np.min(a), np.max(a)])

print ROCstuff
