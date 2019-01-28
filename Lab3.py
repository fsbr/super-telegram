# life is but a dreammmm
# ya
# yaaaa momma this surely is a dream.

import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy import signal

# comment like this
t = np.linspace(0,5,100000)
g = 1-np.exp(-t)*np.cos(np.sqrt(8)*t) -(1/np.sqrt(8))*np.exp(-t)*np.sin(np.sqrt(8)*t)
noise = 0.25*np.sin(2*np.pi*1000*t)

# signal
noiseyG = g + noise
plt.plot(t,noiseyG)
plt.show()

# take the fft of the data
fftOut = fft(noiseyG)

# set up the frequency labels
k = np.arange(len(noiseyG))
time = 5
freqLabel = k/time
plt.plot(freqLabel,np.abs(fftOut))
plt.xlim([-100,4000])
plt.title('Fourier Transform Amplitude Spectrum')
plt.show()

#compute filter coefficient
coeff = np.sqrt((1e4 -1)/((2*np.pi*1000)**2))
print(coeff)

#new bode plot
a = signal.lti([1],[0.015914, 1])
w1 = np.logspace(-1,4,100)
w, mag, phase = signal.bode(a,w=w1)
plt.subplot(211)
plt.semilogx(w,mag)
plt.title('Magnitude Plot')

plt.subplot(212)
plt.semilogx(w,phase)
plt.title('Phase Plot')
plt.show()

#simulate the filter
tout,y,x = signal.lsim(a,noiseyG,t)
plt.plot(t,y)
plt.title('greatly reduced noise')
plt.xlabel('time (s)')
plt.ylabel('OUTPUT')
plt.show()

# take the fft
fftOut2 = fft(y)

# set up the frequency lables
k = np.arange(len(y))
time = 5
freqLabel = k/time
plt.plot(freqLabel,np.abs(fftOut2))
plt.xlim([-100,4000])
plt.title('Fourier Transform Amplitude Spectrum (Filtered Signal)')
plt.show()

