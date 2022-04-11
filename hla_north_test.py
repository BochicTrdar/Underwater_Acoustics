# Test reading HLA North data 

from numpy import *
from scipy import signal
from matplotlib.pyplot import * 
from sioread import *

sampling_rate = 3276.8
nyquist = sampling_rate/2
dt = 1.0/sampling_rate
i1 = 1
i2 = 7000
channels = range(1,28)
xdata = sioread('J1312340.hla.north.sio',i1,i2,channels)
channel1 = xdata[:,0]
n = channel1.size
t = arange(0,n*dt,dt)
nseconds = max( t )
channel1 = channel1 - mean( channel1 )
channel1 = channel1/max( abs( channel1 ) )
ef,et,Rxx = signal.spectrogram(channel1,sampling_rate,nperseg=512,noverlap=500,nfft=512)

figure(1)
plot(t,channel1)
xlabel('Time (s)')
title('HLA North - Channel 1')
grid(True)

figure(2)
pcolormesh(et,ef,10*log10(abs(Rxx)),shading='auto',cmap='jet')
colorbar()
xlabel('Time (s)')
ylabel('Frequency (Hz)')
xlim(0,nseconds)
ylim(0,nyquist)

show()

print('done.')
