from setuptools import setup
import os
import sys

PKG_NAME = "MathGames"

_here = os.path.abspath(os.path.dirname(__file__))

if sys.version_info[0] < 3:
    with open(os.path.join(_here, 'README.md')) as f:
        long_description = f.read()
else:
    with open(os.path.join(_here, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()

version = {}
with open(os.path.join(_here, PKG_NAME, 'version.py')) as f:
    exec(f.read(), version)

setup(
    name = PKG_NAME,
    version=version['__version__'],
    description=('A multi-player math game designed for first graders'),
    long_description=long_description,
    author='Jared Dyreson, Peyman Dinani, Kevin Durate',
    author_email='jareddyreson@csu.fullerton.edu',
    url='https://github.com/JaredDyreson/',
    license='GNU GPL-3.0',
    packages=[PKG_NAME],
    install_requires = [
      'beautifulsoup4',
      'colored',
      'lxml',
      'natsort',
      'requests',
      'rply',
      'termcolor'
    ],
    include_package_data=True,
    classifiers=['Programming Language :: Python :: 3.8']
)

