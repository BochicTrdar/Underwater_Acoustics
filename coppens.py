from numpy import *
def coppens( z=None, T=None, S=None ):

#COPPENS: Converts Depth, Temperature and Salinity to Sound Velocity in Sea Water
#through Coppens's formula. 
#
#Full reference:  
#A.B. Coppens, "Simple equations for the speed of sound in Neptunian waters",  
#J. Acoust. Soc. Am. 69(3), pp 862-863, 1981.
#
#
# Usage:    sound_speed_in_sea_water = coppens( depths , temperature , salinity ) ; 
#         
#           When applied to a vector 'coppens' returns a vector,  
#           when applied to a matrix 'coppens' returns a matrix 
#           after operating on every column. 
#           Range of validity: temperature 2 to 30 Celsius degrees, 
#           salinity 25 to 40 parts per thousand and depth 0 to 8000 m.

#***************************************************************************************
# Faro, Ter 12 Abr 2022 21:33:24 WEST 
# Written by Tordar
#***************************************************************************************

#***************************************************************************************
# Don't like it? Don't use it...
#***************************************************************************************
    c = []

    S   = S - 35
    T   = T/10
    TT  = T**2
    TTT = T**3
    z   = z/1000
    zz  = z**2
 
    c0 = 1449.05 + 45.7*T - 5.21*TT + 0.23*TTT + ( 1.333 - 0.126*T + 0.009*TT )*S 
   
    c  = c0 + (16.23 + 0.253*T)*z + (0.213 - 0.1*T)*zz + ( 0.016 + 0.0002*S )*S*T*z  
                         
    return c

