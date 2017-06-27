'''
Counts the number of times each variable was in ONLY THE TOP generated models. 
'''

import numpy as np
import csv
import sys
import matplotlib.pylab as plt

tasks = ['Down', 'Jogging', 'Running', 'Up', 'Walking']
subjects = [1,2,3,4,5,6]
takes = [1,2,3,4,5]

dimensions=["acc_x", "acc_y", "acc_z", "mag_x", "mag_y", "mag_z", "gyro_x", "gyro_y", "gyro_z"]

#TIME = '10s'
#TIME = '20s'
TIME = 'all'

allBestVal = []
allBestInd = []
allmsE = []
allabE = []


allVarCounts = []

for tsk in tasks:
	for sub in subjects:
		for tke in takes:		
			fcount = np.zeros(9)
			print tsk, sub, tke

			bestInd = -1;
			bestVal = sys.float_info.max
			iFile = csv.reader(open('../outsSM_' + TIME + '/' + tsk + '_' + str(sub) + '_' + str(tke) + '_Z_' + TIME + '/stats.csv', 'r'))
			
			for l in iFile:
				if float(l[1]) < bestVal:
					bestVal = float(l[1])
					bestInd = int(l[0])
			print '\t\t', bestInd, bestVal
			allBestVal.append(bestVal)
			allBestInd.append(bestInd)

			iFile = csv.reader(open('../outsSM_' + TIME + '/' + tsk + '_' + str(sub) + '_' + str(tke) + '_Z_' + TIME + '/' + str(allBestInd[-1]) + '_multi.txt','r'), delimiter='\t')
				
			for line in iFile:
				if(line[-1][0] == 'v'):
					eInt = int(line[-1][1:])
					fcount[eInt] = 1

			fcount[-1] = 1
			allVarCounts.append(fcount)




plt.matshow(allVarCounts, aspect='auto')
plt.colorbar()
plt.title('Devices when trained on ' + TIME + ' of Data --- Top Only')
plt.ylabel('Subjects and Tasks')
for i in range(len(tasks)):
	plt.axhline(i*len(subjects)*len(takes)-.5, color='k', linewidth=2.0)

plt.xlabel('Device')
plt.xticks(range(len(dimensions)), dimensions)
for i in range(0, len(dimensions), 3):
	plt.axvline(i-.5, color='k', linewidth=2.0)
plt.show()





