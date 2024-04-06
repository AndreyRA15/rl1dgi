import numpy as np
from scipy.signal import chirp
from scipy.io.wavfile import write

interval_length1 = 4 # in seconds
interval_length2 = 2 # in seconds
fs = 44100 # sampling of your signal
f0 = 1000   # frequency 1
f1 = 10000   # frequency 2
t1 = np.linspace(0, interval_length1, int(fs * (interval_length1)))
t2 = np.linspace(0, interval_length2, int(fs * (interval_length2)))

w1 = chirp(t1, f0=f1, f1=f0, t1=interval_length1, method='linear') # check also other methods
w2 = chirp(t2, f0=f0, f1=f1, t1=interval_length2, method='quadratic') # check also other methods
w = np.concatenate((w1, w2), axis=0)
write('test.wav', fs, (w*(2**15)).astype(np.int16))