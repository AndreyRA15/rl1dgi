import struct
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

with open("test.wav", "rb") as file:
    data = file.read()

sampleRate = struct.unpack_from('i', data, offset=24)[0]
print(sampleRate)

dataSize = struct.unpack_from('i', data, offset=40)[0]
print(dataSize)

pureAdcData = np.array([a[0] for a in struct.iter_unpack("h",data[44:44+dataSize:1])])

frequencies, times, spectrogram = signal.spectrogram(pureAdcData, sampleRate, nperseg=1000, window='boxcar', noverlap=0)
# spectrogram[spectrogram==0] = 1e-3
plt.pcolormesh(times, frequencies, spectrogram)

plt.ylabel('Frequency [Hz]')

plt.xlabel('Time [sec]')

plt.show()