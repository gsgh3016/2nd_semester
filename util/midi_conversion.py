import os
import librosa
from sound_to_midi.monophonic import wave_to_midi
from basic_pitch.inference import predict
from basic_pitch import ICASSP_2022_MODEL_PATH
from util.io_manage import *


def convert_to_midi(midi_out_path: str, audio_dir: str, audio_file_names: list[str]) -> None:
    """
    주어진 오디오 파일 목록을 MIDI 파일로 변환하고 지정된 출력 경로에 저장합니다. 이 함수는
    'sound_to_midi'와 'basic_pitch' 두 가지 방법을 사용하여 오디오 파일에서 MIDI 변환을 시도합니다.

    Args:
        midi_out_path (str): 생성된 MIDI 파일들을 저장할 상위 디렉토리의 경로.
        audio_dir (str): 변환할 오디오 파일들이 위치한 디렉토리의 경로.
        audio_file_names (list[str]): 변환할 오디오 파일들의 파일명 리스트.

    작업 과정:
        - 각 오디오 파일에 대해, 'sound_to_midi'와 'basic_pitch' 방법을 이용하여 MIDI 파일을 생성합니다.
        - 각 방법에 대한 하위 디렉토리를 생성하고, 해당 디렉토리에 MIDI 파일을 저장합니다.
        - MIDI 파일이 이미 존재하는 경우, 해당 파일을 재생성하지 않고 건너뜁니다.

    주의:
        - 파일 변환은 librosa를 통한 오디오 파일 로딩과 각각의 MIDI 변환 알고리즘에 의존합니다.
        - 모든 오디오 파일은 단일 음표 변환만을 지원합니다 (monophonic).
    """
    
    sound_to_midi_dir = os.path.join(midi_out_path, 'sound_to_midi')
    basic_pitch_dir = os.path.join(midi_out_path, 'basic_pitch')
    
    print(f'미디 디렉토리({sound_to_midi_dir}) 확인')
    create_dir(sound_to_midi_dir)
    print(f'미디 디렉토리({basic_pitch_dir}) 확인')
    create_dir(basic_pitch_dir)
    
    for file_name in audio_file_names:
        instrument, _ = os.path.splitext(file_name)
        audio_file_path = os.path.join(audio_dir, file_name)
        
        sound_to_midi_path = os.path.join(sound_to_midi_dir, f'{instrument}.mid')
        basic_pitch_path = os.path.join(basic_pitch_dir, f'{instrument}.mid')
        
        print(f'{instrument} 변환 중')
        if not os.path.exists(sound_to_midi_path):
            y, _ = librosa.load(audio_file_path)
            midi = wave_to_midi(y)
            with open(sound_to_midi_path, 'wb') as f:
                midi.writeFile(f)
        else:
            print(f'{sound_to_midi_path}이(가) 이미 존재합니다.')
        
        if not os.path.exists(basic_pitch_path):
            _, midi_data, _ = predict(audio_file_path)
            midi_data.write(basic_pitch_path)
            print(f'{instrument} 변환 완료')
        else:
            print(f'{basic_pitch_path}이(가) 이미 존재합니다.')