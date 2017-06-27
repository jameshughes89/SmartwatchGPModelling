import numpy as np
import csv

tasks = ['Down', 'Jogging', 'Running', 'Up', 'Walking']
subjects = [1,2,3,4,5,6]
takes = [1,2,3,4,5]

allmsE = []
allabE = []

for tsk in tasks:
	for tke in takes:	
		for sub in subjects:
			print tsk, sub, tke

			iFile = csv.reader(open('../' + tsk + '_' + str(sub) + '_' + str(tke) + '_Z.csv', 'r'))
			data = []

			for l in iFile:
				data.append(l)

		data = np.array(data).astype(np.float)
		np.savetxt('../' + tsk + '_' + str(tke) + '_Z_All.csv', data, delimiter=",")
