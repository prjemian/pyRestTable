*grid* (*complex*)
##################

:see: http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#grid-tables

These commands::

    import pyRestTable
    t = pyRestTable.Table()
    t.labels = ('one', 'two', 'three' )
    t.rows.append( ['1,1', '1,2', '1,3',] )
    t.rows.append( ['2,1', '2,2', '2,3',] )
    t.rows.append( ['3,1', '3,2', '3,3',] )
    t.rows.append( ['4,1', '4,2', '4,3',] )
    print t.reST(fmt='grid')

build this table source code::

   +-----+-----+-------+
   | one | two | three |
   +=====+=====+=======+
   | 1,1 | 1,2 | 1,3   |
   +-----+-----+-------+
   | 2,1 | 2,2 | 2,3   |
   +-----+-----+-------+
   | 3,1 | 3,2 | 3,3   |
   +-----+-----+-------+
   | 4,1 | 4,2 | 4,3   |
   +-----+-----+-------+

which is rendered as:

+-----+-----+-------+
| one | two | three |
+=====+=====+=======+
| 1,1 | 1,2 | 1,3   |
+-----+-----+-------+
| 2,1 | 2,2 | 2,3   |
+-----+-----+-------+
| 3,1 | 3,2 | 3,3   |
+-----+-----+-------+
| 4,1 | 4,2 | 4,3   |
+-----+-----+-------+

API Changes
***********

In versions previous to 2015.1111.01, the `complex` output 
table format was supported.  ::

    print t.reST(fmt='complex')

The `complex` output format has been renamed `grid` to be
consistent with the docutils [#]_ documentation::

    print t.reST(fmt='grid')

The two commands are identical.  To preserve existing code, no
plans are made to deprecate the `complex` name.

 .. [#] docutils: http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html
 