import unittest
from unittest.mock import patch
from io import StringIO

def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for i in my_list:
        print("{:d}".format(i))

class TestPrintReversed(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def assert_stdout(self, expected_output, args, mock_stdout):
        print_reversed_list_integer(args)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_empty_list(self):
        self.assert_stdout('', [])

    def test_single_element(self):
        self.assert_stdout('1\n', [1])

    def test_multiple_elements(self):
        self.assert_stdout('3\n2\n1\n', [1, 2, 3])

    def test_negative_numbers(self):
        self.assert_stdout('-1\n-2\n-3\n', [-3, -2, -1])

    def test_zero(self):
        self.assert_stdout('0\n', [0])

    def test_large_numbers(self):
        self.assert_stdout('1000000000\n999999999\n', [999999999, 1000000000])

    def test_large_list(self):
        large_list = list(range(1000000))  # A list with 1 million elements
        expected_output = '\n'.join(map(str, reversed(large_list))) + '\n'
        self.assert_stdout(expected_output, large_list)

    def test_large_numbers(self):
        large_numbers = [10**18, 10**18 + 1]  # Very large numbers
        self.assert_stdout('1000000000000000001\n1000000000000000000\n', large_numbers)

    def test_small_numbers(self):
        small_numbers = [-10**18, -10**18 - 1]  # Very small numbers
        self.assert_stdout('-1000000000000000001\n-1000000000000000000\n', small_numbers)

    def test_mixed_numbers(self):
        mixed_numbers = [10, -10, 0, -1, 1]
        self.assert_stdout('1\n-1\n0\n-10\n10\n', mixed_numbers)

    def test_repeated_numbers(self):
        repeated_numbers = [1, 2, 2, 1]
        self.assert_stdout('1\n2\n2\n1\n', repeated_numbers)

    def test_none_values(self):
        with self.assertRaises(TypeError):
            self.assert_stdout('', [None])

    def test_non_integer_values(self):
        with self.assertRaises(TypeError):
            self.assert_stdout('', ['a', 'b', 'c'])

    def test_very_large_list(self):
        very_large_list = list(range(10**6))  # A list with 1 million elements
        # No expected output; this test is just for performance

    def test_extremely_large_numbers(self):
        extremely_large_numbers = [10**100, 10**100 + 1]  # Extremely large numbers
        # No expected output; this test is just for performance
        

if __name__ == '__main__':
    unittest.main()
