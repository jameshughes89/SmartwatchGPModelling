#finds the top models for each subject
#must copy the stuf over

import numpy as np
import csv
import sys
from math import *

def func_0(v0,v1,v2,v3,v4,v5,v6,v7,v8): return  ( ( ( ( v1 + v6 ) - ( v4 -sin( v5 )) ) /tan( 1.8504810057939345 )) + (cos( v4 )*tan(sin(sin( (sin( v5 )* ( v5 + 1.8504810057939345 ) ) )))) ) 
def func_1(v0,v1,v2,v3,v4,v5,v6,v7,v8): return  (sin(sin( ( ( ( v7 + v2 ) - ( ( v4 - ( v1 - v4 ) ) *sin( v0 )) ) / ( v0 - -4.203150267534678 ) ) ))- ( ( ( v4 - ( v1 - v4 ) ) - v4 ) / -2.6602661702920116 ) ) 
def func_2(v0,v1,v2,v3,v4,v5,v6,v7,v8): return  ( ( v2 / (abs( v1 )+ ( 5.431387860540262 - v7 ) ) ) + ( ( v4 / (tan( ( ( v0 + 6.669520298108061 ) / 5.431387860540262 ) )-cos( v4 )) ) + ( (cos( ( v1 + v1 ) )- (cos( ( 5.431387860540262 - v7 ) )+ ( v1 + v1 ) ) ) / (abs( v1 )+ ( 5.431387860540262 - v7 ) ) ) ) ) 
def func_3(v0,v1,v2,v3,v4,v5,v6,v7,v8): return  ( ( ( v4 + v2 ) / ( (abs( ( v4 + v2 ) )+ v0 ) +tan( 7.490391518278674 )) ) - ( ( v1 - ( v4 + v2 ) ) / ( (abs( ( v4 + v2 ) )+ v0 ) +tan( 7.490391518278674 )) ) ) 
def func_4(v0,v1,v2,v3,v4,v5,v6,v7,v8): return  ( (sin( ( v4 + v2 ) )* ( ( (cos( -3.6132910443136126 )+ v0 ) / ( v1 + ( -3.6132910443136126 +cos( ( v4 + v2 ) )) ) ) + ( ( (cos( -3.6132910443136126 )+ v0 ) / ( v1 + ( -3.6132910443136126 +cos( ( v4 + v2 ) )) ) ) *tan( (cos(tan(sin( ( v4 + v2 ) )))*cos(sin( 17.42668862701946 ))) )) ) ) + ( ( v1 - ( v4 + v2 ) ) / -3.6132910443136126 ) ) 
def func_5(v0,v1,v2,v3,v4,v5,v6,v7,v8): return  ( ( ( ( ( v1 - v0 ) / 2.3465946407954554 ) *abs( ( ( v0 * ( v1 / 2.9205598361867935 ) ) -sin( (sin( v6 )+sin( v6 )) )) )) -sin(sin( ( v7 +sin( v6 )) ))) + ( v7 * ( v1 / 2.9205598361867935 ) ) ) 
def func_6(v0,v1,v2,v3,v4,v5,v6,v7,v8): return  (sin( ( ( ( v1 -sin( v7 )) + ( v0 * (sin( ( v6 + 12.655846379890676 ) )- 0.3983841389268221 ) ) ) * ( 0.3983841389268221 + ( v6 / ( ( 12.655846379890676 / v1 ) / v1 ) ) ) ) )-sin(sin( ( v6 + 12.655846379890676 ) ))) 
def func_7(v0,v1,v2,v3,v4,v5,v6,v7,v8): return  ( ( v1 / 2.863098785192708 ) - (sin( (sin(sin( v6 ))- ( ( v1 / 2.863098785192708 ) *sin( v6 )) ) )- ( ( ( ( v1 / 2.863098785192708 ) *sin( v6 )) * ( v0 / v1 ) ) - ( ( 2.863098785192708 *sin(sin( v6 ))) / ( (tan( ( -5.00536157179187 - ( ( ( v1 / 2.863098785192708 ) *sin( v6 )) * ( v0 / v1 ) ) ) )+tan( ( -5.00536157179187 - ( ( ( v1 / 2.863098785192708 ) *sin( v6 )) * ( v0 / v1 ) ) ) )) + ( v6 * ( 2.863098785192708 *sin(sin( v6 ))) ) ) ) ) ) ) 
def func_8(v0,v1,v2,v3,v4,v5,v6,v7,v8): return  ( ( ( ( 4.1900812079932805 - v1 ) - ( ( ( -8.976809665862259 - v0 ) - ( v0 * (sin( ( ( v6 + v6 ) -abs( v1 )) )+sin( ( ( v6 + v6 ) -abs( v1 )) )) ) ) + ( ( v6 + v6 ) * v7 ) ) ) / ( ( 4.1900812079932805 + v0 ) / ( v7 + ( ( v6 + v6 ) - v1 ) ) ) ) / ( -8.976809665862259 - v0 ) ) 
def func_9(v0,v1,v2,v3,v4,v5,v6,v7,v8): return  ( ( ( v1 *tan( 6.6644675175892445 )) - v6 ) + ( ( ( v0 * (sin( v6 )*tan( 6.6644675175892445 )) ) + (tan(sin( ( ( v6 -tan( 6.6644675175892445 )) * ( v7 - ( v0 * (sin( v6 )*tan( 6.6644675175892445 )) ) ) ) ))/ 6.6644675175892445 ) ) + ( ( ( ( v1 *tan( 6.6644675175892445 )) - ( ( v0 * (sin( v6 )*tan( 6.6644675175892445 )) ) +cos( v6 )) ) + ( ( v6 -tan( 6.6644675175892445 )) /sin( v7 )) ) * (tan( 6.6644675175892445 )*sin( v7 )) ) ) ) 
def func_10(v0,v1,v2,v3,v4,v5,v6,v7,v8): return  ( ( ( 3.1750159454578366 *sin( v6 )) + ( ( v0 * ( ( 3.1750159454578366 *sin( v6 )) / ( -4.190035816863546 - v6 ) ) ) - ( v1 - ( ( 3.1750159454578366 *sin( v6 )) / ( -4.190035816863546 - v6 ) ) ) ) ) / ( (cos( ( ( 3.1750159454578366 *sin( v6 )) / ( -4.190035816863546 - v6 ) ) )- ( ( v1 - ( ( 3.1750159454578366 *sin( v6 )) / ( -4.190035816863546 - v6 ) ) ) /abs( 2.0726680872802774 )) ) - 3.1750159454578366 ) ) 
def func_11(v0,v1,v2,v3,v4,v5,v6,v7,v8): return  (sin( ( -3.2235628178954343 -sin( v6 )) )* ( ( (sin( v6 )* v2 ) / -3.2235628178954343 ) + ( ( ( v0 + -3.2235628178954343 ) + ( ( v1 /sin( ( -3.2235628178954343 -sin( v6 )) )) +sin( ( -3.2235628178954343 -sin( v6 )) )) ) / ( ( ( v6 -sin( v1 )) / ( v0 + -3.2235628178954343 ) ) - -2.687088358855469 ) ) ) ) 
def func_12(v0,v1,v2,v3,v4,v5,v6,v7,v8): return  ( ( ( v1 * 0.3622396443746112 ) - (cos( ( v0 +abs( (cos( -11.719157974605249 )-sin( v6 )) )) )* (sin(sin( v6 ))*cos( v1 )) ) ) -sin(sin( v6 ))) 
def func_13(v0,v1,v2,v3,v4,v5,v6,v7,v8): return  (tan( ( ( v0 + -4.476669888947139 ) / -10.322815711620162 ) )* ( ( v1 - v6 ) -sin( ( v6 +sin( v7 )) )) ) 
def func_14(v0,v1,v2,v3,v4,v5,v6,v7,v8): return  ( ( v1 / 2.701144267951328 ) - (cos( (sin(cos( v1 ))- ( v0 / ( -2.4784373320980606 -sin( v0 )) ) ) )/ (cos(sin( v0 ))/sin( v6 )) ) ) 
def func_15(v0,v1,v2,v3,v4,v5,v6,v7,v8): return  ( ( ( ( v2 +cos(cos( ( v1 + -4.131177280618331 ) ))) - (sin( v7 )+ v4 ) ) / -4.131177280618331 ) +sin( (sin( ( v1 + -4.131177280618331 ) )- v6 ) )) 
def func_16(v0,v1,v2,v3,v4,v5,v6,v7,v8): return  ( ( ( ( v6 + v6 ) - v4 ) +sin( ( ( v6 + v6 ) - v4 ) )) / ( ( -7.628931960864648 -sin( ( ( ( v6 + v6 ) - v4 ) + v6 ) )) / ( (sin( v1 )/ ( ( v6 + v6 ) - v4 ) ) + ( 1.9681772159163735 - v0 ) ) ) ) 
def func_17(v0,v1,v2,v3,v4,v5,v6,v7,v8): return  (sin( ( ( v6 + (abs( v6 )*sin( v4 )) ) -sin( v4 )) )*tan( ( ( ( 8.074523888333232 - v0 ) / -5.632436963116367 ) + -5.632436963116367 ) )) 
def func_18(v0,v1,v2,v3,v4,v5,v6,v7,v8): return  (sin( ( ( ( ( v7 - v6 ) * -0.31373949059558726 ) -sin( v4 )) + ( -0.31373949059558726 * v0 ) ) )* ( -1.0532476626581158 +sin(sin( v0 ))) ) 
def func_19(v0,v1,v2,v3,v4,v5,v6,v7,v8): return tan( ( (sin( ( ( v0 + v0 ) / -7.1896111663037345 ) )+ 10.049279887365334 ) * ( ( ( v4 - ( ( v0 + v0 ) / -7.1896111663037345 ) ) - v6 ) /abs( ( ( v4 - ( ( v0 + v0 ) / -7.1896111663037345 ) ) - v6 ) )) ) )
def func_20(v0,v1,v2,v3,v4,v5,v6,v7,v8): return  (sin( ( ( ( ( v6 / ( -5.16104826506707 - v1 ) ) / ( ( -3.501298981088926 +cos( -3.501298981088926 )) / ( -5.16104826506707 + v0 ) ) ) + (cos( ( ( v6 / ( -5.16104826506707 - v1 ) ) * -3.501298981088926 ) )* v7 ) ) +sin( ( ( v6 - v1 ) / -5.16104826506707 ) )) )/ ( ( -3.501298981088926 +cos( -3.501298981088926 )) / ( -5.16104826506707 + v0 ) ) ) 
def func_21(v0,v1,v2,v3,v4,v5,v6,v7,v8): return  ( ( ( ( v6 +abs( v1 )) -sin( ( ( ( v0 / -3.6716614095776805 ) + -3.6716614095776805 ) + v6 ) )) / ( ( v0 / -3.6716614095776805 ) + -3.6716614095776805 ) ) - ( ( ( (sin( v7 )* ( ( v6 +abs( v1 )) -sin( ( ( ( v0 / -3.6716614095776805 ) + -3.6716614095776805 ) + v6 ) )) ) - -3.6716614095776805 ) *sin( v7 )) / (cos( v1 )+ ( ( v0 / -3.6716614095776805 ) + -3.6716614095776805 ) ) ) ) 
def func_22(v0,v1,v2,v3,v4,v5,v6,v7,v8): return  ( ( ( ( ( v7 *abs(cos( v0 ))) / (abs( v7 )+ ( v7 / -4.551118208455547 ) ) ) *sin( v1 )) + ( ( ( v2 *abs(cos( v0 ))) / (abs( v7 )+ ( v7 / -4.551118208455547 ) ) ) + ( ( ( v7 / -4.551118208455547 ) + ( -4.551118208455547 + (abs( v7 )+ ( v7 / -4.551118208455547 ) ) ) ) + ( ( ( v0 - ( -4.551118208455547 / ( -4.551118208455547 + -4.551118208455547 ) ) ) -cos(abs( v7 ))) / (abs( v7 )- ( v7 / -4.551118208455547 ) ) ) ) ) ) * ( v7 / -4.551118208455547 ) ) 
def func_23(v0,v1,v2,v3,v4,v5,v6,v7,v8): return  (sin( ( ( (cos( v6 )* v7 ) - (sin(cos( -4.860918630807895 ))+ ( v6 / 7.511775221408161 ) ) ) - (cos( ( v2 / ( v6 + v6 ) ) )* ( ( v6 + v6 ) / ( v0 - -4.860918630807895 ) ) ) ) )/ ( (sin(cos( -4.860918630807895 ))* ( v0 - -4.860918630807895 ) ) +sin(cos( -4.860918630807895 ))) ) 
def func_24(v0,v1,v2,v3,v4,v5,v6,v7,v8): return  ( ( ( v6 + v7 ) / -2.8454214051830142 ) + ( ( ( ( ( ( v7 * v6 ) * v6 ) - ( v4 *cos( v7 )) ) - ( (cos( v7 )* ( v7 - v2 ) ) + v7 ) ) / ( -6.6791017639879335 + ( v7 * v6 ) ) ) + v7 ) ) 

