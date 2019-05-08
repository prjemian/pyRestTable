#!/usr/bin/env python

#-----------------------------------------------------------------------------
# :author:    Pete R. Jemian
# :email:     prjemian@gmail.com
# :copyright: (c) 2014-2019, Pete R. Jemian
#
# Distributed under the terms of the Creative Commons Attribution 4.0 International Public License.
#
# The full license is in the file LICENSE, distributed with this software.
#-----------------------------------------------------------------------------

from setuptools import setup, find_packages
import os
import re
import sys

import versioneer

# pull in some definitions from the package's __init__.py file
basedir = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(basedir, 'src', ))
import pyRestTable


verbose=1
long_description = open(os.path.join(basedir, 'README.rst'), 'r').read()


setup (name =             pyRestTable.__package_name__,        # pyRestTable
       version =          versioneer.get_version(),
       cmdclass =         versioneer.get_cmdclass(),
       license =          pyRestTable.__license__,
       description =      pyRestTable.__description__,
       long_description = long_description,
       author =           pyRestTable.__author_name__,
       author_email =     pyRestTable.__author_email__,
       url =              pyRestTable.__url__,
       download_url =     pyRestTable.__download_url__,
       keywords =         pyRestTable.__keywords__,
       platforms =        pyRestTable.__platforms__,
       package_dir =      {'': 'src'},
       packages =         ['pyRestTable', ],
       #packages=find_packages(),
       package_data     = {'pyRestTable': ['LICENSE.txt',]},
       classifiers =      pyRestTable.__classifiers__,
       test_suite  =      "tests",
       zip_safe =         pyRestTable.__zip_safe__,
      )
