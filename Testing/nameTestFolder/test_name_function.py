import unittest
from name_function import formatted_name

class NamesTestCase(unittest.TestCase):

   def test_first_last_name(self):
       result = formatted_name("pete", "seeger")
       self.assertEqual(result, "Pete Seeger")
   # another method id added for another test (middle name)
   def test_first_last_middle_name(self):
        result = formatted_name("raymond", "reddington", "red")
        self.assertEqual(result, "Raymond Red Reddington")
       

if __name__== '__main__':
   unittest.main()
