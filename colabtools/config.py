# -- public imports
import torch
from os import environ

# -- constants
DRIVE_NAME = environ.get('DRIVE_NAME', 'drive')

if torch.cuda.is_available():
    DEVICE = 'cuda'
    print('CUDA device detected. Using GPU...')
else:
    DEVICE = 'cpu'
    print('CUDA device NOT detected. Using CPU...')