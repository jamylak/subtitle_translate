#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='subtitle_translate',
      version='0.0.1',
      description='This package has translate components.',
      author='Jane Doe',
      author_email='user@email.com',
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
      license='LICENSE.txt',
    )
