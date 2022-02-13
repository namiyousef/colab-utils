from setuptools import setup, find_packages

setup(
    name='colabutils',
    version='0.0.1',
    description='Python utils package for Google Colab',
    author='Yousef Nami',
    author_email='namiyousef@hotmail.com',
    url='https://github.com/namiyousef/colab-utils',
    #install_requires=[],
    #package_data={}
    packages=find_packages(exclude=('tests*', 'experiments*')),
    license='MIT',
    #entry_points=(),
)