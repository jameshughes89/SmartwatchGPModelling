'''
Creates the error (or whatever metric we want to use) matrix when each model is applied to all data. It saves it to a file 3-metriCmat_TIME.csv
'''

import numpy as np
import csv
import sys
from math import *


#------#
#TIME = '10s'
#TIME = '20s'
TIME = 'all'
# CHANGE BELOW TOO
import bestExpressions_all as bexp		# YOU HAVE TO CHANGE ME TOO!
# CHANGE ABOVE TOO
funcs = bexp.getFuncs()
#------#

#tasks = ['Down', 'Jogging', 'Running', 'Up', 'Walking']
tasks = ['Down', 'Up', 'Walking', 'Jogging', 'Running']
subjects = [1,2,3,4,5,6]
takes = [1,2,3,4,5]

matrixMSE = []
matrixABE = []

count = 0

for tsk in tasks:
	for sub in subjects:
		for tke in takes:
						
			print tsk, sub, tke, count
			count+= 1

			#this should be on the whole data
			iFile = csv.reader(open('../' + tsk + '_' + str(sub) + '_' + str(tke) + '_Z.csv', 'r'))
			
			data = []

			for l in iFile:
				data.append(l)

			data = np.array(data)
			data = data.astype(np.float)
		
			allmsE = []
			allabE = []

			for f in funcs:
				try:			
					msE = []
					abE = []			
					for l in data:
						err = l[8] - f(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8])
						msE.append(err**2)
						abE.append(abs(err))
					
					allmsE.append((np.mean(msE)))
					allabE.append((np.mean(abE)))
					#allmsE.append(log(np.mean(msE)))
					#allabE.append(log(np.mean(abE)))
				except Exception:
					print '\t\t\tBBBBBUSTTTEDDDD: ', tsk, sub, tke
					allmsE.append(np.float('nan'))
					allabE.append(np.float('nan'))
					continue


			matrixMSE.append(allmsE)
			matrixABE.append(allabE)

np.savetxt('3-msEmat_' + TIME + '.csv', matrixMSE, delimiter=",")
np.savetxt('3-abEmat_' + TIME + '.csv', matrixABE, delimiter=",")


