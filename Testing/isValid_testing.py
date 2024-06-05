"""
This file will be used to test the isValid file using unittesting
"""
import unittest
import isValid


class Validate_isValid(unittest.TestCase):
    def testPassword(self):
        data = "passwA!or33345"
        result = isValid.validatePassword(data)    # call the function you want to test
        expected = True
        print(result, expected)
        self.assertEqual(expected, result)

    def testEmail(self):
        data = "b32908@sfc.potteries.ac.uk"
        result = isValid.validEmail(data)
        expected = True
        print(result, expected)
        self.assertEqual(expected, result)

    def testVerifyEmail(self):
        data = "b32908@sfc.potteries.ac.uk"
        result = isValid.verifyEmail(data)
        expected = True
        print(result, expected)
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
