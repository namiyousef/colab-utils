import subprocess
import sys
import os
from pynvml import nvmlInit, nvmlDeviceGetHandleByIndex, nvmlDeviceGetMemoryInfo
import json
import torch

# -- public imports
try:
    from google.colab import drive
    print('Google Drive import successful.')
except:
    print('Google Drive import failed... continuing anyways...')

# -- private imports
from colabtools.config import DRIVE_NAME

def mount_drive():
    base_path = f'/content/{DRIVE_NAME}'
    drive.mount(base_path)
    print('Google Drive mount successful.')
    return os.path.join(DRIVE_NAME, 'MyDrive')


def install_package_dev_mode(repo_name, requirements='requirements.txt'):
    drive_path = mount_drive()
    base_path = os.path.join(drive_path, repo_name)
    subprocess.check_call([sys.executable, "-m", "pip", "install", '-e', base_path])
    subprocess.check_call([sys.executable, '-m', 'pip', "install", '-r', os.path.join(base_path, requirements)])

def install_private_library(path_to_config, repo_name):
    with open(path_to_config, 'r') as f:
        github_config = json.load(f)
        access_token = github_config['access_token']
        username = github_config['username']
    # TODO add branch stuff, add gitlab functionality
    git_link = f'git+https://{access_token}@github.com/{username}/{repo_name}.git'
    try:
      output = subprocess.check_output([sys.executable, '-m', 'pip', 'install', git_link]) # security risk, output not encrypted
    except subprocess.CalledProcessError as e:
      # TODO improve security
      e.cmd[-1] = e.cmd[-1].replace(access_token, '****')
      raise e

def get_gpu_utilization():
    nvmlInit()
    handle = nvmlDeviceGetHandleByIndex(0)
    info = nvmlDeviceGetMemoryInfo(handle)
    return info.used // 1024 ** 2

def move_to_device(data, device='cpu'):
    """
    Function to move data to device
    """
    if torch.is_tensor(data):
        return data.to(device)
    elif isinstance(data, dict):
        return {key: tensor.to(device) for key, tensor in data.items()}
    elif isinstance(data, list):
        raise NotImplementedError('Currently no support for tensors stored in lists.')
    else:
        raise TypeError('Invalid data type.')
