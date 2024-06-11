# Converted to Python from Matlab code in: 
# https://gorbatschow.github.io/SonarDocs/pressure_to_depth_sea_bisset.en/
# Depth and pressure relationship

from numpy import * 

def pressure_to_depth_sea_bisset(P=None,L=None):

# Inputs
#   P: pressure \ kPa
#   L: latitude \ degree \ -90 < L < 90
# Outputs
#   D: depth \ m
    
    Lr = deg2rad( L )
    P = P*0.0102
    D = 9.7512*P/( 1 + 5.3e-3*sin( Lr )**2 ) - 2.07e-4*P**2

return D
