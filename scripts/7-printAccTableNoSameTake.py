'''
Prints a table form of the accuracy (as opposed to the whole matrix).

Don't forget to change GROUP_SIZE
'''

import numpy as np
import csv
import sys
import scipy.stats
from math import *
import matplotlib
import matplotlib.pylab as plt


def calcCI(a):
	return scipy.stats.norm.interval(0.95, loc=np.mean(a), scale=(np.std(a)/np.sqrt(len(a))))[1] - np.mean(a)	# return 1 because 0 is the negative

#TIME = '10s'
TIME = '20s'
#TIME = 'all'

GROUP_SIZE = 50		# CHANGE ME


#tasks = ['Down', 'Jogging', 'Running', 'Up', 'Walking']
tasks = ['Down', 'Up', 'Walking', 'Jogging', 'Running']
iFile =  csv.reader(open('5-accMatNoSameTake_G' + str(GROUP_SIZE) + '_' + TIME + '.csv', 'r'))

accMat = []
for l in iFile:
	accMat.append(l)
accMat = np.array(accMat)
accMat = accMat.astype(np.float)



accMatSmall = []
for i in range(0, accMat.shape[0], 1):
	accMatRow = []
	for j in range(0, accMat.shape[1], 5):
		accMatRow.append(np.sum(accMat[i,j:j+5]))
	accMatSmall.append(accMatRow)


accMatSmall = np.array(accMatSmall)


#for i in range(0,30,6):
#	for j in range(0,30,5):
#		for k in range(0,6):			
#			print i,j,k, np.mean(accMatSmall[j:j+5,i+k])

print
print "DOWN:"
print np.mean(accMatSmall[0:0+5,0]), np.mean(accMatSmall[5:5+5,1]), np.mean(accMatSmall[10:10+5,2]), np.mean(accMatSmall[15:15+5,3]), np.mean(accMatSmall[20:20+5,4]), np.mean(accMatSmall[25:25+5,5])

print
print "JOGGING:"
print np.mean(accMatSmall[30:30+5,6]), np.mean(accMatSmall[35:35+5,7]), np.mean(accMatSmall[40:40+5,8]), np.mean(accMatSmall[45:45+5,9]), np.mean(accMatSmall[50:50+5,10]), np.mean(accMatSmall[55:55+5,11])

print
print "Running:"
print np.mean(accMatSmall[60:60+5,12]), np.mean(accMatSmall[65:65+5,13]), np.mean(accMatSmall[70:70+5,14]), np.mean(accMatSmall[75:75+5,15]), np.mean(accMatSmall[80:80+5,16]), np.mean(accMatSmall[85:85+5,17])

print
print "UP:"
print np.mean(accMatSmall[90:90+5,18]), np.mean(accMatSmall[95:95+5,19]), np.mean(accMatSmall[100:100+5,20]), np.mean(accMatSmall[105:105+5,21]), np.mean(accMatSmall[110:110+5,22]), np.mean(accMatSmall[115:115+5,23])

print
print "WALKING:"
print np.mean(accMatSmall[120:120+5,24]), np.mean(accMatSmall[125:125+5,25]), np.mean(accMatSmall[130:130+5,26]), np.mean(accMatSmall[135:135+5,27]), np.mean(accMatSmall[140:140+5,28]), np.mean(accMatSmall[145:145+5,29])



accs = []
d = []
d.append(np.mean(accMatSmall[0:0+5,0]))
d.append(np.mean(accMatSmall[5:5+5,1]))
d.append(np.mean(accMatSmall[10:10+5,2]))
d.append(np.mean(accMatSmall[15:15+5,3]))
d.append(np.mean(accMatSmall[20:20+5,4]))
d.append(np.mean(accMatSmall[25:25+5,5]))

j = []
j.append(np.mean(accMatSmall[30:30+5,6]))
j.append(np.mean(accMatSmall[35:35+5,7]))
j.append(np.mean(accMatSmall[40:40+5,8]))
j.append(np.mean(accMatSmall[45:45+5,9]))
j.append(np.mean(accMatSmall[50:50+5,10]))
j.append(np.mean(accMatSmall[55:55+5,11]))

