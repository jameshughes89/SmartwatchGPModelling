import numpy as np
import csv

tasks = ['Down', 'Jogging', 'Running', 'Up', 'Walking']
subjects = [1,2,3,4,5,6]
takes = [1,2,3,4,5]

allmsE = []
allabE = []

for tsk in tasks:
	for sub in subjects:
		for tke in takes:		
			print tsk, sub, tke

			iFile = csv.reader(open('../' + tsk + '_' + str(sub) + '_' + str(tke) + '_Z.csv', 'r'))
			data = []

			for l in iFile:
				data.append(l)

			data = np.array(data)
			data = data.astype(np.float)


			for i in range(0,data.shape[0], 15):
				np.savetxt('../splitData/' + tsk + '_' + str(sub) + '_' + str(tke) + '_Z_' + str(i) + '.csv', data[i:i+15], delimiter=",")
