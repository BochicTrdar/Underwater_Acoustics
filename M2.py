from numpy import *
from scipy.signal import max_len_seq
from matplotlib.pyplot import *

carrier          =   57 # Heard Island signal main frequency
bandwidth        = 11.4 
cycles_per_digit =    5
modulation_angle = pi/4

sampling_frequency = 16*carrier
nyquist = sampling_frequency/2.0

# M-sequence coefficients - 511 digits
m = 9
thestate = zeros(m)
thestate[0] = 1
m_sequence = max_len_seq(m,state=thestate)[0]*2-1

nfreqs = 1001
frequencies = linspace( 0, 2*carrier, nfreqs )
ideal_power_spectrum    = ( sinc( ( frequencies - carrier )/bandwidth ) )**2 
ideal_power_spectrum_dB = log( ideal_power_spectrum )

figure(1)
stem(m_sequence)
title('Heard Island Feasibility Test M2')
xlim(-1,20)
grid(True)

show()
