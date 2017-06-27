'''
prints the accuracy matrix generated from 5

dont forget to change GROUP_SIZE
'''

import numpy as np
import csv
import sys
from math import *
import matplotlib
import matplotlib.pylab as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable


TIME = '10s'
#TIME = '20s'
#TIME = 'all'

GROUP_SIZE = 50		# CHANGE ME

iFile =  csv.reader(open('5-accMatNoSameTake_G' + str(GROUP_SIZE) + '_' + TIME + '.csv', 'r'))

tasks = ['Down', 'Up', 'Walking', 'Jogging', 'Running']
tasks2 = ['D', 'U', 'W', 'J', 'R']

accMat = []
for l in iFile:
	accMat.append(l)
accMat = np.array(accMat)
accMat = accMat.astype(np.float)

for i in range(150):
	for j in range(150):
		#if not(j - (i -  i%5)  >= 5 or i - (j -  j%5)  >= 5):
		if i == j:
			accMat[i][j] = float('nan')


pltz = []

axes = plt.subplot2grid((2,2), (0,0))
pltz.append(axes)

img = pltz[0].matshow(accMat)

#plt.clim(0,1)

pltz[0].set_yticks(range(15,150,30))
pltz[0].set_yticklabels(tasks, rotation=90)
pltz[0].set_xticks(range(15,150,30))
pltz[0].set_xticklabels(tasks, rotation=0)

