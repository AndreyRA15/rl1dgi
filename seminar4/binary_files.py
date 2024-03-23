import struct
import matplotlib.pyplot as plt
import numpy as np



with open("1kHz_44100Hz_16bit_05sec.wav", "rb") as file:
    data = file.read()

sampleRate = struct.unpack_from('i', data, offset=24)[0]
print(sampleRate)


pureAdcData =[a[0] for a in struct.iter_unpack("h",data[45::2])]

# print(pureAdcData)

chartLen = 1000

# maxFreq = 20e3
# chartLen = 

time = [temp/(sampleRate/2) for temp in range(0, chartLen)]
signal = pureAdcData[0:chartLen]

# plt.plot(time,signal)
# plt.grid()
# plt.xlabel('t, с')
# plt.ylabel('S')
# plt.show()

spectr = np.fft.fft(signal)/chartLen

freq = [ftemp/time[-1] for ftemp in range(0, chartLen)]

# plt.stem(freq,np.abs(spectr))
# plt.grid()
# plt.xlabel('f, Гц')
# plt.ylabel('S')



fig, axs = plt.subplots(1, 2, sharey=False)
axs[0].plot(time,signal)
axs[1].stem(freq,np.abs(spectr))

plt.show()
