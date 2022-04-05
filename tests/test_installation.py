from importlib import import_module

def test_imports():
    import os.path, pkgutil
    import colabtools

    pkgpath = os.path.dirname(colabtools.__file__)
    modules = [name for _, name, _ in pkgutil.iter_modules([pkgpath])]

    for module in modules:
        imported_module = import_module(f'.{module}', package=colabtools.__name__)



if __name__ == '__main__': test_imports()