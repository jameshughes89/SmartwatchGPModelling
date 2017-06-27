import csv
from math import *
import numpy as np
import scipy
import scipy.special
import matplotlib.pyplot as plt
import scipy.io
import scipy.signal
import sklearn
import sklearn.preprocessing


from scipy.signal import butter, lfilter, freqz

#tasks = ['Jogging', 'Running']
#subjects = [1,2]
#takes = [1,2]

tasks = ['Down']
subjects = [1]
takes = [1]
	
for tsk in tasks:
	for sub in subjects:
		for tke in takes:
			iFile = csv.reader(open(tsk + '_' + str(sub) + '_' + str(tke) + '.csv','r'))

			v0 = []
			v1 = []
			v2 = []
			v3 = []
			v4 = []
			v5 = []
			v6 = []
			v7 = []
			v8 = []


			for l in iFile:
				try:
					v0.append(float(l[0]))
					v1.append(float(l[1]))
					v2.append(float(l[2]))
					v3.append(float(l[3]))
					v4.append(float(l[4]))
					v5.append(float(l[5]))
					v6.append(float(l[6]))
					v7.append(float(l[7]))
					v8.append(float(l[8]))
				except ValueError:
					print "burp!"					
					continue
			



			plt.plot(v0)


			plt.show()
			
			#DOWN SAMPLE SIGNALS
			v0 = scipy.signal.decimate(v0,4)
			v1 = scipy.signal.decimate(v1,4)
			v2 = scipy.signal.decimate(v2,4)
			v3 = scipy.signal.decimate(v3,4)
			v4 = scipy.signal.decimate(v4,4)
			v5 = scipy.signal.decimate(v5,4)
			v6 = scipy.signal.decimate(v6,4)
			v7 = scipy.signal.decimate(v7,4)
			v8 = scipy.signal.decimate(v8,4)


			v0 = v0[200:-200]
			v1 = v1[200:-200]
			v2 = v2[200:-200]
			v3 = v3[200:-200]
			v4 = v4[200:-200]
			v5 = v5[200:-200]
			v6 = v6[200:-200]
			v7 = v7[200:-200]
			v8 = v8[200:-200]


			plt.plot(v0)


			plt.show()
			
			#v0 = scipy.stats.mstats.zscore(v0)
			#v1 = scipy.stats.mstats.zscore(v1)
			#v2 = scipy.stats.mstats.zscore(v2)
			#v3 = scipy.stats.mstats.zscore(v3)
			#v4 = scipy.stats.mstats.zscore(v4)
			#v5 = scipy.stats.mstats.zscore(v5)
			#v6 = scipy.stats.mstats.zscore(v6)
			#v7 = scipy.stats.mstats.zscore(v7)
			#v8 = scipy.stats.mstats.zscore(v8)
				


'''
Xs = range(len(v0))



# Filter requirements.
order = 4
fs = 50.0   
    # sample rate, Hz (VERIFY THIS)
cutoff = 5.0  # desired cutoff frequency of the filter, Hz (could probbaly be >2)

# Get the filter coefficients so we can check its frequency response.
b, a = butter_lowpass(cutoff, fs, order)

# Plot the frequency response.
#w, h = freqz(b, a, worN=8000)
#plt.subplot(2, 1, 1)
#plt.plot(0.5*fs*w/np.pi, np.abs(h), 'b')
#plt.plot(cutoff, 0.5*np.sqrt(2), 'ko')
#plt.axvline(cutoff, color='k')
#plt.xlim(0, 0.5*fs)
#plt.title("Lowpass Filter Frequency Response")
#plt.xlabel('Frequency [Hz]')
#plt.grid()

#plt.show()

#plt.clf()
#y = butter_lowpass_filter(v0, cutoff, fs, order)
#plt.plot(Xs, v0)
#plt.plot(Xs, y)
#plt.show()

v0 = butter_lowpass_filter(v0, cutoff, fs, order)
v1 = butter_lowpass_filter(v1, cutoff, fs, order)
v2 = butter_lowpass_filter(v2, cutoff, fs, order)


#NORMALIZZZING
#thing = np.array([v0,v1,v2])
#thing = sklearn.preprocessing.normalize(thing)
#v0 = thing[0]
#v1 = thing[1]
#v2 = thing[2]
v0 = scipy.stats.mstats.zscore(v0)
v1 = scipy.stats.mstats.zscore(v1)
v2 = scipy.stats.mstats.zscore(v2)

plt.clf()
#PLOT STUFF
plt.plot(Xs[:],v0[:],color='b')
plt.plot(Xs[:],v1[:],color='g')
plt.plot(Xs[:],v2[:],color='r')

#plt.show()

print len(v0)
plt.show()
'''



