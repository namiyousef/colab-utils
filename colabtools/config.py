# -- public imports
import torch
from os import environ
try:
    from google.colab import drive
    print('Google Drive import successful.')
except:
    print('Google Drive import failed... continuing anyways...')

# -- constants
DRIVE_NAME = environ.get('DRIVE_NAME', 'drive')

if torch.cuda.is_available():
    DEVICE = 'cuda'
    print('CUDA device detected. Using GPU...')
else:
    DEVICE = 'cpu'
    print('CUDA device NOT detected. Using CPU...')
