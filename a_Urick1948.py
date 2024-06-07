from numpy import *

def a_Urick1948(freq=None,a=None,rho0=None,rho1=None,mu=None,c0=None,C=None):
    # Underwater acoustics: calculation of the absorption coefficient
    #
    # SYNTAX: a = a_Urick1948(freq,a,rho0,rho1,mu,c0,C)
    # Units: freq => Hz, a => m, rho => kg/m3, mu => m2/s, n => 1/m3
    # Reference: 
    # The Absorption of Sound in Suspensions of Irregular Particles
    # R. J. Urick

    
    #*******************************************************************************
    # Arraial do Cabo, Sab 14 Out 2017 19:14:22 WEST 
    # Written by Tordar
    #*******************************************************************************
    
    omega = 2*pi*freq
    l = c0/freq
    k = 2*pi/l
    beta = sqrt( omega/( 2*mu ) )
    s = 9/( 4*beta*a )*( 1 + 1 /( beta*a ) )
    tau = 0.5 + 9/( 4*beta*a )
    sigma = rho1/rho0
    p = 1.0/6.0*k**4*a**3 + k*( sigma - 1 )**2*s/( s**2 + ( sigma + tau )**2 )
    a = C*p

    return a
