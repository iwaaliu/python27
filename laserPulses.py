#!/usr/bin/env python
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

def Sin2(E0,omega,phi,T0,ts,t):
   # ts: pulse starting point
   # E0: field strength
   # phi: phase
   # T0: pulse width
   # omega: frequency
    if abs(t-ts-T0/2)<T0/2:
        Et=E0*np.cos(omega*(t-ts)+phi)*np.sin(np.pi*(t-ts)/T0)**2
    else:
        Et=0.0
    return Et

def Gaussian(E0,omega,phi,sigma,t0,t):
   # t0: pulse center
   # E0: field strength
   # phi: phase
   # sigma pulse width
   # omega: frequency
    Et = E0*np.cos(omega*t+phi)*np.exp(-(t-t0)**2/sigma/sigma)
    return Et

def Cos2(E0,omega,phi,T0,ts,t):
   # ts: pulse starting point
   # E0: field strength
   # phi: phase
   # T0: pulse width
   # omega: frequency
    if abs(t-ts)<T0/2:
        Et=E0*np.cos(omega*(t-ts)+phi)*np.cos(np.pi*(t-ts)/T0)**2
    else:
        Et=0.0
    return Et


dt = 0.01
E0 = 0.01
omega = 1.58/27.21
n=1
T0 = n*2*np.pi/omega; print T0/n
sigma =  100
phi = 1.0*np.pi/2
N = int(400/dt)
Et = np.zeros(N)
xt = np.zeros(N)

for i in xrange(0, N):
    t = dt*(i-N/2*1)
    xt[i] = t
    Et[i] += Sin2(E0,omega,phi,T0,0,t)
    Et[i] += Gaussian(E0,omega,phi,T0/4,0.0,t)
    Et[i] += Cos2(E0,omega,phi,T0,T0/2,t)
plt.plot(xt,Et)
plt.show()
