#! /usr/bin/env python
from distutils.core import setup

import setuptools

with open('README.rst') as fp:
    long_description = fp.read()

setup(name='pr_demo',
      version='0.0.1',
      author='John Wiggins',
      author_email='john.wiggins@xfel.eu',
      description='Github-Flow Demonstration',
      long_description=long_description,
      url='https://github.com/jwiggins/PR-Demo',
      packages=setuptools.find_packages(),
      )

