pyRestTable
===========

Format a nice table in reST (reStructuredText) from Python.

Each cell may have multiple lines, separated by a newline.
The content of each cell will be rendered as str(cell).
At present, *pyRestTable* only supports tables with content 
that does not span any cells (no rowspans or columnspans).

* Install with conda: ``conda install -c prjemian pyRestTable``
* Install with pip: ``pip install pyRestTable``

:author:    Pete R. Jemian
:email:     prjemian@gmail.com
:copyright: 2014-2019, Pete R. Jemian
:license:   Creative Commons Attribution 4.0 International Public License (see *LICENSE.txt*)
:docs:      https://pyRestTable.readthedocs.io
:URL:       https://github.com/prjemian/pyRestTable
:TODO:      https://github.com/prjemian/pyRestTable/issues
:citations:
    .. image:: https://zenodo.org/badge/16644277.svg
       :target: https://zenodo.org/badge/latestdoi/16644277
       :alt: DOI: 10.5281/zenodo.1471691
:package:
    .. image:: https://anaconda.org/prjemian/pyresttable/badges/version.svg
       :target: https://anaconda.org/prjemian/pyresttable
       :alt: https://anaconda.org/prjemian/pyresttable
    .. image:: https://img.shields.io/pypi/v/pyresttable.svg
       :target: https://pypi.python.org/pypi/pyresttable
       :alt: https://pypi.python.org/pypi/pyresttable
    .. image:: https://img.shields.io/pypi/pyversions/pyresttable.svg
       :target: https://pypi.python.org/pypi/pyresttable
       :alt: Py 2.7 | 3.5 | 3.6 | 3.7
:build:
    .. image:: https://travis-ci.org/prjemian/pyRestTable.svg?branch=master
       :target: https://travis-ci.org/prjemian/pyRestTable
:coverage:
   .. image:: https://coveralls.io/repos/github/prjemian/pyRestTable/badge.svg?branch=master
       :target: https://coveralls.io/github/prjemian/pyRestTable?branch=master
:review:
    .. image:: https://img.shields.io/lgtm/grade/python/g/prjemian/spec2nexus.svg?logo=lgtm&logoWidth=18
       :target: https://lgtm.com/projects/g/spec2nexus/context:python
       :alt: Language grade: Python
    .. image:: https://img.shields.io/lgtm/grade/javascript/g/prjemian/spec2nexus.svg?logo=lgtm&logoWidth=18
       :target: https://lgtm.com/projects/g/prjemian/spec2nexus/alerts
       :alt: Total alerts
