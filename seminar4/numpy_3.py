import numpy as np
import matplotlib.pyplot as plt

chartLen = 1024
maxTime = 1e-3
step = maxTime/(chartLen-1)

t = np.linspace(0, maxTime-step, chartLen)

print(t.size)

w1 = 2e3*2*np.pi
w2 = 1e3*2*np.pi

A1 = 10
ph1 = 45
s1 = A1*np.cos(w1*t + ph1*np.pi/180)

A2 = 10
ph2 = 30
s2 = A2*np.cos(w2*t + ph2*np.pi/180)

C = 5
s_summ = s1+s2 + C

# plt.plot(t, s1)
# plt.plot(t, s2)
# plt.ylabel('U')
# plt.xlabel('t')
# plt.grid()



fig, ax = plt.subplots()
line1 = ax.plot(t, s1)[0] #, label = 'line1', linestyle='--', linewidth=2, color='r')[0]
line2 = ax.plot(t, s2)[0] #, label='line2', linestyle=':', marker = '+')[0]
# line3 = ax.plot(t, s_summ)[0] #, label='line2', linestyle=':', marker = '+')[0]



# line1.set_color('r')
# line2.set_linestyle('--')
# line1.set_label('l1')

ax.grid()
ax.legend()

plt.show()

spectr = np.fft.fft(s_summ)/chartLen

freq = [ftemp/maxTime for ftemp in range(0, chartLen)]



plt.stem(freq, np.abs(spectr))
plt.show()

plt.stem(freq, np.angle(spectr)*180/np.pi)
plt.show()

# spectr0 = spectr
# spectr0[np.abs(spectr)<1e-3] = 0

# plt.stem(freq, np.angle(spectr0)*180/np.pi)
# plt.show()