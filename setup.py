from distutils.core import setup
from setuptools import find_packages
from glob import glob
from pubot import __version__, __authors__


VERSION = __version__
AUTHORS = __authors__

config_files = glob('config/*cfg')

setup(
    name='pubot',
    version=VERSION,
    author=AUTHORS,
    packages=find_packages(),
    include_package_data=True,
    data_files=[
        ('config', config_files),
    ],
    install_requires=open("requirements.txt").readlines(),
    python_requires='>=3.6,',
    long_description=open('README.md').read(),
    description='Handy script for retrieving scientific publications info',
    license='BSD',
)
