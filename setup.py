# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

here = os.path.abspath(os.path.dirname(__file__))

NAME = 'YoBit'
about = {}
with open(os.path.join(here, NAME, '__version__.py')) as f:
    exec(f.read(), about)

setup(
    name=NAME,
    version=about['__version__'],
    description="Python wrapper for YoBit API",
    license="MIT",
    author="Mambix Ltd.",
    author_email="ledi.mambix@gmail.com",
    url="https://github.com/Mambix/yobit",
    packages=find_packages(exclude=('tests')),
    entry_points={'console_scripts': ['YoBit=YoBit:main']},
    install_requires=[],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
	"Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ]
)
