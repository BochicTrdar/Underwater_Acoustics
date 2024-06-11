# Converted to Python from Matlab code in: 
# https://gorbatschow.github.io/SonarDocs/pressure_to_depth_sea_leroy_97.en/
# Depth and pressure relationship

# Equation for the "standard" ocean. Use corrective terms for particular applications.
# Z_corrected = Z(P,phi) + Delta Z(P)
# Area of applicability   Latitude       Delta Z(P) (m)       Accuracy +/- m
# Common oceans           60º N - 40º S  P/(P + 1) + 5.7e-2*P 0.8
# North Eastern Atlantic  30º N - 35º S  P/(P + 2) + 3e-2*P   0.3
# Circumpolar Antarctic                  4e-2*P - 2e-4*P^2    0.1
# Mediterranean Sea                     -7e-2*P + 2 e-3*P^2   0.2
# Red Sea                                0                    0.2
# Arctic ocean                           0                    0.1
# Sea of Japan                           6e-2*P               0.1
# Sulu Sea               8º              0.9*P/(P+1)+0.17*P+7e-4*P^2 0.2
# Halmahera basin        0º              0.8*P/( P + 0.5 ) + 0.125*P 0.1
# Celebes basin          4º              1.2*P/( P + 1 ) + 6.7e-2*P + 2.2e-4*P^2 0.4
# Weber deep             6º              1.2*P/( P + 1 ) + 6.7e-2*P + 2.2e-4*P^2 0.4
# Black Sea             43º              1.1*P                0.1
# Baltic Sea            60º              1.8*P                0.1
from numpy import * 

def pressure_to_depth_sea_leroy_97(P=None,L=None):

# Inputs
#   P: pressure \ kPa
#   L: latitude \ degree \ -90 < L < 90
# Outputs
#   D: depth \ m
    Lr = deg2rad( L )
    P = P*1e-3
    G = 9.780318*(1 + (5.2788e-3)*(sin(Lr)**2) - (2.36e-5)*(sin(Lr)**4))
    D = (9.72659e2)*P - (2.512e-1)*(P**2) + (2.279e-4)*(P**3) - (1.82e-7)*(P**4)
    D = D/( G + (1.092e-4)*P )

return D

