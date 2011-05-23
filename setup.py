#!/usr/bin/env python
#from distutils.core import setup
from setuptools import setup, find_packages

setup(name="simpledependency",
      version="0.0.1",
      description="An embarrassingly simple library for replacing dependencies.",
      author="Benjamin Coe",
      author_email="ben@attachments.me",
      entry_points = {},
      url="https://github.com/attachmentsme/simpledependency",
      packages = find_packages(),
      install_requires = [],
      tests_require=['nose', 'coverage', 'mock']
)
