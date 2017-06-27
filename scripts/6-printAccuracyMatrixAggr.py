#finds the top models for each subject

import numpy as np
import csv
import sys
from math import *
import matplotlib
import matplotlib.pylab as plt

iFile =  csv.reader(open('accMat_aggr.csv', 'r'))

accMat = []
for l in iFile:
	accMat.append(l)
accMat = np.array(accMat)
accMat = accMat.astype(np.float)



font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 6}

matplotlib.rc('font', **font)


plt.matshow(accMat, aspect='auto')
plt.colorbar()
plt.clim(0,1)

plt.yticks(range(150), ['D 1 1', 'D 1 2', 'D 1 3', 'D 1 4', 'D 1 5', 'D 2 1', 'D 2 2', 'D 2 3', 'D 2 4', 'D 2 5', 'D 3 1', 'D 3 2', 'D 3 3', 'D 3 4', 'D 3 5', 'D 4 1', 'D 4 2', 'D 4 3', 'D 4 4', 'D 4 5', 'D 5 1', 'D 5 2', 'D 5 3', 'D 5 4', 'D 5 5', 'D 6 1', 'D 6 2', 'D 6 3', 'D 6 4', 'D 6 5', 'J 1 1', 'J 1 2', 'J 1 3', 'J 1 4', 'J 1 5', 'J 2 1', 'J 2 2', 'J 2 3', 'J 2 4', 'J 2 5', 'J 3 1', 'J 3 2', 'J 3 3', 'J 3 4', 'J 3 5', 'J 4 1', 'J 4 2', 'J 4 3', 'J 4 4', 'J 4 5', 'J 5 1', 'J 5 2', 'J 5 3', 'J 5 4', 'J 5 5', 'J 6 1', 'J 6 2', 'J 6 3', 'J 6 4', 'J 6 5', 'R 1 1', 'R 1 2', 'R 1 3', 'R 1 4', 'R 1 5', 'R 2 1', 'R 2 2', 'R 2 3', 'R 2 4', 'R 2 5', 'R 3 1', 'R 3 2', 'R 3 3', 'R 3 4', 'R 3 5', 'R 4 1', 'R 4 2', 'R 4 3', 'R 4 4', 'R 4 5', 'R 5 1', 'R 5 2', 'R 5 3', 'R 5 4', 'R 5 5', 'R 6 1', 'R 6 2', 'R 6 3', 'R 6 4', 'R 6 5', 'U 1 1', 'U 1 2', 'U 1 3', 'U 1 4', 'U 1 5', 'U 2 1', 'U 2 2', 'U 2 3', 'U 2 4', 'U 2 5', 'U 3 1', 'U 3 2', 'U 3 3', 'U 3 4', 'U 3 5', 'U 4 1', 'U 4 2', 'U 4 3', 'U 4 4', 'U 4 5', 'U 5 1', 'U 5 2', 'U 5 3', 'U 5 4', 'U 5 5', 'U 6 1', 'U 6 2', 'U 6 3', 'U 6 4', 'U 6 5', 'W 1 1', 'W 1 2', 'W 1 3', 'W 1 4', 'W 1 5', 'W 2 1', 'W 2 2', 'W 2 3', 'W 2 4', 'W 2 5', 'W 3 1', 'W 3 2', 'W 3 3', 'W 3 4', 'W 3 5', 'W 4 1', 'W 4 2', 'W 4 3', 'W 4 4', 'W 4 5', 'W 5 1', 'W 5 2', 'W 5 3', 'W 5 4', 'W 5 5', 'W 6 1', 'W 6 2', 'W 6 3', 'W 6 4', 'W 6 5'])



plt.axhline(29.5, color='k', linewidth=2)
plt.axhline(59.5, color='k', linewidth=2)
plt.axhline(89.5, color='k', linewidth=2)
plt.axhline(119.5, color='k', linewidth=2)




