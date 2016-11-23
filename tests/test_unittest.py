
'''
unit testing of pyRestTable package
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


if __name__ == '__main__':
    unittest.main()
