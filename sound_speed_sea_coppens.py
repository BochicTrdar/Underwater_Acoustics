# Converted to Python from Matlab code in: 
# https://gorbatschow.github.io/SonarDocs/sound_speed_sea_coppens.en/
# Sound speed in sea
from numpy import * 

def sound_speed_sea_coppens(T=None,S=None,D=None):

# Inputs
#   T: temperature \ degree Celsius \ -2 < T < 35 
#   S: salinity \ ppt \ 0 < S < 42
#   D: depth \ m \ 0 < D < 4000
# Outputs
#   C: speed of sound in seawater \ m/s

    d = D*1e-3
    t = T*1e-1
    S = S - 35
    tt  = t*t
    ttt = tt*t
    
    C = 1449.05 + 45.7*t - 5.21*tt + 0.23*ttt      \
      + (1.333 - 0.126*t + 0.009*tt)*S             \
      + (16.23 + 0.253*t)*d + (0.213-0.1*t)*(d**2) \
      + (0.016 + 0.0002*S)*S*t*d

return C
