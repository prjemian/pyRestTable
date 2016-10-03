Interactive example with *ipython*
##################################

.. code-block:: guess
    :linenos:

    In [1]: import pyRestTable
 
    In [2]: pyRestTable.__long_description__
 
    Out[2]: 'Format a nice table in reST (reStructuredText ) from Python'
 
    In [3]: pyRestTable.__version__
 
    Out[3]: '2015-1111-1'
 
    In [4]: t = pyRestTable.Table()
 
    In [5]: t.labels = ['x', 'y']
 
    In [6]: t.rows.append([1,2])
 
    In [7]: print(t.reST())
 
    = =
    x y
    = =
    1 2
    = =

which displays as:

= =
x y
= =
1 2
= =

The same table may be rendered in the *grid* reST format:

.. code-block:: guess
    :linenos:

    In [8]: print(t.reST(fmt='grid'))

    +---+---+
    | x | y |
    +===+===+
    | 1 | 2 |
    +---+---+

which displays as:

+---+---+
| x | y |
+===+===+
| 1 | 2 |
+---+---+

The same table may be rendered in the *list-table* reST format:

.. code-block:: guess
    :linenos:

    In [9]: print(t.reST(fmt='list-table'))

    .. list-table:: 
       :header-rows: 1
       :widths: 1 1
   
       * - x
    	 - y
       * - 1
    	 - 2

which displays as:

.. list-table:: 
   :header-rows: 1
   :widths: 1 1

   * - x
     - y
   * - 1
     - 2
