Complicated example
###################

These python commands setup the table:

.. code-block:: python
    :linenos:

    import pyRestTable
    t = pyRestTable.Table()
    t.addLabel('Name\nand\nAttributes')
    t.addLabel('Type')
    t.addLabel('Units')
    t.addLabel('Description\n(and Occurrences)')
    t.addRow( ['one,\ntwo', "buckle my", "shoe.\n\n\nthree,\nfour", "..."] )
    t.addRow( ['class', 'NX_FLOAT', '', None, ] )
    t.addRow( range(0,4) )
    t.addRow( [None, {'a': 1, 'b': 'dreamy'}, 1.234, range(3)] )

Format: `print(t.reST(fmt='simple'))`
-------------------------------------

this reST code:

.. code-block:: guess
   :linenos:
   
   ========== ======================= ====== =================
   Name       Type                    Units  Description      
   and                                       (and Occurrences)
   Attributes                                                 
   ========== ======================= ====== =================
   one,       buckle my               shoe.  ...              
   two                                                        
                                                              
                                      three,                  
                                      four                    
   class      NX_FLOAT                       None             
   0          1                       2      3                
   None       {'a': 1, 'b': 'dreamy'} 1.234  [0, 1, 2]        
   ========== ======================= ====== =================

is rendered as:

========== ======================= ====== =================
Name       Type                    Units  Description      
and                                       (and Occurrences)
Attributes                                                 
========== ======================= ====== =================
one,       buckle my               shoe.  ...              
two                                                        
                                                           
                                   three,                  
                                   four                    
class      NX_FLOAT                       None             
0          1                       2      3                
None       {'a': 1, 'b': 'dreamy'} 1.234  [0, 1, 2]        
========== ======================= ====== =================

Format: `print(t.reST(fmt='grid'))`
-----------------------------------

this reST code:

.. code-block:: guess
   :linenos:
   
   +------------+-------------------------+--------+-------------------+
   | Name       | Type                    | Units  | Description       |
   | and        |                         |        | (and Occurrences) |
   | Attributes |                         |        |                   |
   +============+=========================+========+===================+
   | one,       | buckle my               | shoe.  | ...               |
   | two        |                         |        |                   |
   |            |                         |        |                   |
   |            |                         | three, |                   |
   |            |                         | four   |                   |
   +------------+-------------------------+--------+-------------------+
   | class      | NX_FLOAT                |        | None              |
   +------------+-------------------------+--------+-------------------+
   | 0          | 1                       | 2      | 3                 |
   +------------+-------------------------+--------+-------------------+
   | None       | {'a': 1, 'b': 'dreamy'} | 1.234  | [0, 1, 2]         |
   +------------+-------------------------+--------+-------------------+

is rendered as:

+------------+-------------------------+--------+-------------------+
| Name       | Type                    | Units  | Description       |
| and        |                         |        | (and Occurrences) |
| Attributes |                         |        |                   |
+============+=========================+========+===================+
| one,       | buckle my               | shoe.  | ...               |
| two        |                         |        |                   |
|            |                         |        |                   |
|            |                         | three, |                   |
|            |                         | four   |                   |
+------------+-------------------------+--------+-------------------+
| class      | NX_FLOAT                |        | None              |
+------------+-------------------------+--------+-------------------+
| 0          | 1                       | 2      | 3                 |
+------------+-------------------------+--------+-------------------+
| None       | {'a': 1, 'b': 'dreamy'} | 1.234  | [0, 1, 2]         |
+------------+-------------------------+--------+-------------------+


Format: `print(t.reST(fmt='list-table'))`
-----------------------------------------

this reST code:

.. code-block:: guess
   :linenos:
   
   .. list-table:: 
      :header-rows: 1
      :widths: 10 23 6 17
   
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
        - {'a': 1, 'b': 'dreamy'}
        - 1.234
        - [0, 1, 2]

is rendered as:

.. list-table:: 
   :header-rows: 1
   :widths: 10 23 6 17

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
     - {'a': 1, 'b': 'dreamy'}
     - 1.234
     - [0, 1, 2]
