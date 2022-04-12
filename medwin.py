from numpy import *
def medwin( z , T , S ):

# MEDWIN: Converts Depth, Temperature and Salinity to Sound Velocity in Sea Water
# through Medwin's formula. Range of validity: temperature 0 to 35 Celsius degrees, 
# salinity 0 to 45 parts per thousand and depth 0 to 1000 m.
#
# Reference:
# Medwin H., "Speed of Sound in Water for Realistic Parameters", 
# J. Acoust. Soc. Am. 58(1318), 1975.

#***************************************************************************************
# Don't like it? Don't use it...
#***************************************************************************************
    
    c = []
 
    c = 1449.2 + 4.6*T - 5.5e-2*T*T + 2.9e-4*T*T*T + ( 1.34 - 1e-2*T ).*( S - 35 ) + 1.6e-2*z

    return c 
