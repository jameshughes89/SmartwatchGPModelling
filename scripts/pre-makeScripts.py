################################################

#tasks = ['Down', 'Jogging', 'Running', 'Up', 'Walking']
tasks = ['Down']
#tasks = ['Jogging']
#tasks = ['Running']
#tasks = ['Up']
#tasks = ['Walking']
subjects = [1,2,3,4,5,6]
takes = [1,2,3,4,5]

################################################

#make big file part

#CHANGE THIS NUMBER
oFile = open("rall-no-1.sh", "w")#CHANGE THIS NUMBER
#CHANGE THIS NUMBER
oFile.write("#!/bin/bash\n")

for tsk in tasks:
	for sub in subjects:
		for tke in takes:
			for i in range(0, 100, 1):
				#MIND THE TASK AND L VALUE HERE!!!!
				oFile.write('qsub ' + tsk + '_' + str(sub) + '_' + str(tke) + '_Z-'+str(i)+'.sh\n')

oFile.close()


#make small file part
for tsk in tasks:
	for sub in subjects:
		for tke in takes:
			print tsk, sub, tke
			for i in range(0, 100, 1):
				oFile = open(tsk + '_' + str(sub) + '_' + str(tke) + '_Z-'+str(i)+'.sh', "w")
				oFile.write("#!/bin/bash\n")
				oFile.write("#PBS -l nodes=1:ppn=8\n")
				oFile.write("#PBS -l walltime=0:30:00\n")
				oFile.write("#PBS -N jGPv7-tsk + '_' + str(sub) + '_' + str(tke) + '_Z-"+str(i)+"\n")
				oFile.write("module load java\n")
				oFile.write("cd /scratch/m/mdaley/jhughe54/jGPv7-SM/src/\n")
				#MIND THE TASK AND THE L VALUE HERE!!!!
				oFile.write('java Centre ' + tsk + '_' + str(sub) + '_' + str(tke) + '_Z '+str(i)+' 1\n')
				oFile.close()
