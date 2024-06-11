# Converted to Python from Matlab code in: 
# https://gorbatschow.github.io/SonarDocs/sound_speed_sea_mackenzie.en/
# Sound speed in sea
from numpy import * 

def sound_speed_sea_mackenzie(T=None,S=None,D=None):

# Inputs
#   T: temperature \ degree Celsius \ -2 < T < 30 
#   S: salinity \ ppt \ 25 < S < 40
#   D: depth \ m \ 0 < D < 8000
# Outputs
#   C: speed of sound in seawater \ m/s

    S = S - 35 
    
    C = 1448.96 + 4.591*T - 5.304e-2*( T**2 ) + 2.374e-4*( T**3 ) \
      + 1.340*S + 1.630e-2*D + 1.675e-7*( D**2 ) \
      - 1.025e-2*T*S - 7.139e-13*T*( D**3 )

return C
