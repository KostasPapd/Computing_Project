"""
This file will be used to test the isValid file using unittesting
"""
import unittest
import isValid


class Validate_isValid(unittest.TestCase):
    def testPassword(self):
        data = ""
        result = isValid.validatePassword(data)
        expected = False
        print(result, expected)
        self.assertEqual(expected, result)

    def testEmail(self):
        data = "b32908@uk"
        result = isValid.validEmail(data)
        expected = False
        print(result, expected)
        self.assertEqual(expected, result)

    def testVerifyEmail(self):
        data = "b32908@uk"
        result = isValid.verifyEmail(data)
        expected = False
        print(result, expected)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
