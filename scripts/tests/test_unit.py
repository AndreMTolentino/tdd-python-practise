from scripts.main import Fraction
import unittest


class TestFraction(unittest.TestCase):

    def test_zero_plus_zero(self):
        result = Fraction(0).add(Fraction(0))
        self.assertEqual(result, Fraction(0))

    def test_zero_plus_number(self):
        result = Fraction(0).add(Fraction(2))
        self.assertEqual(result, Fraction(2))

    def test_number_plus_zero(self):
        result = Fraction(3).add(Fraction(0))
        self.assertEqual(result, Fraction(3))

    def test_number_plus_number(self):
        result = Fraction(1).add(Fraction(6))
        self.assertEqual(result, Fraction(7))

    def test_negative_number_plus_number(self):
        result = Fraction(-3).add(Fraction(1))
        self.assertEqual(result, Fraction(-2))

    def test_sum_non_trivial_common_denominator(self):
        result = Fraction(1, 5).add(Fraction(2, 5))
        self.assertEqual(result, Fraction(3, 5))

    def test_diff_denominators(self):
        self.assertEqual(Fraction(5, 6), Fraction(1, 2).add(Fraction(1, 3)))