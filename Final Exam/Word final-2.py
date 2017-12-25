import numpy as np
from pylab import *
from math import *
import mpl_toolkits.mplot3d

L=2
M=0.1
E=8

x0=5
x=[]
x.append(x0)
y0=0
o0=0
y=[]
o=[]
y.append(y0)
o.append(o0)    
u=[]
u.append(M/sqrt(x0**2+y0**2))
w=[]
w0=(E**2-L**2*u[0]**2*(1-2*u[0])/M**2)**0.5/L
w.append(w0)
tot_o=5*pi
do=0.001

for i in range(int(tot_o/do)):
    w.append(w[i]+(3*u[i]**2-u[i]+(M/L)**2)*do)
    u.append(u[i]+w[i+1]*do)
    o.append(o[i]+do)
    x.append((M/u[i])*cos(o[i]))
    y.append((M/u[i])*sin(o[i]))

plot(y,x,color='blue',linestyle='-')
show()
