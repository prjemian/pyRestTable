
'''
unit testing of pyRestTable package
'''

import sys
import unittest

sys.path.insert(0, '..')
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

    def test_simple(self):
        import pyRestTable.simple
        table = pyRestTable.simple.main()
        self.assertTrue(table.reST() == SIMPLE_RESULT)

    def test_cansas(self):
        import pyRestTable.cansas
        table = pyRestTable.cansas.main()
        self.assertTrue(table.reST(fmt='complex') == CANSAS_RESULT)

    def test_minimal_simple(self):
        table = pyRestTable.rest_table.example_minimal()
        self.assertTrue(table.reST(fmt='simple') == MINIMAL_SIMPLE_RESULT)

    def test_minimal_grid(self):
        table = pyRestTable.rest_table.example_minimal()
        self.assertTrue(table.reST(fmt='grid') == MINIMAL_GRID_RESULT)

    def test_minimal_listtable(self):
        table = pyRestTable.rest_table.example_minimal()
        self.assertTrue(table.reST(fmt='list-table') == MINIMAL_LISTTABLE_RESULT)


if __name__ == '__main__':
    unittest.main()
