'''
does an accuracy matric. Basicially, it picks the task that the data fits closest to, BUT it ignores the take the model was trained on. 

It's... complicated. It takes some subset of data points (|GROUP_SIZE|) (these are not necessairly continuous as this is time independent) and does the accuracy. This is then done 100 times. 

'''

import numpy as np
import csv
import sys
from math import *

#------#
#TIME = '10s'
TIME = '20s'	# CHANGE import below too!
#TIME = 'all'
# CHANGE BELOW TOO
import bestExpressions_20s as bexp		# YOU HAVE TO CHANGE ME TOO!
# CHANGE ABOVE TOO
funcs = bexp.getFuncs()
#------#

GROUP_SIZE = 50		# CHANGE ME


#tasks = ['Down', 'Jogging', 'Running', 'Up', 'Walking']
tasks = ['Down', 'Up', 'Walking', 'Jogging', 'Running']
subjects = [1,2,3,4,5,6]
takes = [1,2,3,4,5]

accMat = []

count = 0


for tsk in tasks:
	for sub in subjects:
		for tke in takes:
					
			print tsk, sub, tke, count			
			#count+= 1
			iFile = csv.reader(open('../' + tsk + '_' + str(sub) + '_' + str(tke) + '_Z.csv', 'r'))
			
			data = []

			for l in iFile:
				data.append(l)

			data = np.array(data)
			data = data.astype(np.float)


			#count = 0
			accRow = np.zeros(len(funcs))
			#for i in range(0,data.shape[0], GROUP_SIZE):
			for i in range(100):# IF YOU CHANGE ME, CHANGE The accRow/float near bottom!
				abEs = []
				#count+=1
				#for l in data[i:i+GROUP_SIZE]:
				#np.random.shuffle(data)
				#for ct1, l in enumerate(data[:GROUP_SIZE]):
				for ct1, l in enumerate(data[np.random.permutation(len(data))[:GROUP_SIZE]]):				
					abE = []
					for ct2, f in enumerate(funcs):
						#if ct2 - (count -  count%5)  > 5 or count - (ct2 -  ct2%5)  > 5:
						if count != ct2:
							try:							
								err = l[8] - f(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8])
							except (ValueError, OverflowError, ZeroDivisionError):
								#err = float('nan')
								sys.float_info.max

							abE.append(abs(err))
						else:
							abE.append(sys.maxint)
					abEs.append(abE)
			
				#accRow[np.argmin(np.mean(abEs,axis=0))] += (1./(float(data.shape[0])/float(GROUP_SIZE)))
				accRow[np.argmin(np.mean(abEs,axis=0))] += (1.)
			accRow = accRow/float(100)
			accMat.append(accRow)
			count+=1


np.savetxt('5-accMatNoSameTake_G'+str(GROUP_SIZE)+'_' + TIME + '.csv', accMat, delimiter=",")



