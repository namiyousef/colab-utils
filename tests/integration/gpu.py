import torch
import unittest

class TestGPU(unittest.TestCase):
  
  def check_gpu_avail(self):
      assert torch.cuda.is_available()
