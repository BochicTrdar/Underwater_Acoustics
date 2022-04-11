from numpy import *
def fmstset(law=None):
# Function to generate setup information for fast m-sequence
# transform (fmst) function.
#
# law     sequence law written as if it were octal.  For to
#         specify the law 2033 written in octal use the value
#         2033 decimal.
#
# p       A structure containing the number of transform layers
#         and two arrays of permuation vectors.  The vectors 
#         are used by fmt to unscramble and rescample indices
#         so that processing can be performed using the fast
#         Hadamard transform.
#
#         The basic m-sequence transform technique is described
#         in the paper "On Fast M-Sequence Transforms" by
#         M.Cohn and A.Lempel, IEEE Transactions on Information
#         Theory, January 1977.
#
#         22May2000 initial production version...K.Metzger

# convert law written in decimal to binary
    perm = []
    value  = 0
    weight = 1 
    temp   = law
    while ( temp != 0 ):
          value = value + weight*remainder(temp,10)
          temp = int( floor(temp/10) )
          weight = weight*8
# determine the number of transform layers and the period length, L
    layers = 0 
    v = int( floor(value/2) )
    while ( v != 0 ):
          layers = layers + 1
          v = int( floor(v/2) )
    L = 2**layers - 1
    end_bit = int( (L+1)/2 )
    ms_c = 1
    ss_c = 1
    scrm = zeros(L+1)
    unsc = zeros(L+1)
    scrm[0] = 1
    unsc[0] = 1
# generate the permutation index arrays

    for idx in range(1,L+1):
        scrm[idx] = ss_c + 1
        unsc[idx] = ms_c + 1
        temp = bitwise_and(ss_c, value)
        ss_c = int( floor(ss_c/2) )
        while ( temp != 0 ):
             if ( bitwise_and(temp, 1) == 1 ):
                ss_c = bitwise_xor(ss_c, end_bit)
             temp = int( floor(temp/2) )
        if ( bitwise_and(ms_c, 1) == 1 ):
             ms_c = bitwise_xor(ms_c, value)
        ms_c = int( floor(ms_c/2) )
# layers: number of transform layers to be used
#   scrm: permutation to be applied to input
#   unsc: permutation used to order the output
    perm = {"layers":layers,"in":scrm,"out":unsc}
    return perm
