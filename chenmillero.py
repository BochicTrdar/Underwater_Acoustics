from numpy import *
def chenmillero( P=None , T=None , S=None ):

#CHENMILLERO: Converts Pressure, Temperature and Salinity to Sound Velocity in Sea Water
#through Chen and Millero's formula. 
#
# Usage:    sound_speed_in_sea_water = chenmillero( pressure , temperature , salinity ) ; 
#         
#           When applied to a vector 'chenmillero' returns a vector,  
#           when applied to a matrix 'chenmillero' returns a matrix 
#           after operating on every column. 
#           Range of validity: temperature 0 to 40 Celsius degrees, 
#           salinity 0 to 40 parts per thousand and pressure 0 to 1000 bar. 
#
#           You can validate the calculations using the following values 
#           (taken from Apel "Atmosphere-Ocean Dynamics", page 603): 
#
#          Data = [0 35 -2 1439.7;
#                  0 35  0 1449.1;
#                  0 35  2 1458.1;
#                  0 35  4 1466.6;
#                  0 35  7 1478.7;
#                  0 35 10 1489.8;
#                  0 35 13 1500.2;
#                  0 35 16 1509.8;
#                  0 35 19 1518.7;
#                  0 35 22 1526.8;
#                  0 35 25 1534.4;
#                  0 35 28 1541.3;
#                  0 35 31 1547.6;
#                100 35 -2 1456.1;  
#                100 35  0 1465.5;
#                100 35  2 1474.5; 
#                100 35  4 1483.1;
#                100 35  7 1495.1;
#                100 35 10 1506.3;
#                100 35 13 1516.7;
#                100 35 16 1526.4;
#                100 35 19 1535.3; 
#                200 35 -2 1472.8;  
#                200 35  0 1482.3;
#                200 35  2 1491.2; 
#                200 35  4 1499.8;
#                200 35  7 1511.8;
#                300 35 -2 1489.9;  
#                300 35  0 1499.3;
#                300 35  2 1508.2; 
#                300 35  4 1516.6; 
#                400 35 -2 1507.2;  
#                400 35  0 1516.5;
#                400 35  2 1525.3; 
#                400 35  4 1533.7; 
#                500 35 -2 1524.8;
#                500 35  0 1534.0; 
#                500 35  2 1542.7; 
#                600 35 -2 1542.6;
#                600 35  0 1551.6; 
#                600 35  2 1560.2]
# 

#Max error using Apel data for validation: 0.07 m/s. 

#***************************************************************************************
# First version: 03/07/2002
# 
# Contact: orodrig@ualg.pt
# 
# Any suggestions to improve the performance of this 
# code will be greatly appreciated.
# 
# Reference: C-T. Chen and F.J. Millero, "Speed of sound in seawater at high pressures" 
#                 J. Acoust. Soc. Am. 62(5) pp 1129-1135, 1977. 
#
#***************************************************************************************

# Don't like it? Don't use it... 

    c = []

    c00 =  1402.388  ; c01 =  5.03830    ; c02 = -5.81090e-2 ; c03 =  3.3432e-4  ; c04 = -1.47797e-6 ; c05 = 3.1419e-9 
    c10 =  0.153563  ; c11 =  6.8999e-4  ; c12 = -8.1829e-6  ; c13 =  1.3632e-7  ; c14 = -6.1260e-10 
    c20 =  3.1260e-5 ; c21 = -1.7111e-6  ; c22 =  2.5986e-8  ; c23 = -2.5353e-10 ; c24 =  1.0415e-12 
    c30 = -9.7729e-9 ; c31 =  3.8513e-10 ; c32 = -2.3654e-12
    a00 =  1.389     ; a01 = -1.262e-2   ; a02 =  7.166e-5   ; a03 =  2.008e-6   ; a04 = -3.21e-8 
    a10 =  9.4742e-5 ; a11 = -1.2583e-5  ; a12 = -6.4928e-8  ; a13 = 1.0515e-8   ; a14 = -2.0142e-10
    a20 = -3.9064e-7 ; a21 =  9.1061e-9  ; a22 = -1.6009e-10 ; a23 = 7.994e-12
    a30 =  1.100e-10 ; a31 =  6.651e-12  ; a32 = -3.391e-13
    b00 = -1.922e-2  ; b01 = -4.42e-5    ; b10 =  7.3637e-5  ; b11 = 1.7950e-7 
    d00 =  1.727e-3  ; d10 = -7.9836e-6

    PP    = P**2
    PPP   = P**3
    PPPP  = P**4
    SS    = S**2
    TT    = T**2
    TTT   = T**3
    TTTT  = T**4 
    TTTTT = T**5

    cw = (c00 + c01*T + c02*TT + c03*TTT + c04*TTTT + c05*TTTTT)
       + (c10 + c11*T + c12*TT + c13*TTT + c14*TTTT)*P 
       + (c20 + c21*T + c22*TT + c23*TTT + c24*TTTT)*PP 
       + (c30 + c31*T + c32*TT)*PPP 
    a  = (a00 + a01*T + a02*TT + a03*TTT + a04*TTTT) 
       + (a10 + a11*T + a12*TT + a13*TTT + a14*TTTT)*P 
       + (a20 + a21*T + a22*TT + a23*TTT)*PP 
       + (a30 + a31*T + a32*TT)*PPP 
    b  =  b00 + b01*T + ( b10 + b11*T)*P 
    d  =  d00 + d10*P
    c = cw + a*S + b*( S**(1.5) ) + d*SS 
   
    return c

