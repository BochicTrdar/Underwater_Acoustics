from numpy import * 
from matplotlib.pyplot import *
from chenmillero import *

data = loadtxt('chenmillero_data.txt')

P = data[:,0]
S = data[:,1]
T = data[:,2]
cref = data[:,3]
c = chenmillero(P, T, S)

abs_error = abs( c - cref )

figure()
plot(abs_error)
grid(True)
show()


