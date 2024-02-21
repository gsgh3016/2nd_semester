# 2nd_semester

<b>* 현재 MADMOM 패키지 관련 문제로 디버깅 중입니다.</b> 
- 부산대학교 전자공학과 졸업과제 소스 코드 입니다.
- 프로젝트 기간: 2022년 2학기 (2022.07 ~ 2022.12)
- 주요 내용: Music Source Seperation 모델인 **Demucs**를 활용한 음원 분리와 audio2midi 모델을 활용한 Automatic Music Transcription
- 본 프로젝트는 Meta AI의 [Demucs for colab](https://colab.research.google.com/github/dvschultz/ml-art-colabs/blob/master/Demucs.ipynb) 코드를 바탕으로 됐습니다.
- 기존 프로젝트 소스 코드 원본은 [여기](https://colab.research.google.com/drive/1dkF6TIuqnE9lv9Si8jY-UDoapvEluvs8?usp=sharing)를 참조해주세요.

## 시작하기

### 환경 설정
- OS: macOS Sonoma 14.2.1
- IDE: vscode
- 가상환경: pyenv, venv

### 설치
1. 레포지토리 클론하기
```bash
git clone https://github.com/gsgh3016/2nd_semester.git
```

2. (옵션) 가상환경 설정
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

3. 종속성 설치
```bash
pip install -r requirements.txt
```

## 사용 방법

## 참고 자료 및 기록