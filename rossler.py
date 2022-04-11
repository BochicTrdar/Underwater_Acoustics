#==================================================================
#  
#  Solving a differential system of equations and calculating the 
#  associated Poincare Map
#  Faro, Seg 11 Abr 2022 22:29:38 WEST 
#  Written by Tordar 
#  
#==================================================================

from scipy import integrate
from numpy import *
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import Axes3D

rcParams.update({"text.usetex": True})

x0 = array([1.0, 1.0, 0.0])

#==================================================================
#  
#  Define derivatives:
#  
#==================================================================

# Can't figure out how to pass a, b and c to the solver... 

def solver(x,t):
    c = 1.0
    a = 0.2
    b = 0.2
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    dx1 = -x2 - x3 
    dx2 =  x1 + x2*a 
    dx3 =  x3*( x1 - c ) + b    
    return [dx1,dx2,dx3]

t = arange(0,5000.0+0.1,0.1)
x = integrate.odeint(solver, x0, t)

x1 = x[:,0]
x2 = x[:,1]
x3 = x[:,2]

n = t.size
p = 0.5
RES = 500
np = array([n*p])
indexes = arange(0,np.astype(int),RES)

fig = figure(1)
ax = fig.add_subplot(111, projection="3d")
plot(x1,x2,x3)
ax.set_xlabel(r'$x(t)$',fontsize=18)
ax.set_ylabel(r'$y(t)$',fontsize=18)
ax.set_zlabel(r'$z(t)$',fontsize=18)
title('Rossler system')
grid(True)

figure(2)
plot(x1[indexes],x3[indexes],'r*')
xlabel(r'$x(t)$',fontsize=18)
ylabel(r'$z(t)$',fontsize=18)
title('Poincare map of $(x,z)$')
grid(True)

show()

print('done.')
