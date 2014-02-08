#!/usr/bin/env python
#-----------------------------------------------------------------------------
# Copyright (c) 2014, Pete R. Jemian.
#
# Distributed under the terms of the -tba- License.
#
# The full license is in the file LICENSE, distributed with this software.
#-----------------------------------------------------------------------------

#from distutils.core import setup, Extension
from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages, Extension

import os, sys

# pull in some definitions from the package's __init__.py file
sys.path.insert(0, os.path.join('src', ))
import pyRestTable

verbose=1

setup (name =  pyRestTable.__package_name__,        # pyRestTable
       version = pyRestTable.__version__,
       license = pyRestTable.__license__,
       description = pyRestTable.__description__,
       long_description = pyRestTable.__long_description__,
       author=pyRestTable.__author_name__,
       author_email=pyRestTable.__author_email__,
       url=pyRestTable.__url__,
       download_url=pyRestTable.__download_url__,
       keywords=pyRestTable.__keywords__,
       platforms='any',
       package_dir = {'': 'src'},
       packages = find_packages('src'),
       classifiers= ['Development Status :: 5 - Production/Stable',
                     'Intended Audience :: Developers',
                     'License :: Freely Distributable',
                     'License :: Public Domain',
                     'Programming Language :: Python',
                     'Programming Language :: Python :: 2',
                     'Programming Language :: Python :: 2.7',
                     'Topic :: Documentation',
                     'Topic :: Software Development :: Documentation',
                     'Topic :: Text Processing :: Markup',
                     ],
      )
