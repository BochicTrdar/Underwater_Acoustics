#==================================================================
#  
#  Van der Pol system of equations and calculating the 
#  associated Poincare Map
#  Faro, Seg 11 Abr 2022 22:34:07 WEST 
#  Written by Tordar 
#  
#==================================================================

# Reference: 
# Analytical and Numerical Study of the
# Poincare Map with Applications on the
# Computation of Periodic Orbits

from scipy import integrate
from numpy import *
from matplotlib.pyplot import *

rcParams.update({"text.usetex": True})

def solver(x,t):
    e = 0.1
    x1 = x[0]
    x2 = x[1]
    dx1 = x2
    dx2 = e*( 1.0 - x1*x1 )*x2 - x1
    return [dx1,dx2]

tmax = 100.0
dt = 0.01
t = arange(0,tmax+dt,dt)

np = 101
yp = zeros(np)

x0 = array([0.0, 0.2])
x = integrate.odeint(solver, x0, t)
x1 = x[:,0]
x2 = x[:,1]
figure(1)    
dx = x1 # Section of the Poincare map
ds = abs( diff( sign( dx ) ) )/2
j = where( ds > 0 )[0]
l = j.size
yp[0:l] = x2[j]
plot(x1[j],x2[j],'bo')
plot(x1,x2)
xlabel(r'$x(t)$',fontsize=18)
ylabel(r'$y(t)$',fontsize=18)
title('Van der Pol system')
grid(True)

yp = sort( yp[0:l] )

figure(2)
plot(yp[0:-1],yp[1:],'o')
title('Poincare map')
grid(True)

show()

print('done.')
