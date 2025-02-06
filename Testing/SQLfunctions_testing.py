import unittest
import SQLfunctions

class Validate_SQLfunctions(unittest.TestCase):
    def testCheckEmail(self):
        data = "kostispapd@gmail.com"
        result = SQLfunctions.checkEmail(data)
        expected = True
        self.assertEqual(expected, result)

    def testCheckLogIn(self):
        user = "randomemail@outlook.com"
        password = "UnittestPassword"
        result = SQLfunctions.checkLogIn(user, password)
        expected = None
        self.assertEqual(expected, result)


    """
    getStudents
    getClass
    getAssignName
    checkType
    checkAssignmentNumber
    getIDs
    getLast
    getAnsw
    deleteClass
    """


if __name__ == "__main__":
    unittest.main()
