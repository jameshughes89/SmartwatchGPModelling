'''
does an accuracy matric. This ones does a vote though, which means it uses the 4 models trained on the other takes from the subject/task combo. It also only creates a 150x30 matrix. 

It's... complicated. It takes some subset of data points (|GROUP_SIZE|) (these are not necessairly continuous as this is time independent) and does the accuracy. This is then done 100 times. 

'''

import numpy as np
import csv
import sys
from math import *

#------#
#TIME = '10s'
#TIME = '20s'	# CHANGE import below too!
TIME = 'all'
# CHANGE BELOW TOO
import bestExpressions_all as bexp		# YOU HAVE TO CHANGE ME TOO!
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

			iFile = csv.reader(open('../' + tsk + '_' + str(sub) + '_' + str(tke) + '_Z.csv', 'r'))
			
			data = []

			for l in iFile:
				data.append(l)

			data = np.array(data)
			data = data.astype(np.float)


			#count = 0
			#accRow = np.zeros(len(funcs))
			accRow = np.zeros(len(funcs)/5)
			#for i in range(0,data.shape[0], GROUP_SIZE):
			for i in range(100):
				abEs = []
				#count+=1
				#for l in data[i:i+GROUP_SIZE]:
				np.random.shuffle(data)
				for l in data[:GROUP_SIZE]:
					abE = []
					for f_group in range(0,150,5):
						err = 0;
						for f_group_count in range(0,5):
							if count % 5 == f_group_count:		#ignore the 5th vote (to keep it even across all votes (4 votes on all, except 5 on all but the one)
								continue
							try:
								err+= (l[8] - funcs[f_group + f_group_count](l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8]))
							except (ValueError, OverflowError, ZeroDivisionError):
								#err = float('nan')
								sys.float_info.max
						
						abE.append(abs(err))
					abEs.append(abE)
			
				#accRow[np.argmin(np.mean(abEs,axis=0))] += (1./(float(data.shape[0])/float(GROUP_SIZE)))
				accRow[np.argmin(np.mean(abEs,axis=0))] += (1.)
			accRow = accRow/float(100)
			accMat.append(accRow)
			count+= 1

np.savetxt('5-accMatVote_G'+str(GROUP_SIZE)+'_' + TIME + '.csv', accMat, delimiter=",")



