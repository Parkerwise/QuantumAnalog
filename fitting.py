import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from scipy import signal

plt.rcParams['text.usetex'] = True
plt.rcParams.update({'font.size': 11})

#plots data
columns=["time","pos"]
df=pd.read_csv("TEK0006.CSV",usecols=[3,4],names=["time","amp"])
max_peak_width=1
peak_widths = np.arange(1, max_peak_width)
peak_indices = signal.find_peaks_cwt(y_coordinates, peak_widths)
peak_count = len(peak_indices) # the number of peaks in the array
time=np.array(df.time)
amp=np.array(df.amp)

print(time)
plt.plot(df.time,df.amp)
plt.show()
