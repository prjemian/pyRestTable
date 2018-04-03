
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

MINIMAL_PLAIN_RESULT = '''\
x y
1 2
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

MINIMAL_HTML_RESULT = '''\
<table>
  <tr>
    <th>x</th>
    <th>y</th>
  </tr>
  <tr>
    <td>1</td>
    <td>2</td>
  </tr>
</table>\
'''


EXAMPLE_MINIMAL_RESULT = MINIMAL_PLAIN_RESULT + '\n'
EXAMPLE_MINIMAL_RESULT += MINIMAL_SIMPLE_RESULT + '\n'
EXAMPLE_MINIMAL_RESULT += MINIMAL_GRID_RESULT + '\n'
EXAMPLE_MINIMAL_RESULT += MINIMAL_LISTTABLE_RESULT + '\n'
EXAMPLE_MINIMAL_RESULT += MINIMAL_HTML_RESULT


EXAMPLE_BASIC_RESULT = '''\
one two three
1,1 1,2 1,3  
2,1 2,2 2,3  
3,1 3,2 3,3  
4,1 4,2 4,3  

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
     - 4,3
\
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
</table>\
'''


EXAMPLE_COMPLICATED_RESULT = '''
.. tabularcolumns:: |l|L|c|r|
    :longtable:

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
'''.strip()


class Test_pyRestTable(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def apply_test(self, table, reference_text, style='simple'):
        text = table.reST(fmt=style)
        self.assertTrue(text.strip() == reference_text.strip())
    
    def population_table(self):
        t = pyRestTable.Table()
        t.addLabel('City name')
        t.addLabel('Area')
        t.addLabel('Population')
        t.addLabel('Annual Rainfall')
        t.addRow(['Adelaide',  1295, 1158259,    600.5])
        t.addRow(['Brisbane',  5905, 1857594,    1146.4])
        t.addRow(['Darwin',    112,  120900,     1714.7])
        return t

    def test_simple(self):
        s = self.population_table().reST(fmt = 'simple')
        expected  = '========= ==== ========== ===============\n'
        expected += 'City name Area Population Annual Rainfall\n'
        expected += '========= ==== ========== ===============\n'
        expected += 'Adelaide  1295 1158259    600.5          \n'
        expected += 'Brisbane  5905 1857594    1146.4         \n'
        expected += 'Darwin    112  120900     1714.7         \n'
        expected += '========= ==== ========== ===============\n'
        self.assertEqual(s, expected)

    def test_plain(self):
        s = self.population_table().reST(fmt = 'plain')
        expected  = 'City name Area Population Annual Rainfall\n'
        expected += 'Adelaide  1295 1158259    600.5          \n'
        expected += 'Brisbane  5905 1857594    1146.4         \n'
        expected += 'Darwin    112  120900     1714.7         \n'
        self.assertEqual(s, expected)

    def test_grid(self):
        s = self.population_table().reST(fmt = 'grid')
        expected  = '+-----------+------+------------+-----------------+\n'
        expected += '| City name | Area | Population | Annual Rainfall |\n'
        expected += '+===========+======+============+=================+\n'
        expected += '| Adelaide  | 1295 | 1158259    | 600.5           |\n'
        expected += '+-----------+------+------------+-----------------+\n'
        expected += '| Brisbane  | 5905 | 1857594    | 1146.4          |\n'
        expected += '+-----------+------+------------+-----------------+\n'
        expected += '| Darwin    | 112  | 120900     | 1714.7          |\n'
        expected += '+-----------+------+------------+-----------------+\n'
        self.assertEqual(s, expected)

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

    def test_minimal_htmltable(self):
        table = pyRestTable.rest_table.example_minimal()
        self.apply_test(table, MINIMAL_HTML_RESULT, 'html')

    def test_example_basic(self):
        t = pyRestTable.rest_table.example_basic()
        s = pyRestTable.rest_table._prepare_results_(t)
        self.assertEqual(s.strip(), EXAMPLE_BASIC_RESULT.strip())

    def test_example_complicated(self):
        t = pyRestTable.rest_table.example_complicated()
        s = t.reST(fmt='grid').strip()
        self.assertEqual(s, EXAMPLE_COMPLICATED_RESULT)

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

    def test_default_str(self):
        t = pyRestTable.rest_table.example_minimal()
        s = str(t)
        self.assertEqual(s, MINIMAL_SIMPLE_RESULT, 'string representation')


def suite(*args, **kw):
    test_suite = unittest.TestSuite()
    test_list = [
        Test_pyRestTable,
        ]
    for test_case in test_list:
        test_suite.addTest(unittest.makeSuite(test_case))
    return test_suite


if __name__ == "__main__":
    runner=unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
