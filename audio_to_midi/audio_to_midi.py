import subprocess
import os


# download lakh dataset
script_path = 'lakh_dataset.sh'
file_path = 'lmd_full.tar.gz'

os.chdir('./audio_to_midi')

print('check dataset file exists.')
if not os.path.exists(file_path):
    print(f'{file_path} not found. Executing {script_path} to download and extract.\n')
    subprocess.run(['bash', script_path], check=True)
else:
    print(f'{file_path} already exists. No need to execute {script_path}.')
print('dataset is ready.')    
