#!/usr/bin/env python2

from prepare_data.move_files import move_files
from prepare_data.cut_speech import cut_speech
from prepare_data.prepare_mfcc import prepare_mfcc
from build.train import train

# TODO: accept path to files as program parameter

dirs = [
    '/home/eugen/student/diploma/code/c20/audioFiles/task80'
]

move_files(dirs)
cut_speech(dirs)
prepare_mfcc(dirs)
train()
