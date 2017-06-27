import os
import json
import logging
import scipy.io.wavfile
from glob import glob
from scikits.talkbox.features import mfcc


def prepare_mfcc(dirs):
    """
    This function is used to extract MFCC from previously cleared audion files (see cut_speech.py for that)
    :return: None
    """

    logging.basicConfig(filename="logfile.log", level=logging.DEBUG)

    for d in dirs:
        for speaker in os.listdir(d):
            accent_name = speaker.split('_')[0]
            if len(accent_name) > 2:
                continue

            wav_names = glob('{}/{}/part*.wav'.format(d, speaker))

            for name in wav_names:
                sample = {
                    "accent": accent_name,
                    "speaker": speaker
                }
                part_name = name.split('/')[-1].split('.')[0]

                try:
                    sample_rate, x = scipy.io.wavfile.read(name)
                    ceps, mspec, spec = mfcc(x)
                    sample["ceps"] = ceps.tolist()

                    try:
                        os.mkdir("samples/{}".format(speaker))
                    except OSError:
                        pass

                    save_file = open("samples/{}/{}.json".format(speaker, part_name), "w")
                    json.dump(sample, save_file, indent=4)
                    save_file.close()
                except ValueError:
                    msg = "error reading {}".format(name)
                    print msg
                    logging.error(msg)

    logging.info("Finished extracting features")
