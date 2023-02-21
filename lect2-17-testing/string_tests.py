import unittest
from unittest.mock import patch
import testing

class TestingStringMethod(unittest.TestCase):
    def testSwap(self):
        swapped = testing.stringSwap("This is a sentence here")
        self.assertEqual(
            swapped, 
            "here is a sentence This"
        )
        self.assertFalse(
           swapped == "This is a sentence here"
        )


    @patch('testing.get_joke')
    def testJoke(self, getjoke):
        ret_val = "Strings"
        getjoke.return_value = ret_val
        self.assertEqual(testing.len_joke(), len(ret_val))

if __name__ == '__main__':
    unittest.main()