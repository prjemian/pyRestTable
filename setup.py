#!/usr/bin/env python

#-----------------------------------------------------------------------------
# :author:    Pete R. Jemian
# :email:     prjemian@gmail.com
# :copyright: (c) 2014-2020, Pete R. Jemian
#
# Distributed under the terms of the Creative Commons Attribution 4.0 International Public License.
#
# The full license is in the file LICENSE, distributed with this software.
#-----------------------------------------------------------------------------

from setuptools import setup
import os
import sys
import versioneer

# pull in some definitions from the package's __init__.py file
basedir = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(basedir, 'src', ))
import pyRestTable as package


verbose=1
long_description = """\
Format a nice table in reST (reStructuredText) from Python.

Each cell may have multiple lines, separated by a newline.
The content of each cell will be rendered as str(cell).
At present, *pyRestTable* only supports tables with content 
that does not span any cells (no rowspans or columnspans).
"""

setup (name =             package.__package_name__,        # pyRestTable
       version =          versioneer.get_version(),
       cmdclass =         versioneer.get_cmdclass(),
       license =          package.__license__,
       description =      package.__description__,
       long_description = long_description,
       author =           package.__author_name__,
       author_email =     package.__author_email__,
       url =              package.__url__,
       download_url =     package.__download_url__,
       keywords =         package.__keywords__,
       platforms =        package.__platforms__,
       package_dir =      {'': 'src'},
       packages =         ['pyRestTable', ],
       package_data     = {'pyRestTable': ['LICENSE.txt',]},
       classifiers =      package.__classifiers__,
       test_suite  =      "tests",
       zip_safe =         package.__zip_safe__,
      )
