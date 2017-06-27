'''
Counts the number of times each variable was in all of the generated models. 

Does it for the 10s and 20s thing
'''

import numpy as np
import csv
import sys
import matplotlib.pylab as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

tasks = ['Down', 'Up', 'Walking', 'Jogging', 'Running']
subjects = [1,2,3,4,5,6]
takes = [1,2,3,4,5]

dimensions=["acc_x", "acc_y", "acc_z", "mag_x", "mag_y", "mag_z", "gyro_x", "gyro_y", "gyro_z"]

TIME = '10s'
#TIME = '20s'
#TIME = 'all'

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
pltz = []
axes = plt.subplot2grid((1,2), (0,0))
pltz.append(axes)
img = pltz[0].matshow(allVarCounts, aspect='auto')
#pltz[0].colorbar(label='% Models Containing Feature')
pltz[0].set_title(TIME + ' of the Data', fontsize=12)
pltz[0].set_ylabel('Subjects and Tasks')
pltz[0].set_yticks(range(15,150, 30))
pltz[0].set_yticklabels(tasks, rotation=90)
for i in range(len(tasks)):
	pltz[0].axhline(i*len(subjects)*len(takes)-1, color='k', linewidth=2.0)

for i in range(4,150,5):
	pltz[0].axhline(i, color='k', linewidth=1.0, linestyle='--')


pltz[0].set_xlabel('Device')
pltz[0].set_xticks(range(len(dimensions)))
pltz[0].set_xticklabels(dimensions,rotation=90)
for i in range(0, len(dimensions), 3):
	pltz[0].axvline(i-.5, color='k', linewidth=2.0)

#pltz[0].show()




dimensions=["acc_x", "acc_y", "acc_z", "mag_x", "mag_y", "mag_z", "gyro_x", "gyro_y", "gyro_z"]

#TIME = '10s'
TIME = '20s'
#TIME = 'all'

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
axes = plt.subplot2grid((1,2), (0,1))
pltz.append(axes)
img = pltz[1].matshow(allVarCounts, aspect='auto')
#plt.colorbar(label='% Models Containing Feature')
pltz[1].set_title(TIME + ' of the Data', fontsize=12)
#pltz[1].set_ylabel('Subjects and Tasks')
pltz[1].set_yticks(range(15,150, 30))
pltz[1].set_yticklabels(tasks, rotation=90)
for i in range(len(tasks)):
	pltz[1].axhline(i*len(subjects)*len(takes)-1, color='k', linewidth=2.0)

for i in range(4,150,5):
	pltz[1].axhline(i, color='k', linewidth=1.0, linestyle='--')


pltz[1].set_xlabel('Device')
pltz[1].set_xticks(range(len(dimensions)))
pltz[1].set_xticklabels(dimensions,rotation=90)
for i in range(0, len(dimensions), 3):
	pltz[1].axvline(i-.5, color='k', linewidth=2.0)

plt.suptitle('Features When Trained on: ',fontsize=16)
divider = make_axes_locatable(axes)
cax = divider.append_axes("right", size="5%", pad=0.05)
plt.colorbar(img, cax = cax, label='% Models Containing Feature')
plt.show()


'''
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
'''



