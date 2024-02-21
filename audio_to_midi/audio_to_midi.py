import os
from dataset_download import prepare_dataset


mp3_url = "http://calab1.ucsd.edu/~datasets/cal500/cal500data/CAL500_32kps.tar"
midi_url = "http://hog.ee.columbia.edu/craffel/lmd/clean_midi.tar.gz"

os.chdir('./audio_to_midi')

print('데이터셋 확인')
prepare_dataset(mp3_url)
prepare_dataset(midi_url)