# Test reading VLA data 
# The VLA was not purely vertical. It had a small tilt of 2 or 3 degrees from vertical toward the
# west, which was determined via conventional matched field processing using the highest level
# tonal set and known source locations. Corrections to element positions can be made using these
# array tilt estimates. Since the source track is not a true radial track, note that the apparent array
# tilt (from the perspective of the source) changes over time, i.e., range.
# The data files under Event S5 and Event S59 have the
# channels reversed. So process the data with the array positions reversed. So channel 1 will have
# a depth of 94.125 m and channel 21 (of data file) will have a depth of 212.25 m.
# Two sources were simultaneously towed by the R/V Sproul: a "deep" source (J-15) and a
# "shallow" source (J-13).
# The deep source was towed at a depth of about 54 m. It transmitted numerous tonals of various
# source levels between 49 Hz and 400 Hz. This tonal set is known as T-49-13. The T-49-13 
# tonal pattern consists of 5 sets of 13 tones. Each set of 13 tones spans the frequencies between
# 49Hz and 400Hz. The first set of 13 tones is projected at maximum level and is referred to as
# the "High Tonal Set." These tones are projected with transmitted levels of approximately 158
# dB. The second set of tones are projected with levels of approximately 132 dB. The subsequent
# sets (3rd, 4th, and 5th) are each projected 4 dB down from the previous set.
# T-49-13 Source Frequencies (Hz)
# 49 64 79  94 112 130 148 166 201 235 283 338 388 <-- High Signal Level
# 52 67 82  97 115 133 151 169 204 238 286 341 391 <-- 2nd Set of Tonals
# 55 70 85 100 118 136 154 172 207 241 289 344 394 <-- 3rd Set of Tonals
# 58 73 88 103 121 139 157 175 210 244 292 347 397 <-- 4th Set of Tonals
# 61 76 91 106 124 142 160 178 213 247 295 350 400 <-- 5th Set of Tonals
# Aside: At the beginning, midway point, and end of the track, the deep source stopped
# projecting CW tones and started projected FM chirps.
# The shallow source was towed at a depth of about 9m. It transmitted 9 frequencies between 109
# Hz and 385 Hz, known as the C-109-9S tonal set.
# The C-109-9S Source Frequencies (Hz)
# 109 127 145 163 198 232 280 335 385 <-- Shallow Source Frequencies
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
#i1 = 50*sampling_rate+1;
#nseconds = 10;
#i2 = nseconds*sampling_rate;
i1 = 4000*sampling_rate + 1
nseconds = 10
i2 = nseconds*sampling_rate
t = arange(0,nseconds,dt)
channels = range(1,22)
xdata = sioread('J1312315.vla.21els.sio',i1,i2,channels)
channel1 = xdata[:,0]
channel1 = channel1 - mean( channel1 )
channel1 = channel1/max( abs( channel1 ) )
ef,et,Rxx = signal.spectrogram(channel1,sampling_rate,nperseg=512,noverlap=500,nfft=512)

figure(1)
plot(t,channel1)
xlabel('Time (s)')
title('VLA - Channel 1')
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
