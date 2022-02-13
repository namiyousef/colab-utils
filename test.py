import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


install('git@github.com:namiyousef/argument-mining.git')