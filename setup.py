#-*- coding: utf-8 -*-

"""
    pymarks
    ~~~~~~~
    $ pip install .
"""

from distutils.core import setup
import os

setup(
    name='pymarks',
    version='0.0.1',
    url='http://github.com/mekarpeles/pymarks',
    author='mek',
    author_email='michael.karpeles@gmail.com',
    packages=[
        'pymarks',
        ],
    platforms='any',
    license='LICENSE',
    description="Pymarks benchmarks for common python operations",
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
)
