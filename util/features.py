import os
from typing import Tuple
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import librosa.display
from util.io_manage import *
import matplotlib.ticker as ticker


def read_graph(img_path: str, figsize: Tuple[int, int]):
    """
    이미지 파일을 읽어서 주어진 크기로 플롯을 표시함

    Args:
        img_path (str): 읽을 이미지 파일의 경로
        figsize (Tuple[int, int]): 플롯의 크기
    """
    img = mpimg.imread(img_path)
    plt.figure(figsize=figsize)
    plt.imshow(img)
    plt.axis('off')
    plt.show()


def create_spectrogram(figure_path: str, instrument: str, D: np.ndarray, sr: int):
    """
    주어진 오디오 데이터로부터 스펙트로그램을 생성하고 이미지 파일로 저장함

    Args:
        figure_path (str): 저장할 파일 경로
        instrument (str): 스펙트로그램을 생성할 악기의 이름
        D (np.ndarray): Short-time Fourier transform (STFT) 결과
        sr (int): 오디오의 샘플링 레이트
    """
    DB = librosa.amplitude_to_db(D, ref=np.max)

    inst_dir = os.path.join(figure_path, instrument)
    create_dir(inst_dir)
    spectrogram_path = os.path.join(inst_dir, f'{get_song_name()}_{instrument}_spectrogram.png')

    figsize = (64, 24)
    if not os.path.exists(spectrogram_path):
        os.makedirs(inst_dir, exist_ok=True)
        plt.figure(figsize=figsize)
        librosa.display.specshow(DB, sr=sr, hop_length=512, x_axis='time', y_axis='log')
        plt.colorbar(format='%+2.0fdB')
        plt.title(f'{instrument}_Spectrogram', fontsize=24)
        plt.savefig(spectrogram_path)
        plt.close()
        
    # read_graph(spectrogram_path, figsize)
    
    
def create_eq_curve(figure_path: str, instrument: str, D: np.ndarray, sr: int):
    """
    주어진 오디오 데이터의 평균 진폭 스펙트럼으로부터 EQ 커브를 생성하고 이미지 파일로 저장함

    Args:
        figure_path (str): 저장할 파일 경로
        instrument (str): EQ 커브를 생성할 악기의 이름
        D (np.ndarray): Short-time Fourier transform (STFT) 결과
        sr (int): 오디오의 샘플링 레이트
    """
    inst_dir = os.path.join(figure_path, instrument)
    create_dir(inst_dir)
    eq_curve_path = os.path.join(inst_dir, f'{get_song_name()}_{instrument}_eq_curve.png')
    mean_amplitude = librosa.amplitude_to_db(np.mean(D, axis=1), ref=np.max)

    frequencies = librosa.fft_frequencies(sr=sr, n_fft=2048)

    audible_indices = np.where((frequencies >= 20) & (frequencies <= 20000))
    audible_frequencies = frequencies[audible_indices]
    audible_mean_amplitude = mean_amplitude[audible_indices]

    def freq_formatter(x, pos):
        if x >= 1000:
            return f'{int(x/1000)}k'
        else:
            return f'{int(x)}'
        
    figsize = (10, 6)
    if not os.path.exists(eq_curve_path):
        plt.figure(figsize=figsize)
        plt.plot(audible_frequencies, audible_mean_amplitude)
        plt.xscale('log')  # 주파수 축을 로그 스케일로 설정
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Volumn (dB)')
        plt.title(f'{instrument}_Mean EQ Curve')
        plt.grid(True, which="both", ls="--")  # 그리드 추가
        plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(freq_formatter))
        plt.xlim(20, 20000)  # x축 범위를 가청 주파수 범위로 설정
        plt.savefig(eq_curve_path)
        
    # read_graph(eq_curve_path, figsize)
    
    
def create_mel_spectrogram(figure_path: str, instrument: str, y: np.ndarray, sr: int):
    """
    주어진 오디오 데이터로부터 멜 스펙트로그램을 생성하고 이미지 파일로 저장함

    Args:
        figure_path (str): 저장할 파일 경로
        instrument (str): 멜 스펙트로그램을 생성할 악기의 이름
        y (np.ndarray): 오디오 신호
        sr (int): 오디오의 샘플링 레이트
    """
    S = librosa.feature.melspectrogram(y=y, sr=sr)
    S_DB = librosa.amplitude_to_db(S, ref=np.max)
    
    inst_dir = os.path.join(figure_path, instrument)
    create_dir(inst_dir)
    mel_path = os.path.join(inst_dir, f'{get_song_name()}_{instrument}_mel_spectrogram.png')
    
    figsize = (64, 24)
    if not os.path.exists(mel_path):
        plt.figure(figsize=figsize)
        librosa.display.specshow(S_DB, sr=sr, hop_length=512, x_axis='time', y_axis='log')
        plt.title(f'{instrument}_Mel Spectrogram', fontsize=24)
        plt.colorbar()
        plt.savefig(mel_path)
        
    # read_graph(mel_path, figsize)
    
    
def create_chroma(figure_path: str, instrument: str, y: np.ndarray, sr: int):
    """
    주어진 오디오 데이터로부터 크로마그램을 생성하고 이미지 파일로 저장함

    Args:
        figure_path (str): 저장할 파일 경로
        instrument (str): 크로마그램을 생성할 악기의 이름
        y (np.ndarray): 오디오 신호
        sr (int): 오디오의 샘플링 레이트
    """
    chromagram = librosa.feature.chroma_stft(y=y, sr=sr, hop_length=512)
    
    inst_dir = os.path.join(figure_path, instrument)
    create_dir(inst_dir)
    chroma_path = os.path.join(inst_dir, f'{get_song_name()}_{instrument}_chroma.png')
    
    figsize = (16, 6)
    if not os.path.exists(chroma_path):
        plt.figure(figsize=figsize)
        librosa.display.specshow(chromagram, x_axis='time', y_axis='chroma', hop_length=512)
        plt.title(f'{instrument}_chroma', fontsize=24)
        plt.savefig(chroma_path)
        
    # read_graph(chroma_path, figsize)