#plt.xticks(range(150), ['D 1 1', 'D 1 2', 'D 1 3', 'D 1 4', 'D 1 5', 'D 2 1', 'D 2 2', 'D 2 3', 'D 2 4', 'D 2 5', 'D 3 1', 'D 3 2', 'D 3 3', 'D 3 4', 'D 3 5', 'D 4 1', 'D 4 2', 'D 4 3', 'D 4 4', 'D 4 5', 'D 5 1', 'D 5 2', 'D 5 3', 'D 5 4', 'D 5 5', 'D 6 1', 'D 6 2', 'D 6 3', 'D 6 4', 'D 6 5', 'J 1 1', 'J 1 2', 'J 1 3', 'J 1 4', 'J 1 5', 'J 2 1', 'J 2 2', 'J 2 3', 'J 2 4', 'J 2 5', 'J 3 1', 'J 3 2', 'J 3 3', 'J 3 4', 'J 3 5', 'J 4 1', 'J 4 2', 'J 4 3', 'J 4 4', 'J 4 5', 'J 5 1', 'J 5 2', 'J 5 3', 'J 5 4', 'J 5 5', 'J 6 1', 'J 6 2', 'J 6 3', 'J 6 4', 'J 6 5', 'R 1 1', 'R 1 2', 'R 1 3', 'R 1 4', 'R 1 5', 'R 2 1', 'R 2 2', 'R 2 3', 'R 2 4', 'R 2 5', 'R 3 1', 'R 3 2', 'R 3 3', 'R 3 4', 'R 3 5', 'R 4 1', 'R 4 2', 'R 4 3', 'R 4 4', 'R 4 5', 'R 5 1', 'R 5 2', 'R 5 3', 'R 5 4', 'R 5 5', 'R 6 1', 'R 6 2', 'R 6 3', 'R 6 4', 'R 6 5', 'U 1 1', 'U 1 2', 'U 1 3', 'U 1 4', 'U 1 5', 'U 2 1', 'U 2 2', 'U 2 3', 'U 2 4', 'U 2 5', 'U 3 1', 'U 3 2', 'U 3 3', 'U 3 4', 'U 3 5', 'U 4 1', 'U 4 2', 'U 4 3', 'U 4 4', 'U 4 5', 'U 5 1', 'U 5 2', 'U 5 3', 'U 5 4', 'U 5 5', 'U 6 1', 'U 6 2', 'U 6 3', 'U 6 4', 'U 6 5', 'W 1 1', 'W 1 2', 'W 1 3', 'W 1 4', 'W 1 5', 'W 2 1', 'W 2 2', 'W 2 3', 'W 2 4', 'W 2 5', 'W 3 1', 'W 3 2', 'W 3 3', 'W 3 4', 'W 3 5', 'W 4 1', 'W 4 2', 'W 4 3', 'W 4 4', 'W 4 5', 'W 5 1', 'W 5 2', 'W 5 3', 'W 5 4', 'W 5 5', 'W 6 1', 'W 6 2', 'W 6 3', 'W 6 4', 'W 6 5'], rotation =90)
#plt.yticks(range(150), ['D 1 1', 'D 1 2', 'D 1 3', 'D 1 4', 'D 1 5', 'D 2 1', 'D 2 2', 'D 2 3', 'D 2 4', 'D 2 5', 'D 3 1', 'D 3 2', 'D 3 3', 'D 3 4', 'D 3 5', 'D 4 1', 'D 4 2', 'D 4 3', 'D 4 4', 'D 4 5', 'D 5 1', 'D 5 2', 'D 5 3', 'D 5 4', 'D 5 5', 'D 6 1', 'D 6 2', 'D 6 3', 'D 6 4', 'D 6 5', 'J 1 1', 'J 1 2', 'J 1 3', 'J 1 4', 'J 1 5', 'J 2 1', 'J 2 2', 'J 2 3', 'J 2 4', 'J 2 5', 'J 3 1', 'J 3 2', 'J 3 3', 'J 3 4', 'J 3 5', 'J 4 1', 'J 4 2', 'J 4 3', 'J 4 4', 'J 4 5', 'J 5 1', 'J 5 2', 'J 5 3', 'J 5 4', 'J 5 5', 'J 6 1', 'J 6 2', 'J 6 3', 'J 6 4', 'J 6 5', 'R 1 1', 'R 1 2', 'R 1 3', 'R 1 4', 'R 1 5', 'R 2 1', 'R 2 2', 'R 2 3', 'R 2 4', 'R 2 5', 'R 3 1', 'R 3 2', 'R 3 3', 'R 3 4', 'R 3 5', 'R 4 1', 'R 4 2', 'R 4 3', 'R 4 4', 'R 4 5', 'R 5 1', 'R 5 2', 'R 5 3', 'R 5 4', 'R 5 5', 'R 6 1', 'R 6 2', 'R 6 3', 'R 6 4', 'R 6 5', 'U 1 1', 'U 1 2', 'U 1 3', 'U 1 4', 'U 1 5', 'U 2 1', 'U 2 2', 'U 2 3', 'U 2 4', 'U 2 5', 'U 3 1', 'U 3 2', 'U 3 3', 'U 3 4', 'U 3 5', 'U 4 1', 'U 4 2', 'U 4 3', 'U 4 4', 'U 4 5', 'U 5 1', 'U 5 2', 'U 5 3', 'U 5 4', 'U 5 5', 'U 6 1', 'U 6 2', 'U 6 3', 'U 6 4', 'U 6 5', 'W 1 1', 'W 1 2', 'W 1 3', 'W 1 4', 'W 1 5', 'W 2 1', 'W 2 2', 'W 2 3', 'W 2 4', 'W 2 5', 'W 3 1', 'W 3 2', 'W 3 3', 'W 3 4', 'W 3 5', 'W 4 1', 'W 4 2', 'W 4 3', 'W 4 4', 'W 4 5', 'W 5 1', 'W 5 2', 'W 5 3', 'W 5 4', 'W 5 5', 'W 6 1', 'W 6 2', 'W 6 3', 'W 6 4', 'W 6 5'])

for i in range(29, 150,30):
	pltz[0].axvline(i+0.5, color='k', linewidth=2)	
	pltz[0].axhline(i+0.5, color='k', linewidth=2)

for i in range(4,150,5):
	pltz[0].axvline(i+0.5, color='k', linewidth=1, linestyle='--')
	pltz[0].axhline(i+0.5, color='k', linewidth=1, linestyle='--')


#pltz[0].set_title('Accuracy Matrix: Each Dataset Applied to All Models Except Self --- ' + TIME + ' (Batch of ' + str(GROUP_SIZE) + ')')
pltz[0].set_title('Each Model Applied To All Data (Except Self) (10s)', fontsize=12)
pltz[0].set_ylabel('Data',rotation=90)
#pltz[0].set_xlabel('Model')

divider = make_axes_locatable(axes)
cax = divider.append_axes("right", size="5%", pad=0.05)
plt.colorbar(img, cax = cax)
#plt.clim(0,1)
#plt.show()


