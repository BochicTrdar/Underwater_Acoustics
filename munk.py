from numpy import *
def munk( depths=None , z1=None , c1=None ): 

#Munk deep water profile  
#
# Usage:   c,cz,czz = munk( depths , z1 , c1 ) 
#
#           where z1 is the channel axis and c1 is the sound speed at z1 
#           (default values: z1 = 1200 , c1 = 1480); "cz" and "czz" are 
#           the corresponding sound speed first and second derivatives.       
 
#***************************************************************************************
# Don't like it? Don't use it...
#***************************************************************************************

    c   = []
    cz  = []
    czz = []
    B  = 1.3e3
    B2 = B*B
    epsilon = 7.37e-3
    eta = 2*( depths - z1 )/B
    c   = 1.0 + epsilon*( eta + exp( -eta ) - 1.0 )
    c   = c1*c 
    cz  = ( 2*c1*epsilon/B  ) * ( 1.0 - exp( -eta ) )
    czz = ( 4*c1*epsilon/B2 ) * exp( -eta )

    return c,cz,czz
