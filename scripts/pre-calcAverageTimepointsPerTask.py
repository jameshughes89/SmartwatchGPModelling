import numpy as np
import csv

#tasks = ['Down', 'Jogging', 'Running', 'Up', 'Walking']
tasks = ['Down', 'Up', 'Walking', 'Jogging', 'Running']
subjects = [1,2,3,4,5,6]
takes = [1,2,3,4,5]

TIME = '20s'

matrixMSE = []
matrixABE = []

count = 0

for tsk in tasks:
	
	#taskDataPoints = []	
	
	for sub in subjects:

		subjDataPoints = []		
		
		for tke in takes:
						
			#print tsk, sub, tke, count
			count+= 1

			#this should be on the whole data
			iFile = csv.reader(open('../' + tsk + '_' + str(sub) + '_' + str(tke) + '_Z.csv', 'r'))
			data = []
			for l in iFile:
				data.append(l)
			data = np.array(data)
			data = data.astype(np.float)
			
			#taskDataPoints.append(data.shape[0])
			subjDataPoints.append(data.shape[0])
		print tsk, sub, np.mean(subjDataPoints)
	#print tsk, np.mean(taskDataPoints)

