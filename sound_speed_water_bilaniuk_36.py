# Converted to Python from Matlab code in: 
# https://gorbatschow.github.io/SonarDocs/sound_speed_water_bilaniuk_36.en
# Sound speed in pure water

from numpy import * 

def sound_speed_water_bilaniuk_36(T=None):

# Inputs
#    T: temperature \ degree Celsius \ 0 < T < 100
# Outputs
#    C: speed of sound in pure water \ m/s

    k0 =  1.40238677e+3 
    k1 =  5.03798765e+0 
    k2 = -5.80980033e-2 
    k3 =  3.34296650e-4 
    k4 = -1.47936902e-6 
    k5 =  3.14893508e-9 

    C = k0 + k1*T + k2*(T**2) + k3*(T**3) + k4*(T**4) + k5*(T**5)

return C
