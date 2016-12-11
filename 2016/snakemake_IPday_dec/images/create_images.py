# Create the time series image for the DOLPHINS WAV
from pylab import *
import soundfile, spectrum

sig, samplerate = soundfile.read('../data/DOLPHINS.wav')
ax = gca()
ax.set_axis_bgcolor('#eeeeee')
ax.plot(linspace(0, len(sig)/samplerate, len(sig)), sig, "k")
grid(True)
xlim([0,7])
xlabel("Time (seconds)", fontsize=20)
title("Dolphins' echoes", fontsize=25)
savefig("dolphin_timeseries.png")
