import torch

def test_gpu_avail():
  assert not torch.cuda.is_available()


if __name__ == '__main__':
    test_gpu_avail()
