Interactive example with *ipython*
##################################

Build the table from a dictionary:

.. code-block:: guess
    :linenos:

    In [1]: import pyRestTable

    In [2]: pyRestTable.__version__
    Out[2]: '2020.0.8.dev5+g2e1eee2'

    In [3]: t = pyRestTable.Table(dict(x=[1], y=[2]))

    In [4]: print(t.reST())
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
