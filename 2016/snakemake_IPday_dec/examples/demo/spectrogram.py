#
import numpy as np
import spectrum
import soundfile
import pylab
from easydev import precision

class Spectrogram():
    """

    """
    def __init__(self, signal, ws=128, W=4096, sampling=1, channel=1,
                cmap="jet_r"):
        if len(signal.shape) == 1:
            self.signal = signal
        else:
            self.signal = signal[:,channel-1]
        self.W = W
        self.ws = ws
        self._start_y = 10
        self.sampling = sampling
        self.duration = len(self.signal) / float(self.sampling)

    def plot(self, filename, vmin=None, vmax=None, cmap='jet_r'):
        pylab.clf()
        pylab.imshow(-np.log10(self.results[self._start_y:,:]), 
            origin="lower", 
            aspect="auto", cmap=cmap, vmin=vmin, vmax=vmax)
        pylab.colorbar()

        # Fix xticks
        XMAX = float(self.results.shape[1])  # The max integer on xaxis
        xpos = list(range(0, int(XMAX), int(XMAX/5)))
        xx = [precision(this) for this in np.array(xpos) / XMAX * self.duration]
        pylab.xticks(xpos, xx, fontsize=16)

        # Fix yticks
        YMAX = float(self.results.shape[0])  # The max integer on xaxis
        ypos = list(range(0, int(YMAX), int(YMAX/5)))
        yy = [int(this) for this in np.array(ypos) / YMAX * self.sampling]   
        pylab.yticks(ypos, yy, fontsize=16)

        #pylab.yticks([1000,2000,3000,4000], [5500,11000,16500,22000], fontsize=16)
        #pylab.title("%s echoes" %  filename.replace(".png", ""), fontsize=25)
        pylab.xlabel("Time (seconds)", fontsize=25)
        pylab.ylabel("Frequence (Hz)", fontsize=25)
        pylab.tight_layout()
        pylab.savefig(filename)

    def periodogram(self):
        W = self.W
        ws = self.ws
        N = int(len(self.signal)/ws)
        self.results = np.zeros((W*2+1,N-8))
        print("Duration: %s" % self.duration)
        print("W: %s" % W)
        print("ws: %s" % ws)
        print("Computing %s TFs" % N)
        for i in range(N-8):
            data = self.signal[i*ws:i*ws+W]
            p = spectrum.Periodogram(data, sampling=self.sampling, NFFT=W*4)
            p()
            self.results[:,i] = p.psd
        print("done")

    def pmtm(self):
        W = self.W
        ws = self.ws
        N = int(len(self.signal)/ws)
        self.results = np.zeros((W+1,N-8))
        for i in range(N-8):
            data = self.signal[i*ws:i*ws+W]
            a = spectrum.pmtm(data, 4,NFFT=W*4, show=False)
            Sk = np.mean(abs(a[0].transpose())**2 * a[1], axis=1)
            self.results[:,i] = Sk[0:self.W+1]
            print(i, N)


if __name__ == "__main__":
    import sys
    filename = sys.argv[1]
    if filename.endswith(".wav") is False and filename.endswith(".ogg") is False:
        raise ValueError("accepts only .wav data files")
    basename = filename.rsplit(".", 1)[0]

    # Read the wav/ogg file
    signal, samplerate = soundfile.read(filename)

    # Prepare spectrom computation
    process = Spectrogram(signal, sampling=samplerate)

    if len(sys.argv) == 2:
        output_filename = basename + ".png"
    elif len(sys.argv) == 3:
        process.W = int(sys.argv[2])
        output_filename = basename + "_%s.png" % process.W

    process.periodogram()
    process.plot(output_filename)


