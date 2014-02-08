pyRestTable
===========

:version:   2014-02
:author:    Pete R. Jemian
:email:     prjemian@gmail.com
:copyright: (c) 2014, Pete R. Jemian
:URL:       https://github.com/prjemian/pyRestTable

Format a nice table in reST (reStructuredText ) from Python

Each cell may have multiple lines, separated by "\n".
The content of each cell will be rendered as str(cell).

EXAMPLE

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


Interactive example with ipython::

   In [1]: import pyRestTable
   
   In [2]: pyRestTable.__long_description__
   Out[2]: 'Format a nice table in reST (reStructuredText ) from Python'
   
   In [3]: pyRestTable.__version__
   Out[3]: '2014-02'
   
   In [4]: t = pyRestTable.Table()
   
   In [5]: t.labels = ['x', 'y']
   
   In [6]: t.rows.append([1,2])
   
   In [7]: print t.reST()

	   = =
	   x y
	   = =
	   1 2
	   = =
   