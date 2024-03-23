import struct
import matplotlib.pyplot as plt
import numpy as np



with open("sample-3s.wav", "rb") as file:
    data = file.read()

sampleRate = struct.unpack_from('i', data, offset=24)[0]
print(sampleRate)


pureAdcData =[a for a in struct.iter_unpack("h",data[44:])]

# print(pureAdcData)

chartLen = 100

time = [temp/sampleRate for temp in range(0, chartLen)]
signal = np.cos(np.asarray(time)*2.0*np.pi*sampleRate) #pureAdcData[0:chartLen]

plt.plot(time,signal)
plt.grid()
plt.xlabel('t, с')
plt.ylabel('S')
plt.show()

spectr = np.fft.fftshift(np.fft.fft(signal))

freq = [ftemp/time[-1] for ftemp in range(0, chartLen)]

plt.plot(freq,spectr)
plt.grid()
plt.xlabel('f, Гц')
plt.ylabel('S')
plt.show()

