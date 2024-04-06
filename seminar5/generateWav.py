import numpy as np
from scipy.signal import chirp
from scipy.io.wavfile import write

interval_length1 = 4
interval_length2 = 2
sampleRate = 44100 
startFreq = 1000
stopFreq = 10000
t1 = np.linspace(0, interval_length1, int(sampleRate * (interval_length1)))
t2 = np.linspace(0, interval_length2, int(sampleRate * (interval_length2)))

w1 = chirp(t1, f0=stopFreq, f1=startFreq, t1=interval_length1, method='linear')
w2 = chirp(t2, f0=startFreq, f1=stopFreq, t1=interval_length2, method='quadratic')
w = np.concatenate((w1, w2), axis=0)
write('test.wav', sampleRate, (w*(2**15)).astype(np.int16))