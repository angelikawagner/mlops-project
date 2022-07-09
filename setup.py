from pathlib import Path
from setuptools import find_packages, setup


BASE_DIR = Path(__file__).parent

setup(
    name='sentimentbot',
    packages=find_packages(),
)
