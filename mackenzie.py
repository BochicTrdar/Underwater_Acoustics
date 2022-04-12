from numpy import *
def mackenzie( z=None, T=None, S=None ):

#MACKENZIE: Converts Depth, Temperature and Salinity to Sound Velocity in Sea Water 
#through Mackenzie's formula. 
#
# Usage:    sound_speed_in_sea_water = mackenzie( depths , temperature , salinity ) ; 
#         
#           When applied to a vector 'mackenzie' returns a vector,  
#           when applied to a matrix 'mackenzie' returns a matrix 
#           after operating on every column. 
#           Range of validity: temperature 2 to 30 Celsius degrees, 
#           salinity 25 to 40 parts per thousand and depth 0 to 8000 m.
 
#***************************************************************************************
# 
# Reference: K.V. Mackenzie, "Nine-term equation for the sound speed in the oceans",  
#            J. Acoust. Soc. Am. 70(3), pp 807-812, 1981.
#
#***************************************************************************************

#***************************************************************************************
# Don't like it? Don't use it...
#***************************************************************************************
    c = []
    S = S - 35.0
    c = 1448.96 + 4.591*T - 5.304e-2*T*T + 2.374e-4*T*T*T + 1.340*S + 1.630e-2*z + 1.675e-7*z*z - 1.025e-2*T*S - 7.139e-13*T*z*z*z 
    return c
