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
:copyright: 2014-2022, Pete R. Jemian
:license:   Creative Commons Attribution 4.0 International Public License (see *LICENSE.txt*)
:docs:      https://github.io/prjemian/pyRestTable
:URL:       https://github.com/prjemian/pyRestTable
:TODO:      https://github.com/prjemian/pyRestTable/issues
:version:   |version|
:release:   |release|
:published: |today|

.. toctree::
   :maxdepth: 2
   :glob:

   usage
   install
   examples/index
   code/*
   changes
   license


Features
########

* create *simple*, *plain*, *grid* (also known as *complex*), and *list-table* 
  reST formatted tables [#]_, also *markdown*-formatted tables [#]_
* defines table cells through Python lists, row-by-row
* use with Python 2 or Python 3

.. [#] http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#tables
.. [#] https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#tables

Indices and tables
##################

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

