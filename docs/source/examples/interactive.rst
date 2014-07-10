Interactive example with ipython
################################

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
