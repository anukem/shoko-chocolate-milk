
import unittest

class EmailTestCase(unittest.TestCase):

    def test_invalid_email(self):

        #self.assertTrue(True)
        self.assertFalse(checkEmail("sdkjdslfajkl"))


    def test_valid_email(self):

        self.assertTrue(checkEmail("sk4@columbia.edu"))


if __name__ == '__main__':
    unittest.main()
