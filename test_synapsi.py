from unittest import TestCase
from itertools import product

from synapsi import *


class TestTasksOne(TestCase):

    def test_if_can_reverse_number(self):
        """ Test 32 bit int number """

        number = 5927694924
        reverse_number = str(number)[::-1]
        reverse = reverse_int(number)

        self.assertTrue(reverse, reverse_number)

    def test_if_num_is_32_bit(self):
        """ Test 32 bit int number """

        number = 5927694924
        reversed_number = int(str(number)[::-1])

        reverse = reverse_int(number)

        self.assertEqual(reverse, reversed_number)

    def test_num_higher_than_32_bit(self):
        """ Test 32 bit int number """

        number = 5927694924
        reversed_number = int(str(number)[::-1])

        reverse = reverse_int(2 ** 32)

        self.assertNotEqual(reverse, reversed_number)

    def test_negative_number(self):
        """Test negative 32 bit number"""

        number = -123456789
        reversed_number = 0 - int(str(number)[-1:0:-1])

        reverse = reverse_int(number)

        self.assertTrue(reversed_number, reverse)

    def test_negative_not_32_bit(self):
        """ test not 32 bit int number. Should return 0 """

        number = -4294967295
        reversed_number = 0 - int(str(number)[-1:0:-1])

        reverse = reverse_int(number)

        self.assertNotEqual(reversed_number, reverse)
        self.assertEqual(reverse, 0)

    def test_hex_number(self):
        """ test not 32 bit hex number. Should return 0"""

        number = 0x7fffffff

        reversed_number = int(str(number)[::-1])
        reverse = reverse_int(number)

        self.assertNotEqual(reversed_number, reverse)
        self.assertEqual(reverse, 0)


class TestTaskTwo(TestCase):

    def test_all_combinations_1_digit(self):
        number = 2
        possibilities = [element.upper() for element in ["a", "b", "c"]]

        result = check_product(number)

        self.assertEqual(possibilities, result)

    def test_all_combinations_2_digits(self):
        number = 46
        possibilities = [element.upper() for element in ["gm", "gn", "go", "hm", "hn", "ho", "im", "in", "io"]]

        result = check_product(46)

        self.assertEqual(possibilities, result)

    def test_all_combinations_3_digits(self):
        letters = {
            '1': '',
            '2': list('ABC'),
            '3': list('DEF'),
            '4': list('GHI'),
            '5': list('JKL'),
            '6': list('MNO'),
            '7': list('PQRS'),
            '8': list('TUV'),
            '9': list('WXYZ'),
            '0': list('+'),
        }

        number = 466
        possibility = product(letters['4'], letters['6'], letters['6'])
        possibilities = [''.join(element) for element in possibility]

        result = check_product(number)

        self.assertEqual(possibilities, result)

    def test_zero(self):
        number = 0
        possibility = ['+']

        result = check_product(number)

        self.assertEqual(result, possibility)

    def test_empty_string(self):
        number = ''
        possibility = ['']

        result = check_product(number)

        self.assertEqual(result, possibility)


class TestTaskThree(TestCase):

    def test_first_case(self):

        max_width = 3
        string = 'test'
        test_result = '[\n]'

        result = maximum_string(string, max_width)

        self.assertEqual(test_result, result)

    def test_second_case(self):

        max_width = 4
        string = 'test test tescik'
        test_result = '[\ntest \ntest \n]'

        result = maximum_string(string, max_width)

        self.assertEqual(test_result, result)

    def test_third_case(self):

        max_width = 10
        string = 'test test tescik'
        test_result = '[\ntest test \ntescik \n]'

        result = maximum_string(string, max_width)

        self.assertEqual(test_result, result)
