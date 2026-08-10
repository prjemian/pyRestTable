*html*
######

:see: https://www.w3schools.com/html/html_tables.asp

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
    print(t.reST(fmt='html'))

build this table in HTML source code:

.. code-block:: guess
   :linenos:
   
   <table>
     <tr>
       <th>one</th>
       <th>two</th>
       <th>three</th>
     </tr>
     <tr>
       <td>1,1</td>
       <td>1,2</td>
       <td>1,3</td>
     </tr>
     <tr>
       <td>2,1</td>
       <td>2,2</td>
       <td>2,3</td>
     </tr>
     <tr>
       <td>3,1</td>
       <td>3,2</td>
       <td>3,3</td>
     </tr>
     <tr>
       <td>4,1</td>
       <td>4,2</td>
       <td>4,3</td>
     </tr>
   </table>
