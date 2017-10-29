#!/usr/bin/env python3

from setuptools import setup
from setuptools import find_packages

install_requires = [
    'pandas',
    'scipy',
    'scikit-learn',
    'textstat',
    'configparser',
    'psycopg2',
    'beautifulsoup4',
    'sqlalchemy'
]

setup(
      name='ares',
      version='0.0.1',
      description='Sentence Similarity Comparisons',
      author='Sreejith Sreekumar',
      author_email='sreekumar.s@husky.neu.edu',
      url='https://github.com/srjit/ares',
      license='GNU GPL v3',
      install_requires=install_requires,
      packages=find_packages()
)
