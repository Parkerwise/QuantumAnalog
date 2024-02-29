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
start_index=np.where(time==0)[0][0]
end_index=np.where(time==0.4)[0][0]

time=time[start_index:end_index]
amp=amp[start_index:end_index]
peak_indices = signal.find_peaks(amp,width=20)
peak_indices=peak_indices[0]
peak_count = len(peak_indices) # the number of peaks in the array

plt.plot(time,amp)
peaks_time=[time[peak_indices[i]] for i in range(len(peak_indices))]
peaks_amp=[amp[[peak_indices[i]]] for i in range(len(peak_indices))]

#get index starting at 0.0 and ending at 0.4 s
start_index=np.where(time==0)
end_index=np.where(time==0.4)
plt.plot(peaks_time,peaks_amp,"o")
plt.show()
