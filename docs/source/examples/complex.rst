Complex table example
*********************

These commands::

    import pyRestTable
    t = pyRestTable.Table()
    t.labels = ('Name\nand\nAttributes', 'Type', 'Units', 'Description\n(and Occurrences)', )
    t.rows.append( ['one,\ntwo', "buckle my", "shoe.\n\n\nthree,\nfour", "..."] )
    t.rows.append( ['class', 'NX_FLOAT', '..', '..', ] )
    t.rows.append( range(0,4) )
    t.rows.append( [None, t, 1.234, range(3)] )
    print t.reST(fmt='complex')

build this table source code::

    +------------+-----------------------------------------+--------+-------------------+
    | Name       | Type                                    | Units  | Description       |
    | and        |                                         |        | (and Occurrences) |
    | Attributes |                                         |        |                   |
    +============+=========================================+========+===================+
    | one,       | buckle my                               | shoe.  | ...               |
    | two        |                                         |        |                   |
    |            |                                         |        |                   |
    |            |                                         | three, |                   |
    |            |                                         | four   |                   |
    +------------+-----------------------------------------+--------+-------------------+
    | class      | NX_FLOAT                                | ..     | ..                |
    +------------+-----------------------------------------+--------+-------------------+
    | 0          | 1                                       | 2      | 3                 |
    +------------+-----------------------------------------+--------+-------------------+
    | None       | <__main__.Table instance at 0x022B8EE0> | 1.234  | [0, 1, 2]         |
    +------------+-----------------------------------------+--------+-------------------+
