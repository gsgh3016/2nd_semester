import subprocess as sp
from typing import Optional
from util.io_manage import *


def separate(
    inp: Optional[str] = None, 
    outp: Optional[str] = None, 
    mp3: Optional[bool] = False,
    mp3_rate: Optional[int] = 320,
    float32: Optional[int] = True,
    int24: Optional[int] = False,
    two_stems: Optional[str] = None,
    model: Optional[str] = "mdx_extra"  
    ) -> None:
    """
    입력된 오디오 파일을 분리하여 지정된 출력 경로에 저장합니다. demucs 모델을 사용하여
    오디오 소스를 분리하며, 여러 출력 포맷과 설정을 지원합니다.

    Args:
        inp (Optional[str], optional): 오디오 파일들이 위치한 입력 디렉토리의 경로.
        outp (Optional[str], optional): 분리된 오디오 파일들을 저장할 출력 디렉토리의 경로.
        mp3 (Optional[bool], optional): 결과물을 MP3 형식으로 출력할지 여부. 기본값은 False.
        mp3_rate (Optional[int], optional): MP3 출력 시 비트레이트 설정. 기본값은 320kbps.
        float32 (Optional[bool], optional): 결과물을 float32 WAV 형식으로 출력할지 여부. 기본값은 True.
        int24 (Optional[bool], optional): 결과물을 int24 WAV 형식으로 출력할지 여부. 기본값은 False.
        two_stems (Optional[str], optional): 오디오 파일을 두 가지 파트로만 분리할지 여부.
            예: "vocals"를 지정하면 'vocals'와 'other'로 분리됩니다. 기본값은 None.
        model (Optional[str], optional): 실행할 모델의 종류입니다. 기본값은 mdx_extra.

    Returns:
        None: 함수는 직접적인 반환 값이 없습니다. 대신, 프로세스의 실행 결과가 터미널에 출력됩니다.
            오류 발생 시 오류 메시지를 터미널에 출력합니다.

    주의:
        - `float32`와 `int24`를 동시에 True로 설정하면 에러가 발생합니다.
        - 입력 디렉토리에 유효한 오디오 파일이 없는 경우, 작업은 실행되지 않습니다.
    """
    
    cmd = ["python3", "-m", "demucs.separate", "-o", str(outp), "-n", model]
    if mp3:
        cmd += ["--mp3", f"--mp3-bitrate={mp3_rate}"]
    if float32:
        cmd += ["--float32"]
    if int24:
        cmd += ["--int24"]
    if two_stems is not None:
        cmd += [f"--two-stems={two_stems}"]
    files = [str(f) for f in find_files(inp)]
    if not files:
        print(f"No valid audio files in {inp}")
        return
    print("Going to separate the files:")
    print('\n'.join(files))
    print("With command: ", " ".join(cmd))
    p = sp.Popen(cmd + files, stdout=sp.PIPE, stderr=sp.PIPE)
    copy_process_streams(p)
    p.wait()
    if p.returncode != 0:
        print("Command failed, something went wrong.")