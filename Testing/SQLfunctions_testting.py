import unittest
import SQLfunctions

class Validate_SQLfunctions(unittest.TestCase):
    def testCheckEmail(self):
        data = "kostispapd@outlook.com"
        result = SQLfunctions.checkEmail(data)
        expected = False
        self.assertEqual(expected, result)

    def testCheckLogIn(self):
        user = "admin_kostas"
        password = "UnittestPassword"
        result = SQLfunctions.checkLogIn(user, password)
        expected = None
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
