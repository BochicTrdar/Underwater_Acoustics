from numpy import *

def a_Rhodes2008(freq=None, S=None, T=None, pH=None, z=None, c=None, e=None):
    # Underwater acoustics: calculation of the absorption coefficient
    #
    # SYNTAX: a = a_Rhodes2008(freq, S, T, pH, Z, c, e)
    # Units: freq => kHz, S => ppt, T => Celsius, c => m/s, a => dB/km
    # 
    # Reference: 
    # Excess acoustic absorption attributable to the biological modification of seawater viscosity
    # Christopher J. Rhodes
    # 
    # Coefficients were modified to produce the curve on Rhodes paper. 
    
    #*******************************************************************************
    # Faro, Qua Jul 12 21:18:43 WEST 2017
    # Written by Tordar
    #*******************************************************************************
    
    eta  = 1.79e-3
    etax = eta*( 1.0 + e )
    etab = 2.81*eta
    rhow = 1000.0
    C = 8.0*pi**2/( 3.0*rhow*c**3 )*( etax + etab*3.0/4.0 )*1.0204e10
    
    fxf = freq*freq

    f1 = 0.78*sqrt( S/35.0 )*exp( T/26.0 )
    f2 = 42.0*exp( T/17.0 )
    
    a = 0.106*f1*fxf/( fxf + f1*f1 )*exp( ( pH-8.0 )/0.56 ) + \
    0.52*( 1 + T/43.0 )*( S/35.0 )*f2*fxf/( fxf + f2*f2 )*exp( -z/6.0 ) + \
    C*fxf*exp( -T/27.0 - z/17.0 )
    
    return a
