'''
Counts the number of times each variable was in all of the generated models. 
'''

import numpy as np
import csv
import sys
import matplotlib.pylab as plt

tasks = ['Down', 'Up', 'Walking', 'Jogging', 'Running']
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
			for i in range(100):
				iFile = csv.reader(open('../outsSM_' + TIME + '/' + tsk + '_' + str(sub) + '_' + str(tke) + '_Z_' + TIME + '/' + str(i) + '_multi.txt','r'), delimiter='\t')

				fBool = [False] * 9			
				for line in iFile:
					if(line[-1][0] == 'v'):
						eInt = int(line[-1][1:])
				
						if(not(fBool[eInt])):
							fBool[eInt] = True
							fcount[eInt] += 1


			fcount[-1] = 100
			allVarCounts.append(fcount)


allVarCounts = np.array(allVarCounts)
plt.matshow(allVarCounts, aspect='auto')
plt.colorbar(label='% Models Containing Feature')
plt.title('Features When Trained on ' + TIME + ' of the Data')
plt.ylabel('Subjects and Tasks')
plt.yticks(range(15,150, 30), tasks, rotation=90)
for i in range(len(tasks)):
	plt.axhline(i*len(subjects)*len(takes)-1, color='k', linewidth=2.0)

for i in range(4,150,5):
	plt.axhline(i, color='k', linewidth=1.0, linestyle='--')


plt.xlabel('Device')
plt.xticks(range(len(dimensions)), dimensions,rotation=90)
for i in range(0, len(dimensions), 3):
	plt.axvline(i-.5, color='k', linewidth=2.0)
plt.show()


# # # #
# TRANSPOSED VERSION  
# # # #

plt.matshow(allVarCounts.T, aspect='auto')
plt.colorbar(label='% Models Containing Feature')
plt.title('Features When Trained on ' + TIME + ' of the Data')
plt.xlabel('Subjects and Tasks')
plt.xticks(range(15,150, 30), tasks)
for i in range(len(tasks)):
	plt.axvline(i*len(subjects)*len(takes)-0.5, color='k', linewidth=2.0)

for i in range(4,150,5):
	plt.axvline(i+0.5, color='k', linewidth=1.0, linestyle='--')

plt.ylabel('Device')
plt.yticks(range(len(dimensions)), dimensions)
for i in range(0, len(dimensions), 3):
	plt.axhline(i-.5, color='k', linewidth=2.0)
plt.show()