plt.axhline(4.5, color='k', linewidth=1, linestyle='--')
plt.axhline(9.5, color='k', linewidth=1, linestyle='--')
plt.axhline(14.5, color='k', linewidth=1, linestyle='--')
plt.axhline(19.5, color='k', linewidth=1, linestyle='--')
plt.axhline(24.5, color='k', linewidth=1, linestyle='--')
plt.axhline(29.5, color='k', linewidth=1, linestyle='--')
plt.axhline(34.5, color='k', linewidth=1, linestyle='--')
plt.axhline(39.5, color='k', linewidth=1, linestyle='--')
plt.axhline(44.5, color='k', linewidth=1, linestyle='--')
plt.axhline(49.5, color='k', linewidth=1, linestyle='--')
plt.axhline(54.5, color='k', linewidth=1, linestyle='--')
plt.axhline(59.5, color='k', linewidth=1, linestyle='--')
plt.axhline(64.5, color='k', linewidth=1, linestyle='--')
plt.axhline(69.5, color='k', linewidth=1, linestyle='--')
plt.axhline(74.5, color='k', linewidth=1, linestyle='--')
plt.axhline(79.5, color='k', linewidth=1, linestyle='--')
plt.axhline(84.5, color='k', linewidth=1, linestyle='--')
plt.axhline(89.5, color='k', linewidth=1, linestyle='--')
plt.axhline(94.5, color='k', linewidth=1, linestyle='--')
plt.axhline(99.5, color='k', linewidth=1, linestyle='--')
plt.axhline(104.5, color='k', linewidth=1, linestyle='--')
plt.axhline(109.5, color='k', linewidth=1, linestyle='--')
plt.axhline(114.5, color='k', linewidth=1, linestyle='--')
plt.axhline(119.5, color='k', linewidth=1, linestyle='--')
plt.axhline(124.5, color='k', linewidth=1, linestyle='--')
plt.axhline(129.5, color='k', linewidth=1, linestyle='--')
plt.axhline(134.5, color='k', linewidth=1, linestyle='--')
plt.axhline(139.5, color='k', linewidth=1, linestyle='--')
plt.axhline(144.5, color='k', linewidth=1, linestyle='--')
plt.axhline(149.5, color='k', linewidth=1, linestyle='--')

plt.title('Accuracy Matrix: Each Dataset Applied to All Models (Batch of 100)')
plt.ylabel('Data',rotation=90)
plt.xlabel('Model')
plt.show()


'''
'D 1 1', 'D 1 2', 'D 1 3', 'D 1 4', 'D 1 5', 'D 2 1', 'D 2 2', 'D 2 3', 'D 2 4', 'D 2 5', 'D 3 1', 'D 3 2', 'D 3 3', 'D 3 4', 'D 3 5', 'D 4 1', 'D 4 2', 'D 4 3', 'D 4 4', 'D 4 5', 'D 5 1', 'D 5 2', 'D 5 3', 'D 5 4', 'D 5 5', 'D 6 1', 'D 6 2', 'D 6 3', 'D 6 4', 'D 6 5', 'J 1 1', 'J 1 2', 'J 1 3', 'J 1 4', 'J 1 5', 'J 2 1', 'J 2 2', 'J 2 3', 'J 2 4', 'J 2 5', 'J 3 1', 'J 3 2', 'J 3 3', 'J 3 4', 'J 3 5', 'J 4 1', 'J 4 2', 'J 4 3', 'J 4 4', 'J 4 5', 'J 5 1', 'J 5 2', 'J 5 3', 'J 5 4', 'J 5 5', 'J 6 1', 'J 6 2', 'J 6 3', 'J 6 4', 'J 6 5', 'R 1 1', 'R 1 2', 'R 1 3', 'R 1 4', 'R 1 5', 'R 2 1', 'R 2 2', 'R 2 3', 'R 2 4', 'R 2 5', 'R 3 1', 'R 3 2', 'R 3 3', 'R 3 4', 'R 3 5', 'R 4 1', 'R 4 2', 'R 4 3', 'R 4 4', 'R 4 5', 'R 5 1', 'R 5 2', 'R 5 3', 'R 5 4', 'R 5 5', 'R 6 1', 'R 6 2', 'R 6 3', 'R 6 4', 'R 6 5', 'U 1 1', 'U 1 2', 'U 1 3', 'U 1 4', 'U 1 5', 'U 2 1', 'U 2 2', 'U 2 3', 'U 2 4', 'U 2 5', 'U 3 1', 'U 3 2', 'U 3 3', 'U 3 4', 'U 3 5', 'U 4 1', 'U 4 2', 'U 4 3', 'U 4 4', 'U 4 5', 'U 5 1', 'U 5 2', 'U 5 3', 'U 5 4', 'U 5 5', 'U 6 1', 'U 6 2', 'U 6 3', 'U 6 4', 'U 6 5', 'W 1 1', 'W 1 2', 'W 1 3', 'W 1 4', 'W 1 5', 'W 2 1', 'W 2 2', 'W 2 3', 'W 2 4', 'W 2 5', 'W 3 1', 'W 3 2', 'W 3 3', 'W 3 4', 'W 3 5', 'W 4 1', 'W 4 2', 'W 4 3', 'W 4 4', 'W 4 5', 'W 5 1', 'W 5 2', 'W 5 3', 'W 5 4', 'W 5 5', 'W 6 1', 'W 6 2', 'W 6 3', 'W 6 4', 'W 6 5'
'''



