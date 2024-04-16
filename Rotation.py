import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from scipy import signal

plt.rcParams['text.usetex'] = True
plt.rcParams.update({'font.size': 11})

#plots data
names=[
"TEK0010.CSV",
"TEK0011.CSV",
"TEK0012.CSV",
"TEK0013.CSV",
"TEK0014.CSV",
"TEK0015.CSV",
"TEK0016.CSV",
"TEK0017.CSV",
"TEK0018.CSV",
"TEK0019.CSV",
"TEK0020.CSV",
"TEK0021.CSV",
"TEK0022.CSV",
"TEK0023.CSV",
"TEK0024.CSV",
"TEK0025.CSV",
"TEK0026.CSV",
"TEK0027.CSV"]

def TimeToFreq(t,f0,dt,df):
    conversion_rate=df/dt
    return t*conversion_rate+f0

df=pd.read_csv("TEK0004.CSV",usecols=[3,4],names=["time","amp"])
time=np.array(df.time)
amp=np.array(df.amp)
start_index=np.where(time==0)[0][0]
end_index=np.where(time==0.4)[0][0]
time=time[start_index:end_index+1]
amp=amp[start_index:end_index+1]

#[angle], [freq], [amplitude]
angle=[10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180]
#each index of time --> freq
freq=[TimeToFreq(time[i],800,0.4,9200) for i in range(len(time))]

#read the amplitude from file 0 at time 0

def GivesAmp(file_index, freq_index):
    df=pd.read_csv(names[file_index],usecols=[3,4],names=["time","amp"])
    time=np.array(df.time)
    amp=np.array(df.amp)
    start_index=np.where(time==0)[0][0]
    end_index=np.where(time==0.4)[0][0]
    time=time[start_index:end_index+1]
    amp=amp[start_index:end_index+1]
    return amp[freq_index]
amplitude=[]
for i in range(len(names)):
    new_angle=[]
    for j in range(len(freq)):
        new_angle.append(GivesAmp(i,j))
    amplitude.append(new_angle)

plt.contourf(freq,angle,amplitude)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Angle (degrees)")
cb=plt.colorbar()
cb.set_label(label="Amplitude (V)")
plt.savefig("Rotation.pdf")
