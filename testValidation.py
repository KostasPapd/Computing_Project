import unittest
from isValid import *

class Test(unittest.TestCase):
    def test_email(self):
        self.assert_(validEmail("ojojbho@jgvu.com"),True)


if __name__ == "__main__":
    unittest.main()
