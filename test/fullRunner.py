"""
Run all the core unit tests, not the lengthy and major integration tests
"""
import unittest
import sys
sys.path.append('test') # Allows this runner to be run from the main directory

import test_something

loader = unittest.TestLoader()
suite = unittest.TestSuite()
suite.addTests(loader.loadTestsFromModule(test_something))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)

numberFailures = len(result.errors)
numberErrors= len(result.failures)
numberIssues = numberFailures + numberErrors

sys.exit(numberIssues)
