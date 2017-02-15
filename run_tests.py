
'''
test output results of pyRestTable package
'''

import unittest
import tests.test_results


if __name__ == "__main__":
    runner=unittest.TextTestRunner(verbosity=2)
    runner.run(tests.test_results.suite())
