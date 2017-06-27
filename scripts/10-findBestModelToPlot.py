'''
Finds the model with the best accuracy. This basically is the same as script 2, but whatever. 


'''
import numpy as np
import csv
import sys

#tasks = ['Down', 'Jogging', 'Running', 'Up', 'Walking']
tasks = ['Down', 'Up', 'Walking', 'Jogging', 'Running']
subjects = [1,2,3,4,5,6]
takes = [1,2,3,4,5]

#TIME = '10s'
TIME = '20s'
#TIME = 'all'

totallyBest = sys.maxint
name = ''
funcNumber = -1


count = 0
for tsk in tasks:
	for sub in subjects:
		for tke in takes:
			print tsk, sub, tke

			bestInd = -1;
			bestVal = sys.float_info.max
			iFile = csv.reader(open('../outsSM_' + TIME + '/' + tsk + '_' + str(sub) + '_' + str(tke) + '_Z_' + TIME + '/stats.csv', 'r'))
			
			for l in iFile:
				if float(l[1]) < bestVal:
					bestVal = float(l[1])
					bestInd = int(l[0])
			print '\t\t', bestInd, bestVal

			if bestVal < totallyBest:
				totallyBest = bestVal
				name = tsk + ' ' + str(sub) + ' ' + str(tke)
				funcNumber = count



			count+=1

print totallyBest
print name
print funcNumber
