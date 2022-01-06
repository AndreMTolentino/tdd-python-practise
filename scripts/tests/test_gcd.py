import unittest
from scripts.main import Fraction


class GreatestCommonDivisorTest(unittest.TestCase):

    def gcd(self, a, b):
        while b != 0:
            t = b
            b = a % t
            a = t
        return abs(a)

    def test_already_in_lowest_terms(self):
        self.assertEqual(1, self.gcd(1, 1))
        self.assertEqual(2, self.gcd(2, 2))
        self.assertEqual(1, self.gcd(-1, -1))

    def test_relative_prime(self):
        self.assertEqual(1, self.gcd(2, 3))
        self.assertEqual(1, self.gcd(4, 7))
        self.assertEqual(1, self.gcd(-2, -3))

    def test_one_multiple_of_the_other(self):
        self.assertEqual(3, self.gcd(3, 9))
        self.assertEqual(5, self.gcd(5, 30))

    def test_common_factor(self):
        self.assertEqual(2, self.gcd(6, 8))
        self.assertEqual(7, self.gcd(49, 315))

    def test_negatives(self):
        self.assertEqual(4, self.gcd(-24, 28))
        self.assertEqual(4, self.gcd(24, -28))
