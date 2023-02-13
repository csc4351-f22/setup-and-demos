import unittest
import testing

class TestingStringMethod(unittest.TestCase):
    def testSwap(self):
        self.assertEquals("here is a sentence This", testing.stringSwap("This is a sentence here"))
        self.assertFalse(testing.stringSwap("This is a sentence here") == "This is a sentence here")


if __name__ == '__main__':
    unittest.main()