funcs = [func_0,func_1,func_2,func_3,func_4,func_5,func_6,func_7,func_8,func_9,func_10,func_11,func_12,func_13,func_14,func_15,func_16,func_17,func_18,func_19,func_20,func_21,func_22,func_23,func_24]


tasks = ['Down', 'Jogging', 'Running', 'Up', 'Walking']
subjects = [1,2,3,4,5,6]
takes = [1,2,3,4,5]

accMat = []

count = 0

GROUP_SIZE = 50

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


			#count = 0
			accRow = np.zeros(len(funcs))
			#for i in range(0,data.shape[0], GROUP_SIZE):
			for i in range(100):
				abEs = []
				#count+=1
				#for l in data[i:i+GROUP_SIZE]:
				np.random.shuffle(data)
				for l in data[:GROUP_SIZE]:
					abE = []
					for f in funcs:
						try:
							err = l[8] - f(l[0],l[1],l[2],l[3],l[4],l[5],l[6],l[7],l[8])
						except (ValueError, OverflowError, ZeroDivisionError):
							#err = float('nan')
							sys.float_info.max
						abE.append(abs(err))
					abEs.append(abE)
			
				#accRow[np.argmin(np.mean(abEs,axis=0))] += (1./(float(data.shape[0])/float(GROUP_SIZE)))
				accRow[np.argmin(np.mean(abEs,axis=0))] += (1.)
			accRow = accRow/float(100)
			accMat.append(accRow)


np.savetxt('accMat_aggr.csv', accMat, delimiter=",")



