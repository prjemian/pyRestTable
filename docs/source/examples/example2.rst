Complicated example
###################

These commands setup the table::

   import pyRestTable
   t = pyRestTable.Table()
   t.labels = ('Name\nand\nAttributes', 'Type', 'Units', 'Description\n(and Occurrences)', )
   t.rows.append( ['one,\ntwo', "buckle my", "shoe.\n\n\nthree,\nfour", "..."] )
   t.rows.append( ['class', 'NX_FLOAT', '..', '..', ] )
   t.rows.append( range(0,4) )
   t.rows.append( [None, t, 1.234, range(3)] )
   t.longtable = True
   t.use_tabular_columns = True
   t.alignment = 'l L c r'.split()

Here, we assert more control over the column widths using *longtable*,
*use_tabular_columns*, and *alignment* configuration options.

Format: `print t.reST(fmt='simple')`
------------------------------------

this reST code::

   .. tabularcolumns:: |l|L|c|r|
       :longtable:
   
   ========== =============================================== ====== =================
   Name       Type                                            Units  Description      
   and                                                               (and Occurrences)
   Attributes                                                                         
   ========== =============================================== ====== =================
   one,       buckle my                                       shoe.  ...              
   two                                                                                
                                                                                      
                                                              three,                  
                                                              four                    
   class      NX_FLOAT                                               None             
   0          1                                               2      3                
   None       <__main__.Table instance at 0x0000000001F95D08> 1.234  [0, 1, 2]        
   ========== =============================================== ====== =================

is rendered as:

.. tabularcolumns:: |l|L|c|r|
    :longtable:

========== =============================================== ====== =================
Name       Type                                            Units  Description      
and                                                               (and Occurrences)
Attributes                                                                         
========== =============================================== ====== =================
one,       buckle my                                       shoe.  ...              
two                                                                                
                                                                                   
                                                           three,                  
                                                           four                    
class      NX_FLOAT                                               None             
0          1                                               2      3                
None       <__main__.Table instance at 0x0000000001F95D08> 1.234  [0, 1, 2]        
========== =============================================== ====== =================

Format: `print t.reST(fmt='grid')`
----------------------------------

this reST code::

   .. tabularcolumns:: |l|L|c|r|
       :longtable:
   
   +------------+-------------------------------------------------+--------+-------------------+
   | Name       | Type                                            | Units  | Description       |
   | and        |                                                 |        | (and Occurrences) |
   | Attributes |                                                 |        |                   |
   +============+=================================================+========+===================+
   | one,       | buckle my                                       | shoe.  | ...               |
   | two        |                                                 |        |                   |
   |            |                                                 |        |                   |
   |            |                                                 | three, |                   |
   |            |                                                 | four   |                   |
   +------------+-------------------------------------------------+--------+-------------------+
   | class      | NX_FLOAT                                        |        | None              |
   +------------+-------------------------------------------------+--------+-------------------+
   | 0          | 1                                               | 2      | 3                 |
   +------------+-------------------------------------------------+--------+-------------------+
   | None       | <__main__.Table instance at 0x0000000001F95D08> | 1.234  | [0, 1, 2]         |
   +------------+-------------------------------------------------+--------+-------------------+

is rendered as:

.. tabularcolumns:: |l|L|c|r|
    :longtable:

+------------+-------------------------------------------------+--------+-------------------+
| Name       | Type                                            | Units  | Description       |
| and        |                                                 |        | (and Occurrences) |
| Attributes |                                                 |        |                   |
+============+=================================================+========+===================+
| one,       | buckle my                                       | shoe.  | ...               |
| two        |                                                 |        |                   |
|            |                                                 |        |                   |
|            |                                                 | three, |                   |
|            |                                                 | four   |                   |
+------------+-------------------------------------------------+--------+-------------------+
| class      | NX_FLOAT                                        |        | None              |
+------------+-------------------------------------------------+--------+-------------------+
| 0          | 1                                               | 2      | 3                 |
+------------+-------------------------------------------------+--------+-------------------+
| None       | <__main__.Table instance at 0x0000000001F95D08> | 1.234  | [0, 1, 2]         |
+------------+-------------------------------------------------+--------+-------------------+


Format: `print t.reST(fmt='list-table')`
----------------------------------------

this reST code::

   .. list-table:: 
      :header-rows: 1
      :widths: 10 47 6 17
   
      * - Name
          and
          Attributes
        - Type
        - Units
        - Description
          (and Occurrences)
      * - one,
          two
        - buckle my
        - shoe.
          
          
          three,
          four
        - ...
      * - class
        - NX_FLOAT
        - 
        - 
      * - 0
        - 1
        - 2
        - 3
      * - None
        - <__main__.Table instance at 0x0000000001F15C08>
        - 1.234
        - [0, 1, 2]

is rendered as:

.. list-table:: 
   :header-rows: 1
   :widths: 10 47 6 17

   * - Name
       and
       Attributes
     - Type
     - Units
     - Description
       (and Occurrences)
   * - one,
       two
     - buckle my
     - shoe.
       
       
       three,
       four
     - ...
   * - class
     - NX_FLOAT
     - 
     - 
   * - 0
     - 1
     - 2
     - 3
   * - None
     - <__main__.Table instance at 0x0000000001F15C08>
     - 1.234
     - [0, 1, 2]