'''
'D 1 1', 'D 1 2', 'D 1 3', 'D 1 4', 'D 1 5', 'D 2 1', 'D 2 2', 'D 2 3', 'D 2 4', 'D 2 5', 'D 3 1', 'D 3 2', 'D 3 3', 'D 3 4', 'D 3 5', 'D 4 1', 'D 4 2', 'D 4 3', 'D 4 4', 'D 4 5', 'D 5 1', 'D 5 2', 'D 5 3', 'D 5 4', 'D 5 5', 'D 6 1', 'D 6 2', 'D 6 3', 'D 6 4', 'D 6 5', 'J 1 1', 'J 1 2', 'J 1 3', 'J 1 4', 'J 1 5', 'J 2 1', 'J 2 2', 'J 2 3', 'J 2 4', 'J 2 5', 'J 3 1', 'J 3 2', 'J 3 3', 'J 3 4', 'J 3 5', 'J 4 1', 'J 4 2', 'J 4 3', 'J 4 4', 'J 4 5', 'J 5 1', 'J 5 2', 'J 5 3', 'J 5 4', 'J 5 5', 'J 6 1', 'J 6 2', 'J 6 3', 'J 6 4', 'J 6 5', 'R 1 1', 'R 1 2', 'R 1 3', 'R 1 4', 'R 1 5', 'R 2 1', 'R 2 2', 'R 2 3', 'R 2 4', 'R 2 5', 'R 3 1', 'R 3 2', 'R 3 3', 'R 3 4', 'R 3 5', 'R 4 1', 'R 4 2', 'R 4 3', 'R 4 4', 'R 4 5', 'R 5 1', 'R 5 2', 'R 5 3', 'R 5 4', 'R 5 5', 'R 6 1', 'R 6 2', 'R 6 3', 'R 6 4', 'R 6 5', 'U 1 1', 'U 1 2', 'U 1 3', 'U 1 4', 'U 1 5', 'U 2 1', 'U 2 2', 'U 2 3', 'U 2 4', 'U 2 5', 'U 3 1', 'U 3 2', 'U 3 3', 'U 3 4', 'U 3 5', 'U 4 1', 'U 4 2', 'U 4 3', 'U 4 4', 'U 4 5', 'U 5 1', 'U 5 2', 'U 5 3', 'U 5 4', 'U 5 5', 'U 6 1', 'U 6 2', 'U 6 3', 'U 6 4', 'U 6 5', 'W 1 1', 'W 1 2', 'W 1 3', 'W 1 4', 'W 1 5', 'W 2 1', 'W 2 2', 'W 2 3', 'W 2 4', 'W 2 5', 'W 3 1', 'W 3 2', 'W 3 3', 'W 3 4', 'W 3 5', 'W 4 1', 'W 4 2', 'W 4 3', 'W 4 4', 'W 4 5', 'W 5 1', 'W 5 2', 'W 5 3', 'W 5 4', 'W 5 5', 'W 6 1', 'W 6 2', 'W 6 3', 'W 6 4', 'W 6 5'
'''



accMatSmall = []
for i in range(0, accMat.shape[0], 1):
	accMatRow = []
	for j in range(0, accMat.shape[1], 5):
		accMatRow.append(np.nansum(accMat[i,j:j+5]))
	accMatSmall.append(accMatRow)


axes = plt.subplot2grid((2,2), (0,1))
pltz.append(axes)

img = pltz[1].matshow(accMatSmall, aspect='auto')
#plt.matshow(accMatSmall, aspect='auto')


pltz[1].set_yticks(range(15, 150,30))
pltz[1].set_yticklabels(tasks, rotation=90)
pltz[1].set_xticks(range(2,30,6))
pltz[1].set_xticklabels(tasks, rotation=0)

for i in range(29, 150,30):
	pltz[1].axhline(i+0.5, color='k', linewidth=2)

for i in range(5,30,6):
	pltz[1].axvline(i+0.5, color='k', linewidth=2)

for i in range(4,150,5):
	pltz[1].axhline(i+0.5, color='k', linewidth=1, linestyle='--')

#pltz[1].set_title('Accuracy Matrix: Each Dataset Applied to All Models Except Self --- ' + TIME + ' (Batch of ' + str(GROUP_SIZE) + ')')
pltz[1].set_title('Combined Takes (10s)', fontsize=12)
pltz[1].set_ylabel('Data',rotation=90)
#pltz[1].set_xlabel('Model')

divider = make_axes_locatable(axes)
cax = divider.append_axes("right", size="5%", pad=0.05)
plt.colorbar(img, cax = cax)
#plt.clim(0,1)
#plt.tight_layout()
plt.suptitle('Confusion Matrix',fontsize=16)
#plt.show()













#TIME = '10s'
TIME = '20s'
#TIME = 'all'

GROUP_SIZE = 50		# CHANGE ME