r = []
r.append(np.mean(accMatSmall[60:60+5,12]))
r.append(np.mean(accMatSmall[65:65+5,13]))
r.append(np.mean(accMatSmall[70:70+5,14]))
r.append(np.mean(accMatSmall[75:75+5,15]))
r.append(np.mean(accMatSmall[80:80+5,16]))
r.append(np.mean(accMatSmall[85:85+5,17]))

u = []
u.append(np.mean(accMatSmall[90:90+5,18]))
u.append(np.mean(accMatSmall[95:95+5,19]))
u.append(np.mean(accMatSmall[100:100+5,20]))
u.append(np.mean(accMatSmall[105:105+5,21]))
u.append(np.mean(accMatSmall[110:110+5,22]))
u.append(np.mean(accMatSmall[115:115+5,23]))

w = []
w.append(np.mean(accMatSmall[120:120+5,24]))
w.append(np.mean(accMatSmall[125:125+5,25]))
w.append(np.mean(accMatSmall[130:130+5,26]))
w.append(np.mean(accMatSmall[135:135+5,27]))
w.append(np.mean(accMatSmall[140:140+5,28]))
w.append(np.mean(accMatSmall[145:145+5,29]))

accs.append(d)
accs.append(j)
accs.append(r)
accs.append(u)
accs.append(w)




#_#_#_#_#_#_#_#_#_#_#
print
print
print
print

print "Excluding self (this is the good one)"

print
print "DOWN:"
print np.mean(accMatSmall[1:0+5,0]), '$\pm$', '%.4f'%calcCI(accMatSmall[1:0+5,0]), '&', np.mean(accMatSmall[6:5+5,1]), '$\pm$', '%.4f'%calcCI(accMatSmall[6:5+5,1]), '&', np.mean(accMatSmall[11:10+5,2]), '$\pm$', '%.4f'%calcCI(accMatSmall[11:10+5,2]), '&', np.mean(accMatSmall[16:15+5,3]), '$\pm$', '%.4f'%calcCI(accMatSmall[16:15+5,3]), '&', np.mean(accMatSmall[21:20+5,4]), '$\pm$', '%.4f'%calcCI(accMatSmall[21:20+5,4]), '&', np.mean(accMatSmall[26:25+5,5]), '$\pm$', '%.4f'%calcCI(accMatSmall[26:25+5,5])

print
print "JOGGING:"
print np.mean(accMatSmall[31:30+5,6]), '$\pm$', '%.4f'%calcCI(accMatSmall[31:30+5,6]), '&', np.mean(accMatSmall[36:35+5,7]), '$\pm$', '%.4f'%calcCI(accMatSmall[36:35+5,7]), '&', np.mean(accMatSmall[41:40+5,8]), '$\pm$', '%.4f'%calcCI(accMatSmall[41:40+5,8]), '&', np.mean(accMatSmall[46:45+5,9]), '$\pm$', '%.4f'%calcCI(accMatSmall[46:45+5,9]), '&', np.mean(accMatSmall[51:50+5,10]), '$\pm$', '%.4f'%calcCI(accMatSmall[51:50+5,10]), '&', np.mean(accMatSmall[56:55+5,11]), '$\pm$', '%.4f'%calcCI(accMatSmall[56:55+5,11])

print
print "Running:"
print np.mean(accMatSmall[61:60+5,12]), '$\pm$', '%.4f'%calcCI(accMatSmall[61:60+5,12]), '&', np.mean(accMatSmall[66:65+5,13]), '$\pm$', '%.4f'%calcCI(accMatSmall[66:65+5,13]), '&', np.mean(accMatSmall[71:70+5,14]), '$\pm$', '%.4f'%calcCI(accMatSmall[71:70+5,14]), '&', np.mean(accMatSmall[76:75+5,15]), '$\pm$', '%.4f'%calcCI(accMatSmall[76:75+5,15]), '&', np.mean(accMatSmall[81:80+5,16]), '$\pm$', '%.4f'%calcCI(accMatSmall[81:80+5,16]), '&', np.mean(accMatSmall[86:85+5,17]), '$\pm$', '%.4f'%calcCI(accMatSmall[86:85+5,17])

