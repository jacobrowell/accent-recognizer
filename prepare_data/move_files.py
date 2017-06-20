import os
import glob


def move_files():
    """
    This function is used to re-organize and rename wildcat files by accent name
    :return: None
    """
    dirs = [
        '/home/eugen/student/diploma/code/c20/audioFiles/task80',
        # '/home/eugen/student/diploma/code/c20/audioFiles/task81',
        # '/home/eugen/student/diploma/code/c20/audioFiles/task82',
    ]

    for d in dirs:
        for speaker in os.listdir(d):
            wav_name = glob.glob('{}/{}/*.wav'.format(d, speaker))[0].split('/')[-1]

            tok = wav_name.split('_')
            lang_name = tok[2] + '_' + tok[3]

            os.rename('{}/{}'.format(d, speaker), '{}/{}'.format(d, lang_name))

if __name__ == "main":
    move_files()