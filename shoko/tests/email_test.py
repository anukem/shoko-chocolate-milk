
import unittest
import sys
sys.path.insert(0, "..\\code")

from validate_email import checkEmail

class EmailTestCase(unittest.TestCase):

    def test_invalid_email(self):
        self.assertFalse(checkEmail("sdkjdslfajkl"))


    def test_valid_email(self):
        self.assertTrue(checkEmail("sk4@columbia.edu"))


if __name__ == '__main__':
    unittest.main()
