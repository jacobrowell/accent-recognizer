import os
from glob import glob
from pydub import AudioSegment, silence


def cut_speech(dirs):
    """
    This function is used to cut speech samples into non-silent pieces for further usage in MFCC extraction
    :return: None
    """

    for d in dirs:
        for speaker in os.listdir(d):
            wav_names = glob('{}/{}/*.wav'.format(d, speaker))

            for name in wav_names:
                print "processing file {}...".format(name)
                sound = AudioSegment.from_file(name, format="wav")

                speech = silence.detect_nonsilent(sound, silence_thresh=-50)
                i = 1
                for frag in speech:
                    part = sound[frag[0]:frag[1]]
                    part.export('{}/{}/part_{}.wav'.format(d, speaker, i), format="wav")
                    i += 1
