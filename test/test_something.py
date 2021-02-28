import unittest
import numpy as np
from numpy.testing import assert_equal, assert_allclose

class TestSomething(unittest.TestCase):
    def setUp(self):
        pass # Set up to be run before every test case

    @classmethod
    def setUpClass(cls):
        pass # Set up to be run once at the beginning 

    def testSomething(self):
        """
        Tests that something is OK.
        """
        actual_number = 1.0
        desired_number = 1.0
        assert_equal(actual_number, desired_number)

    def tearDown(self):
        pass # Tear down to be run after every test case

    @classmethod
    def tearDownClass(self):
        pass # Tear down to be run after entire script