print
print "UP:"
print np.mean(accMatSmall[91:90+5,18]), '$\pm$', '%.4f'%calcCI(accMatSmall[91:90+5,18]), '&', np.mean(accMatSmall[96:95+5,19]), '$\pm$', '%.4f'%calcCI(accMatSmall[96:95+5,19]), '&', np.mean(accMatSmall[101:100+5,20]), '$\pm$', '%.4f'%calcCI(accMatSmall[101:100+5,20]), '&', np.mean(accMatSmall[106:105+5,21]), '$\pm$', '%.4f'%calcCI(accMatSmall[106:105+5,21]), '&', np.mean(accMatSmall[111:110+5,22]), '$\pm$', '%.4f'%calcCI(accMatSmall[111:110+5,22]), '&', np.mean(accMatSmall[116:115+5,23]), '$\pm$', '%.4f'%calcCI(accMatSmall[116:115+5,23])

print
print "WALKING:"
print np.mean(accMatSmall[121:120+5,24]), '$\pm$', '%.4f'%calcCI(accMatSmall[121:120+5,24]), '&', np.mean(accMatSmall[126:125+5,25]), '$\pm$', '%.4f'%calcCI(accMatSmall[126:125+5,25]), '&', np.mean(accMatSmall[131:130+5,26]), '$\pm$', '%.4f'%calcCI(accMatSmall[131:130+5,26]), '&', np.mean(accMatSmall[136:135+5,27]), '$\pm$', '%.4f'%calcCI(accMatSmall[136:135+5,27]), '&', np.mean(accMatSmall[141:140+5,28]), '$\pm$', '%.4f'%calcCI(accMatSmall[141:140+5,28]), '&', np.mean(accMatSmall[146:145+5,29]), '$\pm$', '%.4f'%calcCI(accMatSmall[146:145+5,29])



accs = []
d = []
d.append(np.mean(accMatSmall[1:0+5,0]))
d.append(np.mean(accMatSmall[6:5+5,1]))
d.append(np.mean(accMatSmall[11:10+5,2]))
d.append(np.mean(accMatSmall[16:15+5,3]))
d.append(np.mean(accMatSmall[21:20+5,4]))
d.append(np.mean(accMatSmall[26:25+5,5]))

j = []
j.append(np.mean(accMatSmall[31:30+5,6]))
j.append(np.mean(accMatSmall[36:35+5,7]))
j.append(np.mean(accMatSmall[41:40+5,8]))
j.append(np.mean(accMatSmall[46:45+5,9]))
j.append(np.mean(accMatSmall[51:50+5,10]))
j.append(np.mean(accMatSmall[56:55+5,11]))

r = []
r.append(np.mean(accMatSmall[61:60+5,12]))
r.append(np.mean(accMatSmall[66:65+5,13]))
r.append(np.mean(accMatSmall[71:70+5,14]))
r.append(np.mean(accMatSmall[76:75+5,15]))
r.append(np.mean(accMatSmall[81:80+5,16]))
r.append(np.mean(accMatSmall[86:85+5,17]))

u = []
u.append(np.mean(accMatSmall[91:90+5,18]))
u.append(np.mean(accMatSmall[96:95+5,19]))
u.append(np.mean(accMatSmall[101:100+5,20]))
u.append(np.mean(accMatSmall[106:105+5,21]))
u.append(np.mean(accMatSmall[111:110+5,22]))
u.append(np.mean(accMatSmall[116:115+5,23]))

w = []
w.append(np.mean(accMatSmall[121:120+5,24]))
w.append(np.mean(accMatSmall[126:125+5,25]))
w.append(np.mean(accMatSmall[131:130+5,26]))
w.append(np.mean(accMatSmall[136:135+5,27]))
w.append(np.mean(accMatSmall[141:140+5,28]))
w.append(np.mean(accMatSmall[146:145+5,29]))

