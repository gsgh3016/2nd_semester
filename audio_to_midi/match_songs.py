import os


# 다른 데이터셋을 사용하거나 디렉토리 이름을 변경한 경우 바꿀 것
mp3_dir = './audio_to_midi/CAL500_32kps'
midi_dir = './audio_to_midi/clean_midi'
match_dir = './audio_to_midi/matched'

files = os.listdir(mp3_dir)

artists_songs = {}
exception_mp3_files = [
    'sir_mix-a-lot-baby_got_back.mp3',
    'al_green-sha-la-la_make_me_happy.mp3',
    'chi-lites-stoned_out_of_my_mind.mp3',
    'go-gos-vacation.mp3',
    'third_eye_blind-semi-charmed_life.mp3'
]

for file_name in files:
    if file_name.endswith('.mp3'):
        if file_name in exception_mp3_files:
            artists_songs['third eye blind'] = 'semi-charmed life'
            artists_songs['sir mix-a-lot'] = 'baby got back'
            artists_songs['chi-lites'] = 'stoned out of my mind'
            artists_songs['go-go\'s'] = 'vacation'
            artists_songs['al Green'] = 'sha-la-la make me happy'
        else:
            artist, title = file_name[:-4].split('-')
            artist = artist.replace('_', ' ')
            title = title.replace('_', ' ')
            artists_songs[artist] = title

if not os.path.exists(match_dir):
    os.mkdir(match_dir)
    
i = 0
for artist, title in artists_songs.items():
    if os.path.exists(os.path.join(mp3_dir, artist, f'{title}.mid')):
        os.mkdir(os.path.join(match_dir, artist))
        i += 1
        mp3_file_name = '-'.join([
            artist.replace(' ', '_'),
            title.replace(' ', '_')
        ]) + '.mp3'
        os.rename(
            os.path.join(mp3_dir, mp3_file_name),
            os.path.join(match_dir, artist, f'{title}.mp3')
        )
        os.rename(
            os.path.join(midi_dir, artist, f'{title}.mid'),
            os.path.join(match_dir, artist, f'{title}.mid'),            
        )
    else:
        print(f'{artist} - {title}의 MIDI 파일이 존재하지 않습니다.')
        
# TODO: AUDIO - MIDI 매칭되는 데이터 찾기.
        