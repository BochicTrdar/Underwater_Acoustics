# Converted to Python from Matlab code in: 
# https://gorbatschow.github.io/SonarDocs/sound_absorption_air_iso.en/
from numpy import * 

def sound_absorption_air_iso_annex(T=None,RH=None,P=None,f=None):

# Inputs
#   T: temperature \ degree Celsius \ -20 < T < +50
#   RH: relative humidity \ percentage \ 10 < RH < 100
#   P: pressure \ kPa
#   f: frequency \ kHz \ 0.05 < f < 10
# Outputs
#   alpha: absorption of sound in air \ dB/m

    Kelvin = 273.15
    T_ref = Kelvin + 20
    T_kel = Kelvin + T
    T_rel = T_kel / T_ref
    T_01 = Kelvin + 0.01
    Tho = 2239.1
    Thn = 3352.0
    P_ref = 101.325
    P_rel = P / P_ref    
    Xo = 0.209
    Xn = 0.781

    P_sat_P_ref = 10**(-6.8346*(T_01/T_kel)**(1.261)+4.6151)
    H = RH*(P_sat_P_ref/P_rel)

    Fro = P_rel*(24+(4.04e4)*H*(0.02+H)/(0.391+H))
    Frn = P_rel*(T_rel**(-1.0/3.0))*(9+280*H*exp(-4.170*(T_rel**(-1.0/3.0)-1)))

    C = 343.2*(T_rel**(1.0/2.0))
    acr = (1.60e-10)*(T_rel**(1.0/2.0))*(f**2)/P_rel

    amaxO = (2*pi/35)*(10*log10(exp(1)^2))*Xo*((Tho/T_kel)**2)*exp(-Tho/T_kel)
    avibO = amaxO*(f/C)*2*(f/Fro)/(1+(f/Fro)**2)

    amaxN = (2*pi/35)*(10*log10(exp(1)^2))*Xn*((Thn/T_kel)**2)*exp(-Thn/T_kel)
    avibN = amaxN*(f/C)*2*(f/Frn)/(1+(f/Frn)**2)

    alpha = acr + avibO + avibN

return alpha
