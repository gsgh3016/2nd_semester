import os
import io
from pathlib import Path
import select
import subprocess as sp
import sys
from typing import Dict, Tuple, Optional, IO


def create_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
    else:
        print(f'{dir} 디렉토리가 이미 존재합니다.')
 
        
def find_files(target: str, extensions=["mp3", "wav", "ogg", "flac"]) -> list:
    """
    extensions에 지정된 형식을 갖는 파일의 이름을 확장자와 분리하여 반환함

    Args:
        target (str): 파일의 이름을 찾을 디렉토리 경로
        extensions (list(str)): 제거할 확장자 종류

    Returns:
        list: extensions에 해당되는 파일 이름이 담긴 배열
    """
    out = []
    for file in Path(target).iterdir():
        if file.suffix.lower().lstrip(".") in extensions:
            out.append(file)
    return out


def copy_process_streams(process: sp.Popen):
    """
    주어진 프로세스의 출력(stdout)과 오류(stderr) 스트림을 현재 프로세스의 출력 스트림으로 복사함

    Args:
        process (sp.Popen): 출력 스트림과 오류 스트림을 복사할 대상 프로세스 객체
    """
    def raw(stream: Optional[IO[bytes]]) -> IO[bytes]:
        assert stream is not None
        if isinstance(stream, io.BufferedIOBase):
            stream = stream.raw
        return stream

    p_stdout, p_stderr = raw(process.stdout), raw(process.stderr)
    stream_by_fd: Dict[int, Tuple[IO[bytes], io.StringIO, IO[str]]] = {
        p_stdout.fileno(): (p_stdout, sys.stdout),
        p_stderr.fileno(): (p_stderr, sys.stderr),
    }
    fds = list(stream_by_fd.keys())

    while fds:
        # `select` syscall will wait until one of the file descriptors has content.
        ready, _, _ = select.select(fds, [], [])
        for fd in ready:
            p_stream, std = stream_by_fd[fd]
            raw_buf = p_stream.read(2 ** 16)
            if not raw_buf:
                fds.remove(fd)
                continue
            buf = raw_buf.decode()
            std.write(buf)
            std.flush()
            
            
def get_song_names(
    extensions=["mp3", "wav", "ogg", "flac"],
    in_path="input"
    ) -> list[str]:
    """
    현재 디렉토리에서 오디오 파일의 이름을 찾아 반환함
    
    Args:
        extensions (list(str)): 제거할 확장자 종류
        in_pat (str): 원본 오디오 파일 경로
    
    Returns:
        str: 오디오 파일의 이름 (확장자 제외)
    """
    file_names = []
    for _, _, files in os.walk(in_path):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                file_names.append(file)
    
    song_names = []
    for file_name in file_names:
        song_name, _ = os.path.splitext(file_name)
        song_names.append(song_name)
    return song_names