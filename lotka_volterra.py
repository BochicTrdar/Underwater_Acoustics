#==================================================================
#  
#  Lotka Volterra system of differential equations and 
#  associated Poincare Map
#  Faro, Seg 11 Abr 2022 22:25:48 WEST 
#  Written by Tordar 
#  
#==================================================================

# Reference: 
# Juan Carlos Albahaca
# Analytical and Numerical Study of the
# Poincare Map with Applications on the
# Computation of Periodic Orbits

from scipy import integrate
from numpy import *
from matplotlib.pyplot import *

rcParams.update({"text.usetex": True})

nx = 101
xi = linspace(0.5,1.5,nx)

def solver(x,t): 
    a = 0.4
    b = 0.1 
    r = 0.3
    c = 0.5
    x1 = x[0]
    x2 = x[1]
    dx1 =  a*x1 - b*x1*x2
    dx2 = -r*x2 + c*x1*x2
    return [dx1,dx2]

tmax = 100.0
dt = 0.02
t = arange(0,tmax+dt,dt)

np = 101
yp = zeros(np)
k = 0

for i in range(nx):
    x0 = array([xi[i], 3.0])
    x = integrate.odeint(solver, x0, t)
    x1 = x[:,0]
    x2 = x[:,1]
    dx = x1 - 1.0 # Section of the Poincare map
    ds = abs( diff( sign( dx ) ) )/2
    j = where( ds > 0 )[0]
    l = j.size
    figure(1)
    plot(x1,x2)
    if l > 2:
       j = j[0:2]
       yp[k] = x2[j[0]]
       k = k + 1
       plot(x1[j],x2[j],'bo')
xlabel(r'$x(t)$',fontsize=18)
ylabel(r'$y(t)$',fontsize=18)
title('Lotka-Volterra system')
grid(True)

yp = sort( yp[0:k] )

figure(2)
plot(yp[0:-1],yp[1:],'o')
title('Poincare map')
grid(True)

show()

print('done.')
