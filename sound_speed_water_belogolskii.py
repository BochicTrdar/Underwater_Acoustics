# Converted to Python from Matlab code in: 
# https://gorbatschow.github.io/SonarDocs/sound_speed_water_belogolskii.en/
# Sound speed in pure water

from numpy import *

def sound_speed_water_belogolskii(T=None, P=None):

# Inputs
#    T: temperature \ degree Celsius \ 0 < T < 40
#    P: pressure \ kPa \ 100 < P < 60000
# Outputs
#    C: speed of sound in pure water \ m/s

    P = P*1e-3

    a00 =  1402.38744
    a10 =  5.03836171
    a20 = -5.81172916e-2
    a30 =  3.34638117e-4
    a40 = -1.48259672e-6
    a50 =  3.16585020e-9
    a01 =  1.49043589
    a11 =  1.077850609e-2
    a21 = -2.232794656e-4
    a31 =  2.718246452e-6
    a02 =  4.315328330e-3
    a12 = -2.938590293e-4
    a22 =  6.822485943e-6
    a32 = -6.674551162e-8
    a03 = -1.852993525e-5
    a13 =  1.481844713e-6
    a23 = -3.940994021e-8
    a33 =  3.939902307e-10
    TT  = T*T
    TTT = TT*T
    TIV = TTT*T
    TV  = TIV*T
    C0 = a00 + a10*T + a20*TT + a30*TTT + a40*TIV + a50*TV
    M1 = a01 + a11*T + a21*TT + a31*TTT
    M2 = a02 + a12*T + a22*TT + a32*TTT
    M3 = a03 + a13*T + a23*TT + a33*TTT
    C = C0 + M1*( P - 0.101325 ) + M2*( ( P - 0.101325 )**2 ) + M3*( ( P - 0.101325 )**3 )
    
return C

