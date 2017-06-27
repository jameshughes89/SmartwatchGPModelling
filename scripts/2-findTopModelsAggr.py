'''
NOT DONE YET
'''

import numpy as np
import csv
import sys

tasks = ['Down', 'Jogging', 'Running', 'Up', 'Walking']
takes = [1,2,3,4,5]

allBestVal = []
allBestInd = []
bestExpressions = []

for tsk in tasks:
		for tke in takes:
			print tsk, tke

			bestInd = -1;
			bestVal = sys.float_info.max
			iFile = csv.reader(open('../outs_All/' + tsk + '_' + str(tke) + '_Z_All/stats.csv', 'r'))
			
			for l in iFile:
				if float(l[1]) < bestVal:
					bestVal = float(l[1])
					bestInd = int(l[0])
			print '\t\t', bestInd, bestVal
			allBestVal.append(bestVal)
			allBestInd.append(bestInd)

			iFile = open('../outs_All/' + tsk + '_' + str(tke) + '_Z_All/' + str(allBestInd[-1]) + '_line.txt','r')
			bestExpressions.append(iFile.next())
			iFile.close()


			

oFile = open('bestExpressions_All.txt','w')	
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
oFile.close()

