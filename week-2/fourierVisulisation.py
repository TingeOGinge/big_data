import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt
#refer to https://docs.scipy.org/doc/numpy/reference/routines.fft.html
#for more details about the discrete fourier transform

def f(x):
    return 1*np.sin(x)-2*np.sin(5*x)+3*np.cos(4*x)+4*np.sin(10*x)-5*np.sin(15*x)
x = np.linspace(0,2*np.pi,2000)
y = f(x)
plt.plot(x,y)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
#time domain

plt.figure()
yf = abs(fft(y))/len(x)
xf = np.linspace(1,200,200)
plt.plot(xf,yf[0:200])
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
#frequency domain