accs.append(d)
accs.append(j)
accs.append(r)
accs.append(u)
accs.append(w)


accs = np.array(accs)
print 
print 'total subject and task class'
print np.mean(accs)

###########

accMatSmaller = []
for i in range(0, accMatSmall.shape[0], 1):
	accMatRow = []
	for j in range(0, accMatSmall.shape[1], 6):
		accMatRow.append(np.sum(accMatSmall[i,j:j+6]))
	accMatSmaller.append(accMatRow)

accMatSmaller = np.array(accMatSmaller)

print
print
print "Same Task"
print
print "DOWN:"
print np.mean(accMatSmaller[0:30,0]), '$\pm$', '%.4f'%calcCI(accMatSmaller[0:30,0])

print
print "JOGGING:"
print np.mean(accMatSmaller[30:60,1]), '$\pm$', '%.4f'%calcCI(accMatSmaller[30:60,1])

print
print "Running:"
print np.mean(accMatSmaller[60:90,2]), '$\pm$', '%.4f'%calcCI(accMatSmaller[60:90,2])

print
print "UP:"
print np.mean(accMatSmaller[90:120,3]), '$\pm$', '%.4f'%calcCI(accMatSmaller[90:120,3])

print
print "WALKING:"
print np.mean(accMatSmaller[120:150,4]), '$\pm$', '%.4f'%calcCI(accMatSmaller[120:150,4])


# # # #
# Same Subject 
# # # #


#plt.matshow(accMat)
#plt.matshow(accMatSmaller, aspect='auto')
#plt.show()



accMatSmaller2 = []
for i in range(0, len(accMatSmall), 5):
	row = []
	for j in range(len(accMatSmall[0])):
		row.append(np.mean(accMatSmall[i:i+5, j]))
	accMatSmaller2.append(row)

accMarSmaller2 = np.array(accMatSmaller2)

#plt.matshow(accMatSmall, aspect='auto')
#plt.matshow(accMatSmaller2, aspect='auto')
#plt.show()

print
print
print "Same Subject"
print
for i in range(0,6,1):
	print "subject", i
	curSubAccz = []	
	for j in range(0, 5):
		tmp = [accMarSmaller2[j*6+i,0+i], accMarSmaller2[j*6+i,6+i], accMarSmaller2[j*6+i,12+i], accMarSmaller2[j*6+i,18+i], accMarSmaller2[j*6+i,24+i]]
		#print tmp
		curSubAccz.append(np.sum([accMarSmaller2[j*6+i,0+i], accMarSmaller2[j*6+i,6+i], accMarSmaller2[j*6+i,12+i], accMarSmaller2[j*6+i,18+i], accMarSmaller2[j*6+i,24+i]]))
	print np.mean(curSubAccz), '$\pm$', '%.4f'%calcCI(curSubAccz)
	#print curSubAccz	


#plt.matshow(accMatSmaller2, aspect='auto')
#plt.show()

	#curSubAccz.append(accMatSmaller[0+i*5:5+i*5,0]))
	#print np.mean([np.mean(accMatSmaller[0+i*5:5+i*5,0]), np.mean(accMatSmaller[30+i*5:35+i*5,1]), np.mean(accMatSmaller[60+i*5:65+i*5,2]), np.mean(accMatSmaller[90+i*5:95+i*5,3]), np.mean(accMatSmaller[120+i*5:125+i*5,4])])
	#print '\t', np.mean([np.mean(accMatSmaller[0+i*5:5+i*5,0]), np.mean(accMatSmaller[30+i*5:35+i*5,1]), np.mean(accMatSmaller[60+i*5:65+i*5,2]), np.mean(accMatSmaller[90+i*5:95+i*5,3]), np.mean(accMatSmaller[120+i*5:125+i*5,4])])


#print accMatSmaller.shape
#print accMatSmaller[0+i*5:5+i*5,0]




