# Converted to Python from Matlab code in: 
# https://gorbatschow.github.io/SonarDocs/depth_to_pressure_sea_leroy_68.en/
# Depth and pressure relationship

from numpy import * 

def depth_to_pressure_sea_leroy_68(D=None,L=None):
# Inputs
#   D: depth \ m
#   L: latitude \ degree \ -90 < L < 90
# Outputs
#   P: pressure \ kPa
    Lr = deg2rad( L )
    P = 0.102506*( 1 + 5.28e-3*sin( Lr )**2 )*D + 2.54e-7*D**2
    P = P*9.80665e1

return P
