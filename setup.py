# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 10:03:16 2016

@author: gezer
"""

from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("helloworld.py")
)