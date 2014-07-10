pyRestTable
===========

:author:    Pete R. Jemian
:email:     prjemian@gmail.com
:copyright: 2014, Pete R. Jemian
:license:   Creative Commons Attribution 4.0 International Public License (see *LICENSE.txt*)
:URL:       https://github.com/prjemian/pyRestTable
:PyPI:      https://pypi.python.org/pypi/pyRestTable/ 
:documentation: http://prjemian.github.io/pyRestTable
:RTD:       http://pyRestTable.readthedocs.org

Format a nice table in reST (reStructuredText ) from Python.
Each cell may have multiple lines, separated by a newline.
The content of each cell will be rendered as str(cell).
At present, *pyRestTable* only supports tables with content 
that does not span any cells (no rowspans or columnspans).
