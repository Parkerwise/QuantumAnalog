import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from scipy import signal

plt.rcParams['text.usetex'] = True
plt.rcParams.update({'font.size': 11})

#plots data
columns=["time","pos"]
df=pd.read_csv("TEK0004.CSV",usecols=[3,4],names=["time","amp"])
time=np.array(df.time)
amp=np.array(df.amp)
peak_indices = signal.find_peaks(amp,width=20)
peak_indices=peak_indices[0]
peak_count = len(peak_indices) # the number of peaks in the array
print(peak_count)
print(peak_indices)
plt.plot(df.time,df.amp)
peaks_time=[time[peak_indices[i]] for i in range(len(peak_indices))]
peaks_amp=[amp[[peak_indices[i]]] for i in range(len(peak_indices))]
plt.plot(peaks_time,peaks_amp,"o")
plt.show()
