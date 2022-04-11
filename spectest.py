# Script to demonstrate processing HIFT data using Python
# Faro, Seg 11 Abr 2022 22:51:17 WEST  
# Written by Orlando Camargo Rodriguez
# Based on hdemo.m by K.Metzger
from scipy import signal
from numpy import * 
from matplotlib.pyplot import *
from fmstset  import *
from hreadchn import *

SoundSpeed = 1498.0       # meters per second
fname = 'X0270949.SAM'    # process this data file
thesignal = 'M2'          # waveform M2 was sent
law    = 1473
VonC = -1.798/SoundSpeed  # Doppler estimate from earlier processing
channel = 0               # process this channel (names start at 0)
samples = hreadchn(fname, channel)
carrier  =  57.0
sampling = 228.0
nyquist  = sampling/2 
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
dt = 1.0/sampling
nsamples = samples.size
t = arange(0,nsamples*dt,dt)
samples = samples - mean( samples )
themax = samples.max()
samples = samples/themax
ef,et,Rxx = signal.spectrogram(samples,sampling)

figure(1)
plot(t,samples)
title(fname)
ylim(-1,1)
grid(True)

figure(2)
pcolormesh(et,ef,10*log10(abs(Rxx)),shading='auto',cmap='jet')
colorbar()
xlabel('Time (s)')
ylabel('Frequency (Hz)')
ylim(0,nyquist)
title(fname)
show()

