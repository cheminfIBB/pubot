from distutils.core import setup
from setuptools import find_packages
from pubot import __version__, __authors__


VERSION = __version__
AUTHORS = __authors__

setup(
    name='pubot',
    version=VERSION,
    author=AUTHORS,
    packages=find_packages(),
    install_requires='>=3.6',
    long_description=open('README.md').read(),
    description='Handy script for retrieving scientific publications info',
    license='BSD',
)
