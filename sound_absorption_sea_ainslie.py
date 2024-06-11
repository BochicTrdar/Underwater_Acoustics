# Converted to Python from Matlab code in: 
# https://gorbatschow.github.io/SonarDocs/sound_absorption_sea_ainslie.en/
# Sound absorption in sea
from numpy import * 

def sound_absorption_sea_ainslie(T=None,S=None,D=None,f=None,pH=None):

# Inputs
#   T: temperature \ degree Celsius
#   S: salinity \ ppt
#   D: depth \ m
#   f: frequency \ kHz
#   pH: "potential of hydrogen"
# Outputs
#   alpha: absorption of sound in seawater \ dB/km

    D = D*1e-3

    # Boric
    A1 = 0.106*exp((pH-8)/0.56)
    P1 = 1
    f1 = 0.78*sqrt(S/35)*exp(T/26)
    Boric = (A1*P1*f1*(f**2))/((f**2)+(f1**2))

    # MgSO4
    A2 = 0.52*(S/35)*(1+T/43)
    P2 = exp(-D/6)
    f2 = 42*exp(T/17)
    MgSO4 = (A2*P2*f2*(f**2))/((f**2)+(f2**2))

    # H2O
    A3 = 0.00049*exp(-(T/27+D/17))
    P3 = 1
    H2O = A3*P3*(f**2)

    # Total
    alpha = Boric + MgSO4 + H2O
    
return alpha, Boric, MgSO4, H2O 

