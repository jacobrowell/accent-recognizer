# -*- coding: utf-8 -*-

import numpy as np
import scipy.io.wavfile
from scikits.talkbox.features import mfcc
import os
import glob
import json


class MFCC:

    def __init__(self):
        pass

    def prepare_data(self):
        dirs = [
            '/home/eugen/student/diploma/code/c20/audioFiles/task80',
            # '/home/eugen/student/diploma/code/c20/audioFiles/task81',
            # '/home/eugen/student/diploma/code/c20/audioFiles/task82',
        ]

        accents = dict()

        for d in dirs:
            for speaker in os.listdir(d):
                accent_name = speaker.split('_')[0]
                if len(accent_name) > 2:
                    continue

                if accent_name not in accents:
                    num = len(accents)
                    accents[accent_name] = dict()
                    accents[accent_name]["samples"] = list()

                wav_names = glob.glob('{}/{}/part*.wav'.format(d, speaker))

                for name in wav_names:
                    try:
                        sample_rate, X = scipy.io.wavfile.read(name)
                        ceps, mspec, spec = mfcc(X)
                        x = []
                        num_ceps = len(ceps)
                        x.append(np.mean(ceps[int(num_ceps / 10):int(num_ceps * 9 / 10)], axis=0))
                        vx = np.array(x)
                        accents[accent_name]["samples"].append(vx[0].tolist())
                    except ValueError:
                        print "error reading {}".format(name)
                    except:
                        print "some unexpected error"

                save_file = open("samples_tmp.json", "w")
                json.dump(accents, save_file, indent=4)
                save_file.close()

        num_accents = len(accents)
        i = 0

        for accent in accents:
            accents[accent]["out"] = [0] * num_accents
            accents[accent]["out"][i] = 1
            i += 1

        save_file = open("samples.json", "w")
        json.dump(accents, save_file, indent=4)
        save_file.close()

    def process(self, audio_file, cache_file):
        sample_rate, X = scipy.io.wavfile.read(audio_file)
        ceps, mspec, spec = mfcc(X)
        np.save(cache_file, ceps)
