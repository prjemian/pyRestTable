pyRestTable
===========

:version:   2014-02-15
:author:    Pete R. Jemian
:email:     prjemian@gmail.com
:copyright: 2014, Pete R. Jemian
:URL:       https://github.com/prjemian/pyRestTable
:download:  https://github.com/prjemian/pyRestTable/tarball/2014-02-15
:license:   Creative Commons Attribution 4.0 International Public License (see *LICENSE.txt*)

Format a nice table in reST (reStructuredText ) from Python.
Each cell may have multiple lines, separated by "\n".
The content of each cell will be rendered as str(cell).
At present, *pyRestTable* only supports tables with content 
that does not span any cells (no rowspans or columnspans).

Usage
=====

**pyRestTable** provides support for
writing tables in the format of reStructured Text [#]_ 
from Python programs.  (It provides
no command-line or GUI program itself -- no "entry points"; 
it should be used within a Python program.)

* Import the pyRestTable package
* Create the Table() instance
* Set the list of column labels
* Append the list of column cells for each row
* Render the table (default table format is "simple")

Examples are provided to demonstrate usage.

.. [#] http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html

Features
========

* create *simple* or *complex* (also known as *grid*) reST formatted tables
* defines table cells through Python lists, row-by-row

:see: http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#tables

Installation
============

available for installation from PyPI via standard installers::

  $ pip install pyRestTable

or

::

  $ easy_install -U pyRestTable
  
or download the tarball from GitHub and use setuptools to install::

  $ tar xzf pyRestTable-2014-02-15.tar.gz.tar.gz
  $ cd pyRestTable-2014-02-15
  $ python setup.py install

Examples
========

Examples are provided to demonstrate usage.

Interactive example with ipython
--------------------------------

   In [1]: import pyRestTable
   
   In [2]: pyRestTable.__long_description__
   
   Out[2]: 'Format a nice table in reST (reStructuredText ) from Python'
   
   In [3]: pyRestTable.__version__
   
   Out[3]: '2014-02-15'
   
   In [4]: t = pyRestTable.Table()
   
   In [5]: t.labels = ['x', 'y']
   
   In [6]: t.rows.append([1,2])
   
   In [7]: print t.reST()

   ::

	   = =
	   x y
	   = =
	   1 2
	   = =

The same table may be rendered in the "complex" reST format:
   
   In [8]: print t.reST(fmt='complex')

   ::
   
		+---+---+
		| x | y |
		+===+===+
		| 1 | 2 |
		+---+---+
   

Complex table example
---------------------

These commands::

    import pyRestTable
    t = pyRestTable.Table()
    t.labels = ('Name\nand\nAttributes', 'Type', 'Units', 'Description\n(and Occurrences)', )
    t.rows.append( ['one,\ntwo', "buckle my", "shoe.\n\n\nthree,\nfour", "..."] )
    t.rows.append( ['class', 'NX_FLOAT', '..', '..', ] )
    t.rows.append( range(0,4) )
    t.rows.append( [None, t, 1.234, range(3)] )
    print t.reST(fmt='complex')

build this table source code::

    +------------+-----------------------------------------+--------+-------------------+
    | Name       | Type                                    | Units  | Description       |
    | and        |                                         |        | (and Occurrences) |
    | Attributes |                                         |        |                   |
    +============+=========================================+========+===================+
    | one,       | buckle my                               | shoe.  | ...               |
    | two        |                                         |        |                   |
    |            |                                         |        |                   |
    |            |                                         | three, |                   |
    |            |                                         | four   |                   |
    +------------+-----------------------------------------+--------+-------------------+
    | class      | NX_FLOAT                                | ..     | ..                |
    +------------+-----------------------------------------+--------+-------------------+
    | 0          | 1                                       | 2      | 3                 |
    +------------+-----------------------------------------+--------+-------------------+
    | None       | <__main__.Table instance at 0x022B8EE0> | 1.234  | [0, 1, 2]         |
    +------------+-----------------------------------------+--------+-------------------+

Example using XML source data from a URL
----------------------------------------

Another example (*cansas.py* in the source distribution) shows how content can be 
scraped from a URL that provides XML (using the *lxml* package) and written as a
reST table.  This particular XML uses a namespace which we setup in the 
variable ``nsmap``::

	#!/usr/bin/env python
	
	from lxml import etree
	from pyRestTable import Table
	
	xml_url = 'http://www.cansas.org/svn/1dwg/trunk/examples/cs_af1410.xml'
	nsmap = dict(cs='urn:cansas1d:1.1')
	doc = etree.parse(xml_url)
	node_list = doc.xpath('//cs:SASentry', namespaces=nsmap)
	t = Table()
	t.labels = ['SASentry', 'description', 'measurements']
	for node in node_list:
	    subnode = node.find('cs:Title', namespaces=nsmap)
	    if subnode is not None:
	    	s = etree.tostring(subnode, method="text")
	    	s_name = node.attrib['name']
	    	count = len(node.xpath('cs:SASdata', namespaces=nsmap))
	    else:
	    	s_name = ''
	    	count = ''
	    title = s.strip()
	    t.rows += [[s_name, title, count]]
	
	print len(node_list), 'SASentry elements in', xml_url
	print
	# use "complex" since s_name might be empty string
	print t.reST(fmt='complex')

The output from this code::

	10 SASentry elements in http://www.cansas.org/svn/1dwg/trunk/examples/cs_af1410.xml
	
	+-----------+--------------------------------------+--------------+
	| SASentry  | description                          | measurements |
	+===========+======================================+==============+
	| AF1410:10 | AF1410-10 (AF1410 steel aged 10 h)   | 2            |
	+-----------+--------------------------------------+--------------+
	| AF1410:8h | AF1410-8h (AF1410 steel aged 8 h)    | 2            |
	+-----------+--------------------------------------+--------------+
	| AF1410:qu | AF1410-qu (AF1410 steel aged 0.25 h) | 2            |
	+-----------+--------------------------------------+--------------+
	| AF1410:cc | AF1410-cc (AF1410 steel aged 100 h)  | 2            |
	+-----------+--------------------------------------+--------------+
	| AF1410:2h | AF1410-2h (AF1410 steel aged 2 h)    | 2            |
	+-----------+--------------------------------------+--------------+
	| AF1410:50 | AF1410-50 (AF1410 steel aged 50 h)   | 2            |
	+-----------+--------------------------------------+--------------+
	| AF1410:20 | AF1410-20 (AF1410 steel aged 20 h)   | 1            |
	+-----------+--------------------------------------+--------------+
	| AF1410:5h | AF1410-5h (AF1410 steel aged 5 h)    | 2            |
	+-----------+--------------------------------------+--------------+
	| AF1410:1h | AF1410-1h (AF1410 steel aged 1 h)    | 2            |
	+-----------+--------------------------------------+--------------+
	| AF1410:hf | AF1410-hf (AF1410 steel aged 0.5 h)  | 2            |
	+-----------+--------------------------------------+--------------+

The resulting table is shown:

10 SASentry elements in http://www.cansas.org/svn/1dwg/trunk/examples/cs_af1410.xml

+-----------+--------------------------------------+--------------+
| SASentry  | description                          | measurements |
+===========+======================================+==============+
| AF1410:10 | AF1410-10 (AF1410 steel aged 10 h)   | 2            |
+-----------+--------------------------------------+--------------+
| AF1410:8h | AF1410-8h (AF1410 steel aged 8 h)    | 2            |
+-----------+--------------------------------------+--------------+
| AF1410:qu | AF1410-qu (AF1410 steel aged 0.25 h) | 2            |
+-----------+--------------------------------------+--------------+
| AF1410:cc | AF1410-cc (AF1410 steel aged 100 h)  | 2            |
+-----------+--------------------------------------+--------------+
| AF1410:2h | AF1410-2h (AF1410 steel aged 2 h)    | 2            |
+-----------+--------------------------------------+--------------+
| AF1410:50 | AF1410-50 (AF1410 steel aged 50 h)   | 2            |
+-----------+--------------------------------------+--------------+
| AF1410:20 | AF1410-20 (AF1410 steel aged 20 h)   | 1            |
+-----------+--------------------------------------+--------------+
| AF1410:5h | AF1410-5h (AF1410 steel aged 5 h)    | 2            |
+-----------+--------------------------------------+--------------+
| AF1410:1h | AF1410-1h (AF1410 steel aged 1 h)    | 2            |
+-----------+--------------------------------------+--------------+
| AF1410:hf | AF1410-hf (AF1410 steel aged 0.5 h)  | 2            |
+-----------+--------------------------------------+--------------+

