#!/usr/bin/env python2

from prepare_data.prepare_mfcc import prepare_mfcc
from prepare_data.move_files import move_files
from prepare_data.cut_speech import cut_speech
from classify.classify import classify
from build.train import train
import sys

# TODO: accept path to files as program parameter

dirs = [
    '/home/eugen/student/diploma/code/c20/audioFiles/task80'
]

action = sys.argv[1]

# if not action:
#     move_files(dirs)
#     cut_speech(dirs)
#     prepare_mfcc(dirs)
#     train()
if action == 'prepare':
    move_files(dirs)
    cut_speech(dirs)
    prepare_mfcc(dirs)
elif action == 'build':
    train()
elif action == 'classify':
    filename = sys.argv[2]
    if not filename or type(filename) != str:
        filename = input('Provide a path to audio file: ')
    res = classify(filename)
    print res
elif action == 'help':
    print ''.join([
        'This is a program to classify speaker accent using neural network.\n\n',
        'Supply such arguments:\n',
        'prepare - to prepare data for training\n',
        'build - to build and train network\n',
        'classify [filename] - to classify the provided speech sample\n',
        'help - show this message and exit',
    ])
else:
    print 'Unknown action'
