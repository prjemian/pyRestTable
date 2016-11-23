
'''
test output results of pyRestTable package
'''

import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
import pyRestTable.rest_table


SIMPLE_RESULT = '''\
=== === =====
one two three
=== === =====
1,1 1,2 1,3  
2,1 2,2 2,3  
3,1 3,2 3,3  
4,1 4,2 4,3  
=== === =====
'''

CANSAS_RESULT = '''\
+-----------+--------------------------------------+--------------+
| SASentry  | description                          | measurements |
+===========+======================================+==============+
| AF1410:10 | AF1410-10 (AF1410 steel aged 10 h)   | 2            |
+-----------+--------------------------------------+--------------+
| AF1410:8h | AF1410-8h (AF1410 steel aged 8 h)    | 2            |
+-----------+--------------------------------------+--------------+
| AF1410:qu | AF1410-qu (AF1410 steel aged 0.25 h) | 2            |
+-----------+--------------------------------------+--------------+
| AF1410:cc | AF1410-cc (AF1410 steel aged 100 h)  | 2            |
+-----------+--------------------------------------+--------------+
| AF1410:2h | AF1410-2h (AF1410 steel aged 2 h)    | 2            |
+-----------+--------------------------------------+--------------+
| AF1410:50 | AF1410-50 (AF1410 steel aged 50 h)   | 2            |
+-----------+--------------------------------------+--------------+
| AF1410:20 | AF1410-20 (AF1410 steel aged 20 h)   | 1            |
+-----------+--------------------------------------+--------------+
| AF1410:5h | AF1410-5h (AF1410 steel aged 5 h)    | 2            |
+-----------+--------------------------------------+--------------+
| AF1410:1h | AF1410-1h (AF1410 steel aged 1 h)    | 2            |
+-----------+--------------------------------------+--------------+
| AF1410:hf | AF1410-hf (AF1410 steel aged 0.5 h)  | 2            |
+-----------+--------------------------------------+--------------+
'''

MINIMAL_SIMPLE_RESULT = '''\
= =
x y
= =
1 2
= =
'''

MINIMAL_GRID_RESULT = '''\
+---+---+
| x | y |
+===+===+
| 1 | 2 |
+---+---+
'''

MINIMAL_LISTTABLE_RESULT = '''\
.. list-table:: 
   :header-rows: 1
   :widths: 1 1

   * - x
     - y
   * - 1
     - 2\
'''


EXAMPLE_MINIMAL_RESULT = MINIMAL_SIMPLE_RESULT
EXAMPLE_MINIMAL_RESULT += '\n'
EXAMPLE_MINIMAL_RESULT += MINIMAL_GRID_RESULT
EXAMPLE_MINIMAL_RESULT += '\n'
EXAMPLE_MINIMAL_RESULT += MINIMAL_LISTTABLE_RESULT


EXAMPLE_BASIC_RESULT = '''\
=== === =====
one two three
=== === =====
1,1 1,2 1,3  
2,1 2,2 2,3  
3,1 3,2 3,3  
4,1 4,2 4,3  
=== === =====

+-----+-----+-------+
| one | two | three |
+=====+=====+=======+
| 1,1 | 1,2 | 1,3   |
+-----+-----+-------+
| 2,1 | 2,2 | 2,3   |
+-----+-----+-------+
| 3,1 | 3,2 | 3,3   |
+-----+-----+-------+
| 4,1 | 4,2 | 4,3   |
+-----+-----+-------+

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
     - 4,3'''


EXAMPLE_COMPLICATED_RESULT = '.. tabularcolumns:: |l|L|c|r|\n    :longtable:\n\n========== ========================================================= ====== =================\nName       Type                                                      Units  Description      \nand                                                                         (and Occurrences)\nAttributes                                                                                   \n========== ========================================================= ====== =================\none,       buckle my                                                 shoe.  ...              \ntwo                                                                                          \n                                                                                             \n                                                                     three,                  \n                                                                     four                    \nclass      NX_FLOAT                                                         None             \n0          1                                                         2      3                \nNone       <pyRestTable.rest_table.Table instance at 0x7f7401d2bcf8> 1.234  [0, 1, 2]        \n========== ========================================================= ====== =================\n\n.. tabularcolumns:: |l|L|c|r|\n    :longtable:\n\n+------------+-----------------------------------------------------------+--------+-------------------+\n| Name       | Type                                                      | Units  | Description       |\n| and        |                                                           |        | (and Occurrences) |\n| Attributes |                                                           |        |                   |\n+============+===========================================================+========+===================+\n| one,       | buckle my                                                 | shoe.  | ...               |\n| two        |                                                           |        |                   |\n|            |                                                           |        |                   |\n|            |                                                           | three, |                   |\n|            |                                                           | four   |                   |\n+------------+-----------------------------------------------------------+--------+-------------------+\n| class      | NX_FLOAT                                                  |        | None              |\n+------------+-----------------------------------------------------------+--------+-------------------+\n| 0          | 1                                                         | 2      | 3                 |\n+------------+-----------------------------------------------------------+--------+-------------------+\n| None       | <pyRestTable.rest_table.Table instance at 0x7f7401d2bcf8> | 1.234  | [0, 1, 2]         |\n+------------+-----------------------------------------------------------+--------+-------------------+\n\n.. list-table:: \n   :header-rows: 1\n   :widths: 10 57 6 17\n\n   * - Name\n       and\n       Attributes\n     - Type\n     - Units\n     - Description\n       (and Occurrences)\n   * - one,\n       two\n     - buckle my\n     - shoe.\n       \n       \n       three,\n       four\n     - ...\n   * - class\n     - NX_FLOAT\n     - \n     - \n   * - 0\n     - 1\n     - 2\n     - 3\n   * - None\n     - <pyRestTable.rest_table.Table instance at 0x7f7401d2bcf8>\n     - 1.234\n     - [0, 1, 2]'


