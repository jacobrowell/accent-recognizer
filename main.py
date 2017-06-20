from prepare_data.move_files import move_files
from prepare_data.cut_speech import cut_speech
from prepare_data.prepare_mfcc import prepare_mfcc
from build.train import train

move_files()
cut_speech()
prepare_mfcc()
train()
