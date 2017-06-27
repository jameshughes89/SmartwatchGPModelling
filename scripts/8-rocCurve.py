'''
Generates the ROC curve (kinda...) for the data based on the number of data poitns in GROUP SIZE

*
****************
NOTE TO JAMES:
		What if there was a curve for each task? May emphasize what tasks suck?
****************
*

'''

import numpy as np
import csv
import sys
from math import *


#------#
#TIME = '10s'
#TIME = '20s'			# change import below too!
TIME = 'all'
# CHANGE BELOW TOO
import bestExpressions_20s as bexp		# YOU HAVE TO CHANGE ME TOO!
# CHANGE ABOVE TOO
funcs = bexp.getFuncs()
#------#


#tasks = ['Down', 'Jogging', 'Running', 'Up', 'Walking']
tasks = ['Down', 'Up', 'Walking', 'Jogging', 'Running']
subjects = [1,2,3,4,5,6]
takes = [1,2,3,4,5]


ROCstuff = []
for GS in range(5,121,5):
	GROUP_SIZE = GS

	accMat = []
	count = 0
	for tsk in tasks:
		for sub in subjects:
			for tke in takes:
					
				print tsk, sub, tke, count, GROUP_SIZE		
				count+= 1
				iFile = csv.reader(open('../' + tsk + '_' + str(sub) + '_' + str(tke) + '_Z.csv', 'r'))
			
				data = []

				for l in iFile:
					data.append(l)

				data = np.array(data)
				data = data.astype(np.float)


				#count = 0
				accRow = np.zeros(len(funcs))
				#for i in range(0,data.shape[0], GROUP_SIZE):
				for i in range(100):
					abEs = []
					#count+=1
					#for l in data[i:i+GROUP_SIZE]:
					#np.random.shuffle(data)
					#for l in data[:GROUP_SIZE]:
					for l in data[np.random.permutation(len(data))[:GROUP_SIZE]]:
						abE = []
						for f in funcs:
							try:
								err = l[8] - f(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8])
							except OverflowError:
								err = sys.float_info.max
							abE.append(abs(err))
						abEs.append(abE)
			
					#accRow[np.argmin(np.mean(abEs,axis=0))] += (1./(float(data.shape[0])/float(GROUP_SIZE)))
					if np.argmin(np.mean(abEs,axis=0)) > 0.000:			
						accRow[np.argmin(np.mean(abEs,axis=0))] += (1.)
				accRow = accRow/float(100)
				accMat.append(accRow)

	accMat = np.array(accMat)
	accMatSmall = []
	for i in range(0, accMat.shape[0], 1):
		accMatRow = []
		for j in range(0, accMat.shape[1], 5):
			accMatRow.append(np.sum(accMat[i,j:j+5]))
		accMatSmall.append(accMatRow)



	accMatSmall = np.array(accMatSmall)
	a = []
	for i in range(30):
		for j in range(5):
		    a.append(accMatSmall[i*5+j,i])

	ROCstuff.append([np.mean(a), np.std(a), np.median(a), np.min(a), np.max(a), len(funcs)])

np.savetxt('8-roc-' + TIME + '.csv', ROCstuff, delimiter=",")