accMatSmall = []
for i in range(0, accMat.shape[0], 1):
	accMatRow = []
	for j in range(0, accMat.shape[1], 5):
		accMatRow.append(np.sum(accMat[i,j:j+5]))
	accMatSmall.append(accMatRow)

plt.matshow(accMatSmall, aspect='auto')
plt.colorbar()
plt.clim(0,1)
plt.xticks(range(30), ['D 1', 'D 2', 'D 3', 'D 4', 'D 5', 'D 6', 'J 1', 'J 2', 'J 3', 'J 4', 'J 5', 'J 6', 'R 1', 'R 2', 'R 3', 'R 4', 'R 5', 'R 6', 'U 1', 'U 2', 'U 3', 'U 4', 'U 5', 'U 6', 'W 1', 'W 2', 'W 3', 'W 4', 'W 5', 'W 6'], rotation =90)
plt.yticks(range(150), ['D 1 1', 'D 1 2', 'D 1 3', 'D 1 4', 'D 1 5', 'D 2 1', 'D 2 2', 'D 2 3', 'D 2 4', 'D 2 5', 'D 3 1', 'D 3 2', 'D 3 3', 'D 3 4', 'D 3 5', 'D 4 1', 'D 4 2', 'D 4 3', 'D 4 4', 'D 4 5', 'D 5 1', 'D 5 2', 'D 5 3', 'D 5 4', 'D 5 5', 'D 6 1', 'D 6 2', 'D 6 3', 'D 6 4', 'D 6 5', 'J 1 1', 'J 1 2', 'J 1 3', 'J 1 4', 'J 1 5', 'J 2 1', 'J 2 2', 'J 2 3', 'J 2 4', 'J 2 5', 'J 3 1', 'J 3 2', 'J 3 3', 'J 3 4', 'J 3 5', 'J 4 1', 'J 4 2', 'J 4 3', 'J 4 4', 'J 4 5', 'J 5 1', 'J 5 2', 'J 5 3', 'J 5 4', 'J 5 5', 'J 6 1', 'J 6 2', 'J 6 3', 'J 6 4', 'J 6 5', 'R 1 1', 'R 1 2', 'R 1 3', 'R 1 4', 'R 1 5', 'R 2 1', 'R 2 2', 'R 2 3', 'R 2 4', 'R 2 5', 'R 3 1', 'R 3 2', 'R 3 3', 'R 3 4', 'R 3 5', 'R 4 1', 'R 4 2', 'R 4 3', 'R 4 4', 'R 4 5', 'R 5 1', 'R 5 2', 'R 5 3', 'R 5 4', 'R 5 5', 'R 6 1', 'R 6 2', 'R 6 3', 'R 6 4', 'R 6 5', 'U 1 1', 'U 1 2', 'U 1 3', 'U 1 4', 'U 1 5', 'U 2 1', 'U 2 2', 'U 2 3', 'U 2 4', 'U 2 5', 'U 3 1', 'U 3 2', 'U 3 3', 'U 3 4', 'U 3 5', 'U 4 1', 'U 4 2', 'U 4 3', 'U 4 4', 'U 4 5', 'U 5 1', 'U 5 2', 'U 5 3', 'U 5 4', 'U 5 5', 'U 6 1', 'U 6 2', 'U 6 3', 'U 6 4', 'U 6 5', 'W 1 1', 'W 1 2', 'W 1 3', 'W 1 4', 'W 1 5', 'W 2 1', 'W 2 2', 'W 2 3', 'W 2 4', 'W 2 5', 'W 3 1', 'W 3 2', 'W 3 3', 'W 3 4', 'W 3 5', 'W 4 1', 'W 4 2', 'W 4 3', 'W 4 4', 'W 4 5', 'W 5 1', 'W 5 2', 'W 5 3', 'W 5 4', 'W 5 5', 'W 6 1', 'W 6 2', 'W 6 3', 'W 6 4', 'W 6 5'])