class TestUM(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def apply_test(self, table, reference_text, style='simple'):
        text = table.reST(fmt=style)
        self.assertTrue(text == reference_text)

    def test_simple(self):
        import pyRestTable.simple
        self.apply_test(pyRestTable.simple.main(), SIMPLE_RESULT)

    def test_cansas(self):
        import pyRestTable.cansas
        self.apply_test(pyRestTable.cansas.main(), CANSAS_RESULT, 'complex')

    def test_minimal_simple(self):
        self.apply_test(pyRestTable.rest_table.example_minimal(), MINIMAL_SIMPLE_RESULT)

    def test_minimal_complex(self):
        self.apply_test(pyRestTable.rest_table.example_minimal(), MINIMAL_GRID_RESULT, 'complex')

    def test_minimal_grid(self):
        self.apply_test(pyRestTable.rest_table.example_minimal(), MINIMAL_GRID_RESULT, 'grid')

    def test_minimal_listtable(self):
        self.apply_test(pyRestTable.rest_table.example_minimal(), MINIMAL_LISTTABLE_RESULT, 'list-table')

    def test_example_basic(self):
        t = pyRestTable.rest_table.example_basic()
        s = pyRestTable.rest_table._prepare_results_(t)
        self.assertEqual(s, EXAMPLE_BASIC_RESULT)

    def test_example_complicated(self):
        t = pyRestTable.rest_table.example_complicated()
        s = pyRestTable.rest_table._prepare_results_(t)
        self.assertNotEqual(s, EXAMPLE_COMPLICATED_RESULT)

    def test_example_minimal(self):
        t = pyRestTable.rest_table.example_minimal()
        s = pyRestTable.rest_table._prepare_results_(t)
        self.assertEqual(s, EXAMPLE_MINIMAL_RESULT)

    def test_zero_width_column(self):
        t = pyRestTable.rest_table.Table()
        t.labels = ('', 'two', )
        t.rows.append( ['', '1,2',] )
        t.rows.append( ['', '2,2',] )
        s = t.reST(fmt='simple')
        expected = ' ===\n'
        expected += ' two\n'
        expected += ' ===\n'
        expected += ' 1,2\n'
        expected += ' 2,2\n'
        expected += ' ===\n'
        self.assertEqual(s, expected)

    def test_zero_columns(self):
        t = pyRestTable.rest_table.Table()
        t.labels = ()
        t.rows.append( [] )
        t.rows.append( [] )
        s = t.reST(fmt='simple')
        expected = '\n\n\n'
        self.assertEqual(s, expected)

    def test_num_col_labels_different_from_col_width_specifiers(self):
        # Number of column labels is different from column width specifiers
        t = pyRestTable.rest_table.Table()
        t.use_tabular_columns = True
        t.alignment = 'lll'
        t.longtable = True
        t.labels = ('one', 'two', )
        t.rows.append( ['1,1', '1,2',] )
        t.rows.append( ['2,1', '2,2',] )
        self.assertRaises(IndexError, t.reST, fmt='list-table')
        
        # now fix and proceed
        t.alignment = 'll'
        s = t.reST(fmt='list-table')
        expected = ''
        expected += '.. list-table:: \n'
        expected += '   :header-rows: 1\n'
        expected += '   :widths: 3 3\n'
        expected += '\n'
        expected += '   * - one\n'
        expected += '     - two\n'
        expected += '   * - 1,1\n'
        expected += '     - 1,2\n'
        expected += '   * - 2,1\n'
        expected += '     - 2,2'
        self.assertEqual(s, expected)


if __name__ == '__main__':
    unittest.main()
