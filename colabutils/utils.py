import subprocess
import sys
import os
# -- public imports
try:
    from google.colab import drive
    print('Google Drive import successful.')
except:
    print('Google Drive import failed... continuing anyways...')


# -- private imports
from colabutils.config import DRIVE_NAME

def mount_drive():
    base_path = f'/content/{DRIVE_NAME}'
    drive.mount(base_path)
    print('Google Drive mount successful.')
    return os.path.join(DRIVE_NAME, 'MyDrive')


def install_package_dev_mode(repo_name, requirements='requirements.txt'):
    drive_path = mount_drive()
    base_path = os.path.join(drive_path, repo_name)
    subprocess.check_call([sys.executable, "-m", "pip", "install", f'-e {base_path}'])
    subprocess.check_call([sys.executable, '-m', 'pip', f'-r {os.path.join(base_path, requirements)}'])

