import simple_example_1
import sys
import unittest

class TestAdd(unittest.TestCase):
    """
    Test the add function from the mymath module
    """

    def test_add_integers(self):
        """
        Test that the addition of two integers returns the correct total
        """
        result = simple_example_1.add(1, 2)
        self.assertEqual(result, 3)

    def test_add_floats(self):
        """
        Test that the addition of two floats returns the correct result
        """
        result = simple_example_1.add(10.5, 2)
        self.assertEqual(result, 12.5)

    @unittest.skip('Skip this test')
    def test_add_strings(self):
        """
        Test the addition of two strings returns the two string as one
        concatenated string
        """
        result = simple_example_1.add('abc', 'def')
        self.assertEqual(result, 'abcdef')

    # The skipUnless decorator will skip a test unless the condition returns 
    # True. So if you run this test on Mac or Linux, it will get skipped. 
    # There is also a skipIf decorator that will skip a test if the condition 
    # is True.
    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_adding_on_windows(self):
        result = simple_example_1.add(1, 2)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()

    # you can also execute the following
    # $ python -m unittest skip_test_example_1.py -v