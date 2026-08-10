*list-table*
############

:see: http://docutils.sourceforge.net/docs/ref/rst/directives.html#list-table

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
    print(t.reST(fmt='list-table'))
 
.. sidebar: the `:widths:` role

   The values in the `:widths:` role are computed from the
   maximum character width for each column.  These values may need to 
   be adjusted manually, for example, if cell content in a column
   includes any ReST markup.

build this table source code:

.. code-block:: guess
    :linenos:

    .. list-table:: 
      :header-rows: 1
      :widths: 3 3 5
   
      * - one
        - two
        - three
      * - 1,1
        - 1,2
        - 1,3
      * - 2,1
        - 2,2
        - 2,3
      * - 3,1
        - 3,2
        - 3,3
      * - 4,1
        - 4,2
        - 4,3

which is rendered as:

.. list-table:: 
   :header-rows: 1
   :widths: 3 3 5

   * - one
     - two
     - three
   * - 1,1
     - 1,2
     - 1,3
   * - 2,1
     - 2,2
     - 2,3
   * - 3,1
     - 3,2
     - 3,3
   * - 4,1
     - 4,2
     - 4,3
