'''
Not Converted Yet

'''
import numpy as np
import csv

tasks = ['Down', 'Jogging', 'Running', 'Up', 'Walking']
takes = [1,2,3,4,5]

for tsk in tasks:
		for tke in takes:
			print tsk, tke
			oFile = open('../outs_All/' + tsk + '_' + str(tke) + '_Z_All/stats.csv', 'w')
			for i in range(0, 100, 1):
				iFile = open('../outs_All/' + tsk + '_' + str(tke) + '_Z_All/' + str(i) + '_fit.txt', 'r')
				oFile.write(str(i)+","+iFile.read()+"\n")
			
			oFile.close()	

