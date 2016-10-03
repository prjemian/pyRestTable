#!/usr/bin/env python

#-----------------------------------------------------------------------------
# :author:    Pete R. Jemian
# :email:     prjemian@gmail.com
# :copyright: (c) 2014-2016, Pete R. Jemian
#
# Distributed under the terms of the Creative Commons Attribution 4.0 International Public License.
#
# The full license is in the file LICENSE, distributed with this software.
#-----------------------------------------------------------------------------

from setuptools import setup, find_packages
import os
import re
import sys

# pull in some definitions from the package's __init__.py file
sys.path.insert(0, os.path.join('.', 'src', ))
import pyRestTable


verbose=1
long_description = open('README.rst', 'r').read()


setup (name =             pyRestTable.__package_name__,        # pyRestTable
       version =          pyRestTable.__version__,
       license =          pyRestTable.__license__,
       description =      pyRestTable.__description__,
       long_description = long_description,
       author =           pyRestTable.__author_name__,
       author_email =     pyRestTable.__author_email__,
       url =              pyRestTable.__url__,
       download_url =     pyRestTable.__download_url__,
       keywords =         pyRestTable.__keywords__,
       platforms =        'any',
       package_dir =      {'': 'src'},
       packages =         ['pyRestTable', ],
       #packages=find_packages(),
       classifiers =      pyRestTable.__classifiers__,
      )