iFile =  csv.reader(open('5-accMatNoSameTake_G' + str(GROUP_SIZE) + '_' + TIME + '.csv', 'r'))

tasks = ['Down', 'Up', 'Walking', 'Jogging', 'Running']
tasks2 = ['D', 'U', 'W', 'J', 'R']

accMat = []
for l in iFile:
	accMat.append(l)
accMat = np.array(accMat)
accMat = accMat.astype(np.float)

for i in range(150):
	for j in range(150):
		#if not(j - (i -  i%5)  >= 5 or i - (j -  j%5)  >= 5):
		if i == j:
			accMat[i][j] = float('nan')


axes = plt.subplot2grid((2,2), (1,0))
pltz.append(axes)

img = pltz[2].matshow(accMat)

#plt.clim(0,1)

pltz[2].set_yticks(range(15,150,30))
pltz[2].set_yticklabels(tasks, rotation=90)
pltz[2].set_xticks(range(15,150,30))
pltz[2].set_xticklabels(tasks, rotation=0)

#plt.xticks(range(150), ['D 1 1', 'D 1 2', 'D 1 3', 'D 1 4', 'D 1 5', 'D 2 1', 'D 2 2', 'D 2 3', 'D 2 4', 'D 2 5', 'D 3 1', 'D 3 2', 'D 3 3', 'D 3 4', 'D 3 5', 'D 4 1', 'D 4 2', 'D 4 3', 'D 4 4', 'D 4 5', 'D 5 1', 'D 5 2', 'D 5 3', 'D 5 4', 'D 5 5', 'D 6 1', 'D 6 2', 'D 6 3', 'D 6 4', 'D 6 5', 'J 1 1', 'J 1 2', 'J 1 3', 'J 1 4', 'J 1 5', 'J 2 1', 'J 2 2', 'J 2 3', 'J 2 4', 'J 2 5', 'J 3 1', 'J 3 2', 'J 3 3', 'J 3 4', 'J 3 5', 'J 4 1', 'J 4 2', 'J 4 3', 'J 4 4', 'J 4 5', 'J 5 1', 'J 5 2', 'J 5 3', 'J 5 4', 'J 5 5', 'J 6 1', 'J 6 2', 'J 6 3', 'J 6 4', 'J 6 5', 'R 1 1', 'R 1 2', 'R 1 3', 'R 1 4', 'R 1 5', 'R 2 1', 'R 2 2', 'R 2 3', 'R 2 4', 'R 2 5', 'R 3 1', 'R 3 2', 'R 3 3', 'R 3 4', 'R 3 5', 'R 4 1', 'R 4 2', 'R 4 3', 'R 4 4', 'R 4 5', 'R 5 1', 'R 5 2', 'R 5 3', 'R 5 4', 'R 5 5', 'R 6 1', 'R 6 2', 'R 6 3', 'R 6 4', 'R 6 5', 'U 1 1', 'U 1 2', 'U 1 3', 'U 1 4', 'U 1 5', 'U 2 1', 'U 2 2', 'U 2 3', 'U 2 4', 'U 2 5', 'U 3 1', 'U 3 2', 'U 3 3', 'U 3 4', 'U 3 5', 'U 4 1', 'U 4 2', 'U 4 3', 'U 4 4', 'U 4 5', 'U 5 1', 'U 5 2', 'U 5 3', 'U 5 4', 'U 5 5', 'U 6 1', 'U 6 2', 'U 6 3', 'U 6 4', 'U 6 5', 'W 1 1', 'W 1 2', 'W 1 3', 'W 1 4', 'W 1 5', 'W 2 1', 'W 2 2', 'W 2 3', 'W 2 4', 'W 2 5', 'W 3 1', 'W 3 2', 'W 3 3', 'W 3 4', 'W 3 5', 'W 4 1', 'W 4 2', 'W 4 3', 'W 4 4', 'W 4 5', 'W 5 1', 'W 5 2', 'W 5 3', 'W 5 4', 'W 5 5', 'W 6 1', 'W 6 2', 'W 6 3', 'W 6 4', 'W 6 5'], rotation =90)
#plt.yticks(range(150), ['D 1 1', 'D 1 2', 'D 1 3', 'D 1 4', 'D 1 5', 'D 2 1', 'D 2 2', 'D 2 3', 'D 2 4', 'D 2 5', 'D 3 1', 'D 3 2', 'D 3 3', 'D 3 4', 'D 3 5', 'D 4 1', 'D 4 2', 'D 4 3', 'D 4 4', 'D 4 5', 'D 5 1', 'D 5 2', 'D 5 3', 'D 5 4', 'D 5 5', 'D 6 1', 'D 6 2', 'D 6 3', 'D 6 4', 'D 6 5', 'J 1 1', 'J 1 2', 'J 1 3', 'J 1 4', 'J 1 5', 'J 2 1', 'J 2 2', 'J 2 3', 'J 2 4', 'J 2 5', 'J 3 1', 'J 3 2', 'J 3 3', 'J 3 4', 'J 3 5', 'J 4 1', 'J 4 2', 'J 4 3', 'J 4 4', 'J 4 5', 'J 5 1', 'J 5 2', 'J 5 3', 'J 5 4', 'J 5 5', 'J 6 1', 'J 6 2', 'J 6 3', 'J 6 4', 'J 6 5', 'R 1 1', 'R 1 2', 'R 1 3', 'R 1 4', 'R 1 5', 'R 2 1', 'R 2 2', 'R 2 3', 'R 2 4', 'R 2 5', 'R 3 1', 'R 3 2', 'R 3 3', 'R 3 4', 'R 3 5', 'R 4 1', 'R 4 2', 'R 4 3', 'R 4 4', 'R 4 5', 'R 5 1', 'R 5 2', 'R 5 3', 'R 5 4', 'R 5 5', 'R 6 1', 'R 6 2', 'R 6 3', 'R 6 4', 'R 6 5', 'U 1 1', 'U 1 2', 'U 1 3', 'U 1 4', 'U 1 5', 'U 2 1', 'U 2 2', 'U 2 3', 'U 2 4', 'U 2 5', 'U 3 1', 'U 3 2', 'U 3 3', 'U 3 4', 'U 3 5', 'U 4 1', 'U 4 2', 'U 4 3', 'U 4 4', 'U 4 5', 'U 5 1', 'U 5 2', 'U 5 3', 'U 5 4', 'U 5 5', 'U 6 1', 'U 6 2', 'U 6 3', 'U 6 4', 'U 6 5', 'W 1 1', 'W 1 2', 'W 1 3', 'W 1 4', 'W 1 5', 'W 2 1', 'W 2 2', 'W 2 3', 'W 2 4', 'W 2 5', 'W 3 1', 'W 3 2', 'W 3 3', 'W 3 4', 'W 3 5', 'W 4 1', 'W 4 2', 'W 4 3', 'W 4 4', 'W 4 5', 'W 5 1', 'W 5 2', 'W 5 3', 'W 5 4', 'W 5 5', 'W 6 1', 'W 6 2', 'W 6 3', 'W 6 4', 'W 6 5'])

