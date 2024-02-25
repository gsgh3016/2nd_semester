# 2nd_semester

- 부산대학교 전자공학과 졸업과제 소스 코드 입니다.
- 프로젝트 기간: 2022년 2학기 (2022.07 ~ 2022.12)
- 주요 내용: Music Source Seperation 모델인 **Demucs**를 활용한 음원 분리와 audio2midi 모델을 활용한 Automatic Music Transcription
- 본 프로젝트는 Meta AI의 [Demucs for colab](https://colab.research.google.com/github/dvschultz/ml-art-colabs/blob/master/Demucs.ipynb) 코드를 바탕으로 됐습니다.
- 기존 프로젝트 소스 코드 원본은 [여기](https://colab.research.google.com/drive/1dkF6TIuqnE9lv9Si8jY-UDoapvEluvs8?usp=sharing)를 참조해주세요.

## 기술
### Music Source Seperation

- **demucs**([논문 원본](https://arxiv.org/pdf/1911.13254.pdf), [논문 리뷰](https://blog.naver.com/fafg3016/222896593022))
- **Spectrogram**
- **STFT &rarr; Magnitude to dB scale &rarr; EQ Curve**
- **Chroma STFT**

### Automatic Music Transcription

- **audio_to_midi**

    - [tiagoft/audio_to_midi 레포지토리](https://github.com/tiagoft/audio_to_midi/) 참고
    - Fundamental Frequency Detection
    - Onset detection
    - Hidden Markov Models
    - Musicological Models
    - Acoustic Models
    - Estimating priors
    - [참고](https://github.com/tiagoft/audio_to_midi/blob/master/monophonic_audio_to_midi.md)

---

![](https://img.shields.io/badge/OS-macOS_Sonoma_14.2.1-%23000000) ![](https://img.shields.io/badge/IDE-Visual_Studio_Code-%23007ACC) ![](https://img.shields.io/badge/가상환경-pyenv,_venv-%233776AB)

## 시작하기

### 0. git LFS 설치(LFS 설치가 안 된 경우)

#### Window

1. [여기](https://github.com/git-lfs/git-lfs/releases)에서 다운로드 받고 실행
2. 명령 프롬프트 혹은 git에서 `git lfs install` 실행

#### macOS

1. `brew install git-lfs`
2. `git lfs install`

### 1. 레포지토리 클론하기

```bash
git clone https://github.com/gsgh3016/2nd_semester.git
git lfs pull
```

### 2. (옵션) 가상환경 설정

```bash
# 클론 디렉토리로 이동
cd /path/to/cloned/project

# 파이썬 버전 관리
pyenv local 3.11.7

# 가상 환경 생성
python -m venv {가상 환경 이름}

# 가상 환경 활성화(Linux, macOS)
source {가상 환경 이름}/bin/activate

# Window
{가상 환경 이름}\Scripts\activate

# 비활성화 시
deactivate
```

### 3. 종속성 설치

```bash
pip install -r requirements.txt
```

### 4. graduate_project.ipynb 실행

0. ipykernel 모듈이 설치가 안 된 경우
```bash
pip install ipykernel
```

1. 생성한 가상환경을 주피터 노트북 커널에 등록하기
```bash
python -m ipykernel install --user --name={커널 이름 지정} --display-name="선택 메뉴 이름 지정"
```

2. 명령어로 실행하기(커널 선택 후 노트북 쉘마다 실행할 수 있음)
```bash
python graduate_project.ipynb
```

## 디렉토리 설명

1. `input`: 사용자 음원
2. `output`: 악기 별 분리 음원(기본 값 `bass`, `drums`, `other`, `vocals`)
3. `figures`: 악기 별 그래프(`{곡 제목}\_{악기}\_{그래프 종류}.png`)
4. `midi_output`: 두 모델(```sound_to_midi```, ```basic_pitch```)에 따른 악기 별 MIDI 파일
5. `docs`: 발표 자료
6. `util`: 사용한 함수 모듈화

    \* **sound_to_midi**: [tiagoft/audio_to_midi](https://github.com/tiagoft/audio_to_midi) 레포지토리 클론 후 모듈 버전에 따른 코드 수정

## 참고 자료 및 기록

- [demucs (A Défossez, 2019)](https://arxiv.org/pdf/1911.13254.pdf)
- [Madmom (S Böck, 2016)](https://arxiv.org/pdf/1605.07008)
- [basic pitch (RM Bittner, 2022)](https://arxiv.org/pdf/2203.09893.pdf)
- <a href='https://colab.research.google.com/drive/1dkF6TIuqnE9lv9Si8jY-UDoapvEluvs8?usp=sharing'><img src='https://img.shields.io/badge/기존 프로젝트 소스 코드-Open in Colab-%23F9AB00'/></a> (2022.07 ~ 2022.12)
- **Madmom** 모듈 충돌로 **basic pitch**로 대체 (2024.02)