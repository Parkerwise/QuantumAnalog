# 24-02-13
Work today was focused on getting familiar with instruments and reading through the teachspin manual to get an idea of what data to collect for this experiment

# 24-02-15
Today we got our hands on the instruments. We were able to produce a waveform that corresponded to changing AC frequencies on the signal generator. We have been able to use the XY space to find the resonant frequencies, and more specifically we are able to find what frequencies correspond to the peaks in our waveform. Once we have the resonant frequencies and their index, we should be able to interpret the speed of sound. Once we start collecting data it is important to record data regarding the temperature and such.

# 24-02-20

Today we are collecting measurements on our data. We are doing a linear frequency sweep from 800 Hz to 10 kHz. We are going to be changing the length of the tube and we are saving multiple CSV's per length. Then we hope to move on to the spherical unit. Our sweeps are 400 ms. long, Since we know sweep length in time and frequency we can convert between the two. We are using the external trigger that denotes the beginning of the sweep as t=0.00s. We have our sweep length smaller than the window from which are collecting data, so that we can get a full sweep. Data concerning environmental conditions comes from WS-110 weather station: 

Initial conditions:
temp: 74.3 F
temp High: 74.5 F
temp low: 70.0 F
humidity: 9%
humidity low: 7%
humidity high: 17%

TEK0000.CSV: Discard, wasn't using averaged data, used sample
TEK0001.CSV: 60cm length, 74.5 F
TEK0002.CSV: 52.5cm length, 75 F
TEK0003.CSV: 45cm, 75 F
TEK0004.CSV: 37.5cm, 75 F
TEK0005.CSV: 30cm, 75 F
TEK0006.CSV: 22.5cm, 75.2 F
TEK0007.CSV: 15cm, 75.2 F
TEK0008.CSV: 7.5cm, 75.4 F


# 24-02-22

Today we are taking measurements on the spherical chamber. We are using a similar method. We will take one measurement on the bottom microphone, and then 18 measurements for every 10 degrees we can twist the top and the bottom. 

Initial conditions:
temp: 71.2 F
temp High: 71.6 F
temp low: 69.4 F
humidity: 21%
humidity low: 21%
humidity high: 38%

linear Sweep time: 400 ms
freq sweep: 800 Hz - 10 kHz
input amplitude: 100 mV Pk-Pk

TEK0009.CSV: 0 deg, 71.2 F
TEK0010.CSV: 10 deg, 71.6 F
TEK0011.CSV: 20 deg, 71.6 F
TEK0012.CSV: 30 deg, 71.6 F
TEK0013.CSV: 40 deg, 71.6 F
TEK0014.CSV: 50 deg, 71.6 F
TEK0015.CSV: 60 deg, 71.6 F
TEK0016.CSV: 70 deg, 71.2 F
TEK0017.CSV: 80 deg, 71.6 F
TEK0018.CSV: 90 deg, 71.6 F
TEK0019.CSV: 100 deg, 71.6 F
TEK0020.CSV: 110 deg, 71.6 F
TEK0021.CSV: 120 deg, 71.8 F
TEK0022.CSV: 130 deg, 71.8 F
TEK0023.CSV: 140 deg, 71.8 F
TEK0024.CSV: 150 deg, 71.8 F
TEK0025.CSV: 160 deg, 72.0 F
TEK0026.CSV: 170 deg, 72.0 F
TEK0027.CSV: 180 deg, 72.0 F

