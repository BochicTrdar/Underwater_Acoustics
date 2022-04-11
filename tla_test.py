# Test reading TLA data 

from numpy import *
from scipy import *
from scipy import signal
from matplotlib.pyplot import * 
from sioread import *

hyds = [212.25, 206.62, 200.99, 195.38, 189.76, 184.12, 178.49, 172.88, 167.26, 161.62, 155.99]
hyds = hyds + [150.38, 144.74, 139.12, 127.88, 122.25, 116.62, 111.00, 105.38, 99.755, 94.125]
hyds = hyds[::-1]
sampling_rate = 1500
nyquist = sampling_rate/2
dt = 1.0/sampling_rate
i1 = 1
nseconds = 10
i2 = nseconds*sampling_rate
t = arange(0,nseconds,dt)
channels = range(1,23)
xdata = sioread('J1312315.tla.22els.sio',i1,i2,channels)
channel1 = xdata[:,0]
channel1 = channel1 - mean( channel1 )
channel1 = channel1/max( abs( channel1 ) )
ef,et,Rxx = signal.spectrogram(channel1,sampling_rate,nperseg=512,noverlap=500,nfft=512)

figure(1)
plot(t,channel1)
xlabel('Time (s)')
title('TLA - Channel 1')
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
