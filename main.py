from prepare_data.move_files import move_files
from prepare_data.cut_speech import cut_speech
from prepare_data.prepare_mfcc import prepare_mfcc

# TODO: accept path to files as program parameter
# TODO: implement logging

dirs = [
    '/home/eugen/student/diploma/code/c20/audioFiles/task80',
    # '/home/eugen/student/diploma/code/c20/audioFiles/task81',
    # '/home/eugen/student/diploma/code/c20/audioFiles/task82',
]

move_files(dirs)
cut_speech(dirs)
prepare_mfcc(dirs)
