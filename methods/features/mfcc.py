# -*- coding: utf-8 -*-

import numpy as np
import scipy.io.wavfile
from scikits.talkbox.features import mfcc


class MFCC:

    def __init__(self):
        pass

    def process(self, audio_file, cache_file):
        sample_rate, X = scipy.io.wavfile.read(audio_file)
        ceps, mspec, spec = mfcc(X)
        # print ceps.shape
        np.save(cache_file, ceps)
