'''
Finds the top model for each subject/task/take and saves them to a file bestExpression_TIME.txt
'''
import numpy as np
import csv
import sys

#tasks = ['Down', 'Jogging', 'Running', 'Up', 'Walking']
tasks = ['Down', 'Up', 'Walking', 'Jogging', 'Running']
subjects = [1,2,3,4,5,6]
takes = [1,2,3,4,5]

#TIME = '10s'
#TIME = '20s'
TIME = 'all'

allBestVal = []
allBestInd = []
bestExpressions = []

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
			allBestVal.append(bestVal)
			allBestInd.append(bestInd)

			iFile = open('../outsSM_' + TIME + '/' + tsk + '_' + str(sub) + '_' + str(tke) + '_Z_' + TIME + '/' + str(allBestInd[-1]) + '_line.txt','r')
			bestExpressions.append(iFile.next())
			iFile.close()


			

oFile = open('bestExpressions_' + TIME + '.py','w')	
oFile.write("from math import *\n\n")
fs='funcs = ['
count = 0
for l in bestExpressions:
	oFile.write('def func_' + str(count) + '(v0,v1,v2,v3,v4,v5,v6,v7,v8): return ' + l + '\n')		#CHANGE HERE (in function name)
	fs = fs + "func_" + str(count)
	if count != len(bestExpressions) - 1:
		fs = fs + ","	

	count += 1

fs = fs + "]"
oFile.write("\n" + fs)

oFile.write("\n\ndef getFuncs(): return funcs\n")
oFile.close()

