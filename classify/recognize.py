import numpy as np
import scipy.io.wavfile
from scikits.talkbox.features import mfcc
import sys

if len(sys.argv) < 2:
    exit()


file_name = sys.argv[1]
sample_rate, X = scipy.io.wavfile.read(file_name)
ceps, mspec, spec = mfcc(X)
print ceps.shape

x = []
num_ceps = len(ceps)
x.append(np.mean(ceps[int(num_ceps / 10):int(num_ceps * 9 / 10)], axis=0))
vx = np.array(x)
print vx.shape
print vx[0]