for i in range(29, 150,30):
	pltz[2].axvline(i+0.5, color='k', linewidth=2)	
	pltz[2].axhline(i+0.5, color='k', linewidth=2)

for i in range(4,150,5):
	pltz[2].axvline(i+0.5, color='k', linewidth=1, linestyle='--')
	pltz[2].axhline(i+0.5, color='k', linewidth=1, linestyle='--')


#pltz[2].set_title('Accuracy Matrix: Each Dataset Applied to All Models Except Self --- ' + TIME + ' (Batch of ' + str(GROUP_SIZE) + ')')
pltz[2].set_title('Each Model Applied To All Data (Except Self) (20s)', fontsize=12)
pltz[2].set_ylabel('Data',rotation=90)
pltz[2].set_xlabel('Model')

divider = make_axes_locatable(axes)
cax = divider.append_axes("right", size="5%", pad=0.05)
plt.colorbar(img, cax = cax)
#plt.clim(0,1)
#plt.show()


'''
'D 1 1', 'D 1 2', 'D 1 3', 'D 1 4', 'D 1 5', 'D 2 1', 'D 2 2', 'D 2 3', 'D 2 4', 'D 2 5', 'D 3 1', 'D 3 2', 'D 3 3', 'D 3 4', 'D 3 5', 'D 4 1', 'D 4 2', 'D 4 3', 'D 4 4', 'D 4 5', 'D 5 1', 'D 5 2', 'D 5 3', 'D 5 4', 'D 5 5', 'D 6 1', 'D 6 2', 'D 6 3', 'D 6 4', 'D 6 5', 'J 1 1', 'J 1 2', 'J 1 3', 'J 1 4', 'J 1 5', 'J 2 1', 'J 2 2', 'J 2 3', 'J 2 4', 'J 2 5', 'J 3 1', 'J 3 2', 'J 3 3', 'J 3 4', 'J 3 5', 'J 4 1', 'J 4 2', 'J 4 3', 'J 4 4', 'J 4 5', 'J 5 1', 'J 5 2', 'J 5 3', 'J 5 4', 'J 5 5', 'J 6 1', 'J 6 2', 'J 6 3', 'J 6 4', 'J 6 5', 'R 1 1', 'R 1 2', 'R 1 3', 'R 1 4', 'R 1 5', 'R 2 1', 'R 2 2', 'R 2 3', 'R 2 4', 'R 2 5', 'R 3 1', 'R 3 2', 'R 3 3', 'R 3 4', 'R 3 5', 'R 4 1', 'R 4 2', 'R 4 3', 'R 4 4', 'R 4 5', 'R 5 1', 'R 5 2', 'R 5 3', 'R 5 4', 'R 5 5', 'R 6 1', 'R 6 2', 'R 6 3', 'R 6 4', 'R 6 5', 'U 1 1', 'U 1 2', 'U 1 3', 'U 1 4', 'U 1 5', 'U 2 1', 'U 2 2', 'U 2 3', 'U 2 4', 'U 2 5', 'U 3 1', 'U 3 2', 'U 3 3', 'U 3 4', 'U 3 5', 'U 4 1', 'U 4 2', 'U 4 3', 'U 4 4', 'U 4 5', 'U 5 1', 'U 5 2', 'U 5 3', 'U 5 4', 'U 5 5', 'U 6 1', 'U 6 2', 'U 6 3', 'U 6 4', 'U 6 5', 'W 1 1', 'W 1 2', 'W 1 3', 'W 1 4', 'W 1 5', 'W 2 1', 'W 2 2', 'W 2 3', 'W 2 4', 'W 2 5', 'W 3 1', 'W 3 2', 'W 3 3', 'W 3 4', 'W 3 5', 'W 4 1', 'W 4 2', 'W 4 3', 'W 4 4', 'W 4 5', 'W 5 1', 'W 5 2', 'W 5 3', 'W 5 4', 'W 5 5', 'W 6 1', 'W 6 2', 'W 6 3', 'W 6 4', 'W 6 5'
'''



