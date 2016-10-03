# -*- coding: iso-8859-1 -*-

#-----------------------------------------------------------------------------
# :author:    Pete R. Jemian
# :email:     prjemian@gmail.com
# :copyright: (c) 2014-2016, Pete R. Jemian
#
# Distributed under the terms of the Creative Commons Attribution 4.0 International Public License.
#
# The full license is in the file LICENSE.txt, distributed with this software.
#-----------------------------------------------------------------------------

from . import rest_table
Table = rest_table.Table    # shorten the import trail


__version__ = '2016.1003.1+'
__release__ = __version__
__author__ = 'Pete R. Jemian'
__email__ = 'prjemian@gmail.com'
__copyright_year__ = '2014-2016'
__copyright__ = __copyright_year__ + ', Pete R. Jemian'

__package_name__ = 'pyRestTable'
__license_url__ = 'http://creativecommons.org/licenses/by/4.0/deed.en_US'
__license__ = 'Creative Commons Attribution 4.0 International Public License (see LICENSE file)'
__description__ = 'Format a nice table in reST (reStructuredText ) from Python'
__author_name__ = __author__
__author_email__ = __email__
__url__ = 'http://pyRestTable.readthedocs.io'
__download_url__ = 'https://github.com/prjemian/pyRestTable/tarball/' + __version__
__keywords__ = ['reST', 'table', 'documentation']

__classifiers__ = [
     'Development Status :: 6 - Mature',
     'Environment :: Console',
     'Intended Audience :: Developers',
     'License :: Freely Distributable',
     'License :: Public Domain',
     'Programming Language :: Python',
     'Programming Language :: Python :: 2',
     'Programming Language :: Python :: 2.7',
     'Programming Language :: Python :: 3',
     'Topic :: Documentation',
     'Topic :: Documentation :: Sphinx',
     'Topic :: Software Development',
     'Topic :: Software Development :: Documentation',
     'Topic :: Text Processing :: Markup',
     'Topic :: Utilities',
   ]


__display_version__ = __version__  # used for command line version
if __version__.endswith('+'):
    # try to find out the changeset hash if checked out from git, and append
    # it to __version__ (since we use this value from setup.py, it gets
    # automatically propagated to an installed copy as well)
    __display_version__ = __version__
    __version__ = __version__[:-1]  # remove '+' for PEP-440 version spec.
    try:
        import os, subprocess
        package_dir = os.path.abspath(os.path.dirname(__file__))
        p = subprocess.Popen(['git', 'show', '-s', '--pretty=format:%h',
                              os.path.join(package_dir, '..')],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if out:
            __display_version__ += out.decode().strip()
    except Exception:
        pass
