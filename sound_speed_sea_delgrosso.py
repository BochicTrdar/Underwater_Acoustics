# Converted to Python from Matlab code in: 
# https://gorbatschow.github.io/SonarDocs/sound_speed_sea_delgrosso.en/
# Sound speed in sea
from numpy import * 

def sound_speed_sea_delgrosso(T=None,S=None,P=None):
# Inputs
#   T: temperature \ degree Celsius \ 0 < T < 35 
#   S: salinity \ ppt \ 29 < S < 43
#   P: pressure \ kPa \ 0 < P < 98000 
# Outputs
#   C: speed of sound in seawater \ m/s

    C000  = 1402.392
    CT1   =  0.5012285e1
    CT2   = -0.551184e-1
    CT3   =  0.221649e-3
    CS1   =  0.1329530e1
    CS2   =  0.1288598e-3
    CP1   =  0.1560592
    CP2   =  0.2449993e-4
    CP3   = -0.8833959e-8
    CST   = -0.1275936e-1
    CTP   =  0.6353509e-2
    CT2P2 =  0.2656174e-7
    CTP2  = -0.1593895e-5
    CTP3  =  0.5222483e-9
    CT3P  = -0.4383615e-6
    CS2P2 = -0.1616745e-8
    CST2  =  0.9688441e-4
    CS2TP =  0.4857614e-5
    CSTP  = -0.3406824e-3

    p = P*1.019716e-2
    
    TT  = T*T 
    TTT = TT*T
    pp  = p*p
    ppp = pp*p
    SS  = S*S
    
    CT = CT1*T + CT2*TT + CT3*TTT
    CS = CS1*S + CS2*SS
    CP = CP1*p + CP2*pp + CP3*ppp
    CSTP = CTP*T*p      + CT3P*TTT*p + CTP2*T*pp  \
         + CT2P2*TT*pp  + CTP3*T*ppp              \
         + CST*S*T      + CST2*S*TT  + CSTP*S*T*p \
         + CS2TP*SS*T*p + CS2P2*SS*pp

    C = C000 + CT + CS + CP + CSTP

return C
