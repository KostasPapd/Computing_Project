"""
Unittest website: https://www.geeksforgeeks.org/unit-testing-python-unittest/
"""

import unittest
from isValid import *

class Test(unittest.TestCase):
    def test_email(self):
        self.assertTrue(validEmail("ojojbho@jgvu.com"))
    def test_password(self):
        self.assertTrue(validatePassword("12!bbHhhhs"), True)


if __name__ == "__main__":
    unittest.main()
