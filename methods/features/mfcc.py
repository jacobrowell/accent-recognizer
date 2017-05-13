import numpy as np
import scipy.io.wavfile
from scikits.talkbox.features import mfcc


class MFCC:

    def __init__(self):
        pass

    def process(self, audio_file):
        pass


# for i in range(1, minutes):
#     file_name = files_dir + '/' + 'part_{}.wav'.format(i)
#     sample_rate, X = scipy.io.wavfile.read(file_name)
#     ceps, mspec, spec = mfcc(X)
#     print ceps.shape
