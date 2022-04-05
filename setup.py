import os
import sys
from setuptools import setup, find_packages

#this_dir = os.path.abspath(os.path.dirname(__file__))
#sys.path.insert(0, this_dir)

#requirements_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'requirements.txt')

#with open(requirements_path, 'r') as f:
#    install_requires = f.read().split()

setup(
    name='colabtools',
    version='0.0.6',
    description='Python utils package for Google Colab',
    author='Yousef Nami',
    author_email='namiyousef@hotmail.com',
    url='https://github.com/namiyousef/colab-utils',
    #install_requires=install_requires,
    install_requires=['torch', 'numpy', 'nvidia-ml-py3'],
    #package_data={}
    packages=find_packages(exclude=('tests*', 'experiments*')),
    license='MIT',
    #entry_points=(),
)