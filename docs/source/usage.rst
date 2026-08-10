Usage
#####

**pyRestTable** provides support for
writing tables in the format of reStructured Text [#]_ 
from Python programs.  (It provides
no command-line or GUI program itself -- no **"entry points"**; 
it should be used within a Python program.)

* Import the pyRestTable package
* Create the :class:`~Table` instance
* Set the list of column labels (either ``labels.append()`` or :func:`~.addLabel`)
* Append the list of column cells for each row
  (either ``rows.append([])`` or :func:`~.addRow`)
* Render the table with :func:`.reST` (default table format is ``simple``)

For a simple key:value dictionary, use :func:`pyRestTable.kv_table`::

    import pyRestTable

    table = pyRestTable.kv_table({"a": 1, "b": "bb"})
    print(table.reST())

Examples are provided to demonstrate usage.

.. [#] http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html
