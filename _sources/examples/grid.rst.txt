*grid* (*complex*)
##################

:see: http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html#grid-tables

These python commands:

.. code-block:: python
    :linenos:

    import pyRestTable
    t = pyRestTable.Table()
    t.labels = ('one', 'two', 'three' )
    t.rows.append( ['1,1', '1,2', '1,3',] )
    t.rows.append( ['2,1', '2,2', '2,3',] )
    t.rows.append( ['3,1', '3,2', '3,3',] )
    t.rows.append( ['4,1', '4,2', '4,3',] )
    print(t.reST(fmt='grid'))

build this table in reST source code:

.. code-block:: guess
    :linenos:

    +-----+-----+-------+
    | one | two | three |
    +=====+=====+=======+
    | 1,1 | 1,2 | 1,3	|
    +-----+-----+-------+
    | 2,1 | 2,2 | 2,3	|
    +-----+-----+-------+
    | 3,1 | 3,2 | 3,3	|
    +-----+-----+-------+
    | 4,1 | 4,2 | 4,3	|
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

.. note::

   **API Changes**
   
   * version 2015.1111.01

      In versions previous to 2015.1111.01, the ``complex`` output 
      table format was supported::
      
          print t.reST(fmt='complex')
      
      The ``complex`` output format has been aliased ``grid`` to be
      consistent with the docutils [#]_ documentation::
      
          print(t.reST(fmt='grid'))
      
      The two commands are identical (except the latter is upgraded
      for compatibility with Python v3).  
      To preserve existing code, no
      plans are made to deprecate the ``complex`` name.
      
       .. [#] docutils: http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html
    
