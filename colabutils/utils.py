
# -- public imports
try:
    from google.colab import drive
    print('Google Drive import successful.')
except:
    print('Google Drive import failed... continuing anyways...')


# -- private imports
from colabutils.config import DRIVE_NAME

def mount_drive():
    drive.mount(f'/content/{DRIVE_NAME}')
    print('Google Drive mount successful.')


def install_package_dev_mode(repo_name, **kwargs):
    
