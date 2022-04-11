from numpy import *
def hdedop(samples=None, VonC=None, FConFS=None, start_scan=None, n_scans=None):
# Function to frequency shift and adjust sample times to account for
# Doppler compression/expansion when processing HIFT data sets.
#
# samples      Column vector of sample values extracted from a "standard"
#              HIFT data set.
#
# VonC         Ratio of estimated source velocity as seen at the site that
#              generated the sample data set divided by the estimated speed
#              of sound.
#
# FConFS       The ratio of the carrier frequency (FC) divided by the sample
#              rate (FS).
#
# start_scan   The scan to start the output at.  This is relative to the
#              start of the data set AFTER doppler correction.  For example
#              if there are N samples per period of reception.  The starting
#              indices of successive periods are 1, N, 2N, 3N, ... .
#              
# n_scans      The number of dedoppered values to generate
#
# demods       A column vector of complex downshifted, resampled to compensate
#              for doppler.  These have not been filtered!!!  There remains
#              the -2fc term.
#
# Eflag        This is zero if the requested number of values has been
#              generated.  Otherwise it is nonzero.
#
#              Based on hdedop.m by K.Metzger

    Eflag  = 0
    demods = []
    s = 1.0 + VonC
    d_start_scan = (start_scan           - 1)/s # start scan in doppler data
    d_end_scan   = (start_scan + n_scans - 1)/s # end scan in doppler data
    d_start = int( floor(d_start_scan)     )
    d_end   = int( floor(d_end_scan  ) + 1 )
    d_N = d_end - d_start + 1

    L = samples.size

    if ( d_end >= L ):
       Eflag = 1
    else:
       dse = arange(d_start,d_end+1)
       demods = exp(-2j*pi*s*dse*FConFS)*samples[dse]
       di = arange(start_scan - 1, start_scan - 1 + n_scans)
       d_index = di/s - d_start
       di = d_index.astype(int)
       temp = demods[ di ]
       demods = temp + ( d_index - di )*( demods[di+1] - temp )*s

    return demods, Eflag
