# Script to demonstrate processing HIFT data using Python
# Faro, Seg 11 Abr 2022 22:50:04 WEST  
# Written by Orlando Camargo Rodriguez
# Based on hdemo.m by K.Metzger
from numpy import * 
from matplotlib.pyplot import *
from fmst     import *
from fmstset  import *
from hdedop   import *
from hreadchn import *

SoundSpeed = 1498.0        # meters per second
fname = 'X0270949.SAM'    # process this data file
signal = 'M2'             # waveform M2 was sent
law    = 1473
VonC = -1.798/SoundSpeed  # Doppler estimate from earlier processing
channel = 0               # process this channel (names start at 0)
samples = hreadchn(fname, channel)
carrier  =  57.0
sampling = 228.0
FConFS = carrier/sampling # carrier to sample rate ratio
sam_cyc = 4       # samples per carrier cycle
cyc_dig = 5       # number of carrier cycles per sequence bit
angle  = 45.0     # modulation angle
Qfilter = 4       # number of samples in periodic sliding filter summation
perm = fmstset(law) # set up permutation information for fmt
layers = perm["layers"]
L = 2**layers - 1   # number of sequence bits per period
sam_dig = sam_cyc*cyc_dig  # samples per sequence bit (digit)
start_scan = 1       # starting A/D scan to use in processing
n_scans = L*sam_dig  # number of A/D scans per sequence period
Eflag = 0            # clear the data flag
PeriodCount = 0      # initialize the number of sequence periods read
ns = int( n_scans/2 ) # this mimics earlier processing start point
start_scan = start_scan + ns  # by skipping 1/2 half period worth of A/D scans

while ( Eflag == 0 ): # read periods till input is exhausted
# read one period correcting for Doppler:
      demods, Eflag = hdedop(samples, VonC, FConFS, start_scan, n_scans)
      if ( Eflag == 0 ): # process if a set of samples was read
         PeriodCount = PeriodCount + 1  # increment count of periods
         start_scan = start_scan + n_scans # set up start of next period read
# apply sinc filter wrapping around full period:
         N = demods.size
         temp = zeros(N)
         di = arange(0,N)
         for count in range(Qfilter):
             temp = temp + demods[ mod( di+count, N ) ]
         demods = temp/Qfilter
# do sequence removal keeping only resulting amplitudes
         ti = squeeze( abs( fmst( demods, perm, angle ) ) )
         if ( PeriodCount == 1 ):
            tseries = ti
         else:
            tseries = vstack((tseries,ti))
theperiods = 'Number of sequence periods processed: ' + str( PeriodCount )
print( theperiods )
thetitle = 'File: ' + fname
#start_bin = 5600 # matches x0270949.sam processing
#plot_bins = 2001
#tseries = tseries[:,start_bin:start_bin+plot_bins]
tseries = tseries**2
tmax = amax( tseries )
#print( tmax )
tseries = tseries/tmax
theshape = tseries.shape
nsamples = theshape[1]
#print( nsamples )
dt = 1.0/sampling
thetime = arange(0,nsamples*dt,dt)
#print( thetime.size )
Nperiods = arange(0,PeriodCount)
theaverage = zeros(nsamples)
for i in range(PeriodCount):
    theaverage = theaverage + tseries[i,]
tmax = amax( theaverage )
#print( tmax )
theaverage = theaverage/tmax
figure(1)
pcolormesh( thetime, Nperiods, tseries, shading='auto', cmap='jet' )
xlim(24,34)
ylim(0,PeriodCount-1)
colorbar()
xlabel('Time (s)')
ylabel('Reception')
title(thetitle)
figure(2)
plot(thetime,theaverage)
grid(True)
xlabel('Time (s)')
title(thetitle)
show()
