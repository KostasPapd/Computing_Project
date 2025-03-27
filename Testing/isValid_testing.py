"""
This file will be used to test the isValid file using unittesting
"""
import unittest
import isValid


class Validate_isValid(unittest.TestCase):
    def testPassword(self):
        data = ""
        result = isValid.validatePassword(data)
        expected = False # or True depending on the test
        print(result, expected)
        self.assertEqual(expected, result)

    def testEmail(self):
        data = ""
        result = isValid.validEmail(data)
        expected = False # or True depending on the test
        print(result, expected)
        self.assertEqual(expected, result)

    def testVerifyEmail(self):
        data = ""
        result = isValid.verifyEmail(data)
        expected = False # or True depending on the test
        print(result, expected)
        self.assertEqual(expected, result)

if __name__ == "__main__":
    unittest.main()
