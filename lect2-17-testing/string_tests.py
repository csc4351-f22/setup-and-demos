import unittest
from unittest.mock import patch
import testing

class TestingStringMethod(unittest.TestCase):
    def testSwap(self):
        self.assertEquals("here is a sentence This", testing.stringSwap("This is a sentence here"))
        self.assertFalse(testing.stringSwap("This is a sentence here") == "This is a sentence here")

    @patch('testing.get_joke')
    def testJoke(self, make_joke):
        make_joke.return_value = "One"
        self.assertEquals(testing.len_joke(), 3)

if __name__ == '__main__':
    unittest.main()