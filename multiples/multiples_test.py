import unittest

import multiples

# https://projecteuler.net/problem=1

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

class MultiplesTest(unittest.TestCase):
    def test_sum_of_multiples_below_1_is_0(self):
        self.assertEquals(0, multiples.multiples_of_3_and_5(1))

    def test_sum_of_multiples_below_2_is_0(self):
        self.assertEquals(0, multiples.multiples_of_3_and_5(2))

    def test_sum_of_multiples_below_3_is_0(self):
        self.assertEquals(0, multiples.multiples_of_3_and_5(3))

    def test_sum_of_multiples_below_4_is_3(self):
        self.assertEqual(3, multiples.multiples_of_3_and_5(4))

    def test_sum_of_multiples_below_5_is_3(self):
        self.assertEqual(3, multiples.multiples_of_3_and_5(5))

    def test_sum_of_multiples_below_6_is_8(self):
        self.assertEqual(8, multiples.multiples_of_3_and_5(6))

    def test_sum_of_multiples_below_7_is_23(self):
        self.assertEqual(14, multiples.multiples_of_3_and_5(7))

    def test_sum_of_multiples_below_8_is_23(self):
        self.assertEqual(14, multiples.multiples_of_3_and_5(8))

    def test_sum_of_multiples_below_9_is_23(self):
        self.assertEqual(14, multiples.multiples_of_3_and_5(9))

    def test_sum_of_multiples_below_10_is_23(self):
        self.assertEqual(23, multiples.multiples_of_3_and_5(10))

    def test_sum_of_multiples_below_1000_is_233168(self):
        self.assertEqual(233168, multiples.multiples_of_3_and_5(1000))


if __name__ == '__main__':
    unittest.main()
