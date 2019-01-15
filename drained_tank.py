import numpy as np
from datetime import datetime

def tank(c1,c2):
        Ac = 2 # m^2
        qin = 0.5 # m^3/hr
        dt = 0.5 # hr
        tf = 10.0 # hr

        nsteps = int(tf/dt)
        hmax = 1

        h1 = 0
        h2 = 0
        t = 0
        ts = np.empty(nsteps)
        h1s = np.empty(nsteps)
        h2s = np.empty(nsteps)
        i = 0

        starttime = datetime.now()

        while abs(tf - t) > 0.1*dt:
                ts[i] = t
                h1s[i] = h1
                h2s[i] = h2

                qout1 = c1 * pow(h1,0.5)
                qout2 = c2 * pow(h2,0.5)
                h1 = (qin - qout1)*dt/Ac + h1
                if h1>hmax:
                        h1 = 1
                h2 = (qout1 - qout2)*dt/Ac + h2
                if h2>hmax:
                        h2 = 1
                i = i + 1
                t = t + dt

        calctime = (datetime.now() - starttime).microseconds

        print("Time taken: " + str(calctime) + "us.")
        print("First tank height array: " + str(h1s))
        print("Second tank height array: " + str(h2s))

# call function
tank(0.13,0.20)
