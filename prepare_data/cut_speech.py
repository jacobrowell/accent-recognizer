import os
import glob
from pydub import AudioSegment, silence


def cut_speech():
    """
    This function is used to cut speech samples into non-silent pieces for further usage in MFCC extraction
    :return: None
    """
    dirs = [
        '/home/eugen/student/diploma/code/c20/audioFiles/task80',
        # '/home/eugen/student/diploma/code/c20/audioFiles/task81',
        # '/home/eugen/student/diploma/code/c20/audioFiles/task82',
    ]

    for d in dirs:
        for speaker in os.listdir(d):
            wav_names = glob.glob('{}/{}/*.wav'.format(d, speaker))

            for name in wav_names:
                print "processing file {}...".format(name)
                sound = AudioSegment.from_file(name, format="wav")

                speech = silence.detect_nonsilent(sound, silence_thresh=-50)
                i = 1
                for frag in speech:
                    part = sound[frag[0]:frag[1]]
                    part.export('{}/{}/part_{}.wav'.format(d, speaker, i), format="wav")
                    i += 1


if __name__ == "main":
    cut_speech()
