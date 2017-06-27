'''
Creates the statistics file for each subject/task/take. 

'''

import numpy as np
import csv

tasks = ['Down', 'Jogging', 'Running', 'Up', 'Walking']
subjects = [1,2,3,4,5,6]
takes = [1,2,3,4,5]

#TIME = '10s'
#TIME = '20s'
TIME = 'all'

for tsk in tasks:
	for sub in subjects:
		for tke in takes:
			print tsk, sub, tke
			oFile = open('../outsSM_' + TIME + '/' + tsk + '_' + str(sub) + '_' + str(tke) + '_Z_' + TIME + '/stats.csv', 'w')
			for i in range(0, 100, 1):
				iFile = open('../outsSM_' + TIME + '/' + tsk + '_' + str(sub) + '_' + str(tke) + '_Z_' + TIME + '/' + str(i) + '_fit.txt', 'r')
				oFile.write(str(i)+","+iFile.read()+"\n")
			
			oFile.close()	

