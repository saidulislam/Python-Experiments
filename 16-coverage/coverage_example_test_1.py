import coverage_example_1
import unittest

class TestAdd(unittest.TestCase):
    """
    Test the add function from the mymath library
    """

    def test_add_integers(self):
        """
        Test that the addition of two integers returns the correct total
        """
        result = coverage_example_1.add(1, 2)
        self.assertEqual(result, 3)

    def test_add_floats(self):
        """
        Test that the addition of two floats returns the correct result
        """
        result = coverage_example_1.add(10.5, 2)
        self.assertEqual(result, 12.5)

    def test_add_strings(self):
        """
        Test the addition of two strings returns the two string as one
        concatenated string
        """
        result = coverage_example_1.add('abc', 'def')
        self.assertEqual(result, 'abcdef')

class TestSubtract(unittest.TestCase):
    """
    Test the subtract function from the mymath library
    """

    def test_subtract_integers(self):
        """
        Test that subtracting integers returns the correct result
        """
        result = coverage_example_1.subtract(10, 8)
        self.assertEqual(result, 2)


class TestMultiply(unittest.TestCase):
    """
    Test the multiply function from the mymath library
    """

    def test_subtract_integers(self):
        """
        Test that multiplying integers returns the correct result
        """
        result = coverage_example_1.multiply(5, 50)
        self.assertEqual(result, 250)


class TestDivide(unittest.TestCase):
    """
    Test the divide function from the mymath library
    """

    def test_divide_by_zero(self):
        """
        Test that multiplying integers returns the correct result
        """
        with self.assertRaises(ZeroDivisionError):
            result = coverage_example_1.divide(8, 0)


if __name__ == '__main__':
    unittest.main()

    # to check coverage
    # pip install coverage
    # execute the following
    # coverage run coverage_example_test_1.py
    # to get the report, run the following
    # coverage report -m
    # to create an html file of the report, execute the following
    # coverage html