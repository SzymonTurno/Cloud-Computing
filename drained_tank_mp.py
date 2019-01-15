import numpy as np
import multiprocessing as mp
from datetime import datetime

dt = 0.5 # hr
tf = 10.0 # hr
tp = 0
	
def hCalc(c,qin,queue,output):
	global dt
	global tf
	global tp
	Ac = 2 # m^2
	nsteps = int(tf/dt)
	hs = np.empty(nsteps)
	h = 0
	hmax = 1
	i = 0
	while abs(tf - tp) > 0.1*dt:
		hs[i] = h
		q = c*pow(h,0.5)
		i = i + 1
		if qin == 0:
			qs = queue.get()
			
		else:
			queue.put(q)
			qs = qin
			
		h = (qs - q)*dt/Ac + h
		if h>hmax:
			h = 1
		tp = tp + dt
	output.put((c,hs))
	
def tCalc(c,queue):
	global dt
	global tf
	global tp
	nsteps = int(tf/dt)
	ts = np.empty(nsteps)
	i = 0
	while abs(tf - tp) > 0.1*dt:
		ts[i] = tp
		i = i + 1
		tp = tp + dt
	queue.put((c,ts))

c1 = 0.13
c2 = 0.2

queueIn = mp.Queue()
queueOut = mp.Queue()

p1 = mp.Process(target = tCalc, args = (0,queueOut))
p2 = mp.Process(target = hCalc, args = (c1,0.5,queueIn,queueOut))
p3 = mp.Process(target = hCalc, args = (c2,0,queueIn,queueOut))
	
starttime = datetime.now()

p1.start()
p2.start()
p3.start()

p1.join()
p2.join()
p3.join()
	
calctime = (datetime.now() - starttime).microseconds
print("Time taken: " + str(calctime) + "us.")

r = queueOut.get()
if r[0] == c1:
	h1s = r[1]
if r[0] == c2:
	h2s = r[1]
if r[0] == 0:
	ts = r[1]
	
r = queueOut.get()
if r[0] == c1:
	h1s = r[1]
if r[0] == c2:
	h2s = r[1]
if r[0] == 0:
	ts = r[1]
	
r = queueOut.get()
if r[0] == c1:
	h1s = r[1]
if r[0] == c2:
	h2s = r[1]
if r[0] == 0:
	ts = r[1]

print("First tank height array: " + str(h1s))
print("Second tank height array: " + str(h2s))
