# Converted to Python from Matlab code in: 
# https://gorbatschow.github.io/SonarDocs/depth_to_pressure_sea_leroy_97.en/
# Depth and pressure relationship

# Equation for the "standard" ocean. Use corrective terms for particular applications.
# P_corrected = P( Z, phi  ) - Delta P( Z )
# Area of applicability Latitude Delta P( Z ) (MPa) Accuracy +/- 1e3 (Pa)
# Common oceans          60º N - 40º S 1e-2*Z/( Z + 100  ) + 6.2e-6*Z 8
# North Eastern Atlantic 30º N - 35º S 8e-3*Z/( Z + 200  ) + 4e-6*Z   3
# Circumpolar Antarctic                8e-3*Z/( Z + 1000 ) + 1.6e-6*Z 1
# Mediterranean Sea                   -8.5e-6*Z + 1.4e-9*Z^2          2
# Red Sea                              0                              2
# Arctic Ocean                         0                              1
# Sea of Japan                         7.8e-6*Z                       1
# Sulu Sea                8º           1e-2*Z/( Z + 100 ) + 1.6e-5*Z + 1e-9*Z^2 <1
# Halmahera basin         0º           8e-3*Z/( Z + 50  ) + 1.3e-5*Z            <1
# Celebes basin           4º           1.2e-2*Z/( Z + 100 ) + 7e-6*Z + 2.5e-10*Z^2 2
# Weber Deep              6º           1.2e-2*Z/( Z + 100 ) + 7e-6*Z + 2.5e-10*Z^2 2
# Black Sea              43º           1.13e-4*Z                      1
# Baltic Sea             60º           1.8e-4*Z                       1

from numpy import * 

def depth_to_pressure_sea_leroy_97(D=None,L=None):
# Inputs
#   D: depth \ m \ 0 < D < 4000
#   L: latitude \ degree \ -90 < L < 90
# Outputs
#   P: pressure \ kPa
    Lr = deg2rad( L )
    G = 9.7803*( 1 + 5.3e-3*sin( Lr )**2) 
    P45 = 1.00818e-2*D + 2.465e-8*(D**2) - 1.25e-13*(D**3) + 2.8e-19*(D**4)
    k = ( G - 2e-5*D )/(9.80612 - 2e-5*D)
    P =  P45*k*1e3

return P

