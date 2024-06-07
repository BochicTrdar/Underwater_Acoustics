from numpy import *

def a_Ainslie1998(freq=None, S=None, T=None, pH=None, z=None):
    # Underwater acoustics: calculation of the absorption coefficient
    #
    # SYNTAX: a = a_Ainslie1998(freq, S, T, pH, Z)
    # Units: freq => kHz, S => ppt, T => Celsius, a => dB/km
    # 
    # Reference: 
    # A simplified formula for viscous and chemical absorption in sea water
    # Michael A. Ainslie and James G. McColm
    # Validity: 
    # -6 < T < 35 Celsius ( S = 35 ppt, pH =8, z = 0 )
    # 7.7 < pH,< 8.3 ( T = 10 Celsius,, S = 35 ppt, z = 0 )
    # 5 < S  < 50 ppt ( T = 10 Celsius, pH = 8, z = 0 )
    # 0 < z < 7 km ( T = 10 Celsius, S = 35 ppt, pH = 8 )
    
    #*******************************************************************************
    # Faro, Qua Jul 12 21:08:04 WEST 2017
    # Written by Tordar
    #*******************************************************************************
    
    fxf = freq*freq

    f1 = 0.78*sqrt( S/35.0 )*exp( T/26.0 )
    f2 = 42.0*exp( T/17.0 )
    
    a = 0.106*f1*fxf/( fxf + f1*f1 )*exp( ( pH-8.0 )/0.56 ) + \
    0.52*( 1 + T/43.0 )*( S/35.0 )*f2*fxf/( fxf + f2*f2 )*exp( -z/6.0 ) + \
    0.00049*fxf*exp( -T/27.0 - z/17.0 )
    
    return a
