from importlib import import_module

def test_imports():
    with open('requirements.txt', 'r') as f:
        requirements = f.read().split()

    for module in requirements:
        imported_module = import_module(module)