plt.axvline(5.5, color='k', linewidth=2)
plt.axvline(11.5, color='k', linewidth=2)
plt.axvline(17.5, color='k', linewidth=2)
plt.axvline(23.5, color='k', linewidth=2)
#plt.axvline(24.5, color='k', linewidth=2)
#plt.axvline(29.5, color='k', linewidth=2)

plt.axhline(29.5, color='k', linewidth=2)
plt.axhline(59.5, color='k', linewidth=2)
plt.axhline(89.5, color='k', linewidth=2)
plt.axhline(119.5, color='k', linewidth=2)


plt.axhline(4.5, color='k', linewidth=1, linestyle='--')
plt.axhline(9.5, color='k', linewidth=1, linestyle='--')
plt.axhline(14.5, color='k', linewidth=1, linestyle='--')
plt.axhline(19.5, color='k', linewidth=1, linestyle='--')
plt.axhline(24.5, color='k', linewidth=1, linestyle='--')
plt.axhline(29.5, color='k', linewidth=1, linestyle='--')
plt.axhline(34.5, color='k', linewidth=1, linestyle='--')
plt.axhline(39.5, color='k', linewidth=1, linestyle='--')
plt.axhline(44.5, color='k', linewidth=1, linestyle='--')
plt.axhline(49.5, color='k', linewidth=1, linestyle='--')
plt.axhline(54.5, color='k', linewidth=1, linestyle='--')
plt.axhline(59.5, color='k', linewidth=1, linestyle='--')
plt.axhline(64.5, color='k', linewidth=1, linestyle='--')
plt.axhline(69.5, color='k', linewidth=1, linestyle='--')
plt.axhline(74.5, color='k', linewidth=1, linestyle='--')
plt.axhline(79.5, color='k', linewidth=1, linestyle='--')
plt.axhline(84.5, color='k', linewidth=1, linestyle='--')
plt.axhline(89.5, color='k', linewidth=1, linestyle='--')
plt.axhline(94.5, color='k', linewidth=1, linestyle='--')
plt.axhline(99.5, color='k', linewidth=1, linestyle='--')
plt.axhline(104.5, color='k', linewidth=1, linestyle='--')
plt.axhline(109.5, color='k', linewidth=1, linestyle='--')
plt.axhline(114.5, color='k', linewidth=1, linestyle='--')
plt.axhline(119.5, color='k', linewidth=1, linestyle='--')
plt.axhline(124.5, color='k', linewidth=1, linestyle='--')
plt.axhline(129.5, color='k', linewidth=1, linestyle='--')
plt.axhline(134.5, color='k', linewidth=1, linestyle='--')
plt.axhline(139.5, color='k', linewidth=1, linestyle='--')
plt.axhline(144.5, color='k', linewidth=1, linestyle='--')
plt.axhline(149.5, color='k', linewidth=1, linestyle='--')

plt.title('Accuracy Matrix: Each Dataset Applied to All Models (Grouped Takes --- Batch of 100)')
plt.ylabel('Data',rotation=90)
plt.xlabel('Model')
plt.show()




'''
['D 1', 'D 2', 'D 3', 'D 4', 'D 5', 'D 6', 'J 1', 'J 2', 'J 3', 'J 4', 'J 5', 'J 6', 'R 1', 'R 2', 'R 3', 'R 4', 'R 5', 'R 6', 'U 1', 'U 2', 'U 3', 'U 4', 'U 5', 'U 6', 'W 1', 'W 2', 'W 3', 'W 4', 'W 5', 'W 6']
'''


