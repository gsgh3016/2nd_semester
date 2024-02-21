import requests
import tarfile
import os
from tqdm import tqdm


def download_file(url, local_filename=None):
    if local_filename is None:
        local_filename = url.split('/')[-1]
    
    print(f"파일 다운로드: {url}")
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        total_size_in_bytes = int(r.headers.get('content-length', 0))
        
        progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                progress_bar.update(len(chunk))
                f.write(chunk)
    
    if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
        print('오류가 발생했습니다.')
    else:
        print('파일 다운로드 완료')
    return local_filename


def extract_tar_file(tar_path, extract_path='.'):
    print("압축 해재 중")
    with tarfile.open(tar_path, "r:gz") as tar:
        tar.extractall(path=extract_path)
        print(f"압축 해제 완료: {tar_path}")
            
       
def prepare_dataset(url):
    file_name = url.split('/')[-1]
    directory = file_name.split()[0]
    
    print(f'{directory} 데이터셋 존재 확인')
    if not os.path.exists(directory):
        download_file(url)
        extract_tar_file(file_name)
        os.remove(file_name)
    else:
        print('이미 준비된 데이터셋입니다.')