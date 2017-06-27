import os
import glob
import json
import scipy.io.wavfile
from scikits.talkbox.features import mfcc
from time import time


def prepare_mfcc(dirs):
    """
    This function is used to extract MFCC from previously cleared audion files (see cut_speech.py for that)
    :return: None
    """

    accents = dict()

    for d in dirs:
        for speaker in os.listdir(d):
            accent_name = speaker.split('_')[0]
            if len(accent_name) > 2:
                continue

            if accent_name not in accents:
                accents[accent_name] = dict()
                accents[accent_name]["samples"] = list()

            wav_names = glob.glob('{}/{}/part*.wav'.format(d, speaker))

            for name in wav_names:
                try:
                    sample_rate, X = scipy.io.wavfile.read(name)
                    ceps, mspec, spec = mfcc(X)
                    accents[accent_name]["samples"].append(ceps.tolist())
                except ValueError:
                    print "error reading {}".format(name)
                except:
                    print "some unexpected error"  # TODO: remove handling here

            # FIXME: this causes memory overflow
            save_file = open("samples/samples_tmp.json", "w")
            json.dump(accents, save_file, indent=4)
            save_file.close()

    num_accents = len(accents)
    i = 0

    for accent in accents:
        accents[accent]["out"] = [0] * num_accents
        accents[accent]["out"][i] = 1
        i += 1

    save_file = open("samples/samples-{}.json".format(int(time())), "w")
    json.dump(accents, save_file, indent=4)
    save_file.close()
