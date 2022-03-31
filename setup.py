from setuptools import setup, find_packages

setup(
    name='colabtools',
    version='0.0.3',
    description='Python utils package for Google Colab',
    author='Yousef Nami',
    author_email='namiyousef@hotmail.com',
    url='https://github.com/namiyousef/colab-utils',
    install_requires=['nvidia-ml-py3', 'torch'],
    #package_data={}
    packages=find_packages(exclude=('tests*', 'experiments*')),
    license='MIT',
    #entry_points=(),
)