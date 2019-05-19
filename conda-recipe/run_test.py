#!/usr/bin/env python

import pyRestTable

t = pyRestTable.Table()
t.addLabel('City name')
t.addLabel('Area')
t.addLabel('Population')
t.addLabel('Annual Rainfall')
t.addRow(['Adelaide',  1295, 1158259,    600.5])
t.addRow(['Brisbane',  5905, 1857594,    1146.4])
t.addRow(['Darwin',    112,  120900,     1714.7])
expected  = '========= ==== ========== ===============\n'
expected += 'City name Area Population Annual Rainfall\n'
expected += '========= ==== ========== ===============\n'
expected += 'Adelaide  1295 1158259    600.5          \n'
expected += 'Brisbane  5905 1857594    1146.4         \n'
expected += 'Darwin    112  120900     1714.7         \n'
expected += '========= ==== ========== ===============\n'
assert(str(t) == expected)