accMatSmall = []
for i in range(0, accMat.shape[0], 1):
	accMatRow = []
	for j in range(0, accMat.shape[1], 5):
		accMatRow.append(np.nansum(accMat[i,j:j+5]))
	accMatSmall.append(accMatRow)


axes = plt.subplot2grid((2,2), (1,1))
pltz.append(axes)

img = pltz[3].matshow(accMatSmall, aspect='auto')
#plt.matshow(accMatSmall, aspect='auto')


pltz[3].set_yticks(range(15, 150,30))
pltz[3].set_yticklabels(tasks, rotation=90)
pltz[3].set_xticks(range(2,30,6))
pltz[3].set_xticklabels(tasks, rotation=0)

for i in range(29, 150,30):
	pltz[3].axhline(i+0.5, color='k', linewidth=2)

for i in range(5,30,6):
	pltz[3].axvline(i+0.5, color='k', linewidth=2)

for i in range(4,150,5):
	pltz[3].axhline(i+0.5, color='k', linewidth=1, linestyle='--')

#pltz[3].set_title('Accuracy Matrix: Each Dataset Applied to All Models Except Self --- ' + TIME + ' (Batch of ' + str(GROUP_SIZE) + ')')
pltz[3].set_title('Combined Takes (20s)', fontsize=12)
pltz[3].set_ylabel('Data',rotation=90)
pltz[3].set_xlabel('Model')

divider = make_axes_locatable(axes)
cax = divider.append_axes("right", size="5%", pad=0.05)
plt.colorbar(img, cax = cax)
#plt.clim(0,1)
#plt.tight_layout()
plt.suptitle('Confusion Matrix',fontsize=16)
plt.show()


'''
['D 1', 'D 2', 'D 3', 'D 4', 'D 5', 'D 6', 'J 1', 'J 2', 'J 3', 'J 4', 'J 5', 'J 6', 'R 1', 'R 2', 'R 3', 'R 4', 'R 5', 'R 6', 'U 1', 'U 2', 'U 3', 'U 4', 'U 5', 'U 6', 'W 1', 'W 2', 'W 3', 'W 4', 'W 5', 'W 6']
'''


