'''
Prints a table form of the accuracy (as opposed to the whole matrix).

Don't forget to change GROUP_SIZE
'''

import numpy as np
import csv
import sys
import scipy.stats
from math import *
import matplotlib
import matplotlib.pylab as plt


def calcCI(a):
	return scipy.stats.norm.interval(0.95, loc=np.mean(a), scale=(np.std(a)/np.sqrt(len(a))))[1] - np.mean(a)	# return 1 because 0 is the negative

TIME = '10s'
#TIME = '20s'
#TIME = 'all'

GROUP_SIZE = 50		# CHANGE ME


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

tenData = []

for i in range(0, 30):
	tenData.append(accMatSmall[(i*5)+1:i*5+5,i])


#TIME = '10s'
TIME = '20s'
#TIME = 'all'

GROUP_SIZE = 50		# CHANGE ME


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

tweData = []

for i in range(0, 30):
	tweData.append(accMatSmall[(i*5)+1:i*5+5,i])

#TIME = '10s'
#TIME = '20s'
TIME = 'all'

GROUP_SIZE = 50		# CHANGE ME


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

allData = []

for i in range(0, 30):
	allData.append(accMatSmall[(i*5)+1:i*5+5,i])




tenData = np.array(tenData).flatten()
tweData = np.array(tweData).flatten()
allData = np.array(allData).flatten()



