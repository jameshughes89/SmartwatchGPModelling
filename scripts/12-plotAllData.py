import csv
from math import *
import matplotlib.pylab as plt
import numpy as np


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
			count+= 1
			iFile = csv.reader(open('../' + tsk + '_' + str(sub) + '_' + str(tke) + '_Z.csv', 'r'))
			
			data = []

			for l in iFile:
				data.append(l)

			data = np.array(data)
			data = data.astype(np.float)

			signal = data.T[-1]


			plt.plot(signal)
			plt.show()
