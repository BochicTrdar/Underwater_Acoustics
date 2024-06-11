# Converted to Python from Matlab code in: 
# https://gorbatschow.github.io/SonarDocs/sound_speed_water_lubbers_c1.en
# Sound speed in pure water

from numpy import *

def sound_speed_water_lubbers_c1(T=None):
# Inputs
#    T: temperature \ degree Celsius \ 10 < T < 40
# Outputs
#    C: speed of sound in pure water \ m/s

    C = 1405.03 + 4.624*T - 3.83e-2*(T**2)

return C
