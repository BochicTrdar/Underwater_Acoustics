from numpy import *
def delgrosso( P=None, T=None, S=None ):

#DELGROSSO: Converts Pressure, Temperature and Salinity to Sound Velocity in Sea Water
#through Del Grosso's formula. 
#
#Full reference: 
#V.A. Del Grosso, "New equation for the speed of sound in natural waters (with comparisons to other equations)",   
#J. Acoust. Soc. Am 56(4), pp 1084-1091, 1974.
#
# Faro, Ter 12 Abr 2022 21:16:14 WEST  
# Written by TORDAR 
#
# SYNOPSIS: sound_speed_in_sea_water = delgrosso( pressure , temperature , salinity )
#
#           where T = temperature in degrees Celsius
#                 S = salinity in Practical Salinity Units and 
#                 P = pressure in kg/cm2. 
#
#           Range of validity: temperature 0 to 30 Celsius degrees, 
#           salinity 30 to 40 parts per thousand and pressure 0 to 1000 kg/cm2, 
#           where 100 kPa = 1.019716 kg/cm2.

# Don't like it? Don't use it... 

    c = []

    c000  =  1402.392
    cT1   =  0.5012285e1  ; cT2 = -0.551184e-1  ; cT3 =  0.221649e-3 
    cS1   =  0.1329530e1  ; cS2 =  0.1288598e-3
    cP1   =  0.1560592    ; cP2 =  0.2449993e-4 ; cP3 = -0.8833959e-8 
    cST   = -0.1275936e-1
    cTP   =  0.6353509e-2 
    cT2P2 =  0.2656174e-7
    cTP2  = -0.1593895e-5 ; cTP3 = 0.5222483e-9 
    cT3P  = -0.4383615e-6 
    cS2P2 = -0.1616745e-8 
    cST2  =  0.9688441e-4 
    cS2TP =  0.4857614e-5 
    cSTP  = -0.3406824e-3

    PP  = P**2
    PPP = P**3
    SS  = S**2
    TT  = T**2
    TTT = T**3
    delta_cT   = cT1*T + cT2*TT + cT3*TTT 
    delta_cS   = cS1*S + cS2*SS 
    delta_cP   = cP1*P + cP2*PP + cP3*PPP 
    delta_cSTP = cTP*T*P + cT3P*TTT*P + cTP2*T*PP + cT2P2*TT*PP  
               + cTP3*T*PPP + cST*S*T + cST2*S*TT + cSTP*S*T*P 
	       + cS2TP*SS*T*P + cS2P2*SS*PP
    c = c000 + delta_cT + delta_cS + delta_cP + delta_cSTP 

    return c
