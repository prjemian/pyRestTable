*simple* (default)
##################

:see: http://docutils.sourceforge.net/docs/ref/rst/directives.html#tables

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
    print(t.reST())
 
build this table source code:

.. code-block:: guess
    :linenos:
 
    === === =====
    one two three
    === === =====
    1,1 1,2 1,3
    2,1 2,2 2,3
    3,1 3,2 3,3
    4,1 4,2 4,3
    === === =====

which is rendered as:

=== === =====
one two three
=== === =====
1,1 1,2 1,3  
2,1 2,2 2,3  
3,1 3,2 3,3  
4,1 4,2 4,3  
=== === =====
