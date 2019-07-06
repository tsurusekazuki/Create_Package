# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py
import os, sys
from setuptools import setup, find_packages


def read_requirements() -> List:
    """Parse requirements from requirements.txt."""
    reqs_path = os.path.join('.', 'requirements.txt')
    with open(reqs_path, 'r') as f:
        requirements = [line.rstrip() for line in f]
    return requirements


setup(
    name='sample',
    version='0.1.0',
    description='Sample package for Python-Guide.org',
    long_description=readme,
    author='Kazuki Tsuruse',
    author_email='b1714935@planet.kanazawa-it.ac.jp',
    install_requires=read_requirements(),
    url='test',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

