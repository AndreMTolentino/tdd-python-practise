from scripts.main import Fraction
import unittest

class FractionEqualsTests(unittest.TestCase):

    def test_same_numerator_and_denominator(self):
        self.assertEqual(Fraction(3, 5), Fraction(3, 5))

    def test_diff_numerator(self):
        self.assertNotEqual(Fraction(1, 5), Fraction(2, 5))

    def test_diff_denominators(self):
        self.assertNotEqual(Fraction(2, 4), Fraction(3, 7))

    def test_same_integer_and_fraction(self):
        self.assertEqual(Fraction(4, 1), Fraction(4))

    def test_diff_integers(self):
        self.assertNotEqual(Fraction(3), Fraction(4))

    def test_negative_denominator(self):
        self.assertEqual(Fraction(1, 2), Fraction(-1, -2))
        self.assertEqual(Fraction(-1, 2), Fraction(1, -2))
