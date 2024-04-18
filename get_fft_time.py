import numpy as np
import scipy.io as sio
import scipy.io.wavfile
import matplotlib.pyplot as plt
import argparse 
from scipy import fftpack
from time import time

parser = argparse.ArgumentParser()
parser.add_argument('--filename', required=False, default='filename.wav')
args = parser.parse_args()

print("drawing plot for", args.filename)

samplerate, data = sio.wavfile.read(args.filename)
fftsize = len(data)

start = time()
data_fft = fftpack.fft(data, fftsize)
end = time()
print('processing time: ', end-start)

# fast fourier transform 
