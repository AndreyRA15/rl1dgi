import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile

chartLen = 1000
maxTime = 1e-3
step = maxTime/(chartLen-1)

t = np.linspace(0, maxTime, chartLen)

print(t.size)

w1 = 300e3*2*np.pi
w2 = 100e3*2*np.pi
w3 = 400e3*2*np.pi

A1 = 10
ph1 = 0
s1 = A1*np.cos(w1*t + ph1*np.pi/180)

A2 = 15
ph2 = 0
s2 = A2*np.cos(w2*t + ph2*np.pi/180)

A3 = 20
ph3 = 0
s3 = A3*np.cos(w3*t + ph3*np.pi/180)

Ssumm = np.concatenate((s1, s2, s3), axis=0)






frequencies, times, spectrogram = signal.spectrogram(Ssumm, 1/maxTime*chartLen, nperseg=100, window='boxcar', noverlap=0)

plt.pcolormesh(times, frequencies, spectrogram, shading='gouraud')

plt.ylabel('Frequency [Hz]')

plt.xlabel('Time [sec]')

plt.show()