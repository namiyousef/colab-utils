import subprocess
import sys

def install_git(repo_link):
    subprocess.check_call([sys.executable, "-m", "pip", "install", f'git+{repo_link}'])

def test():
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-e', '/Users/yousefnami/Desktop/Main/0.Education/2.UCL/Courses/NLP/argument-mining'])


test()
print("test commit for actions")
