import unittest
from scripts.main import Fraction


class ReduceFractionTest(unittest.TestCase):

    def test_already_in_lowest_terms(self):
        self.assertEqual(Fraction(3, 4), Fraction(3, 4))

    def test_reduce_to_not_whole_numbers(self):
        self.assertEqual(Fraction(6, 8), Fraction(3, 4))

    def test_reduce_to_whole_numbers(self):
        self.assertEqual(Fraction(6), Fraction(24, 4))

    def test_reduce_zero(self):
        self.assertEqual(Fraction(0), Fraction(0, 16))

    def test_reduce_results_to_whole_number(self):
        self.assertEqual(Fraction(1), Fraction(1, 3).add(Fraction(2, 3)))

    def test_one_denominator_is_multiple_of_the_other(self):
        self.assertEqual(Fraction(11, 8), Fraction(3, 4).add(Fraction(5, 8)))

    def test_common_factor_in_denominators(self):
        self.assertEqual(Fraction(11, 18), Fraction(1, 6).add(Fraction(4, 9)))

    def test_reduce_event_when_denominators_are_the_same(self):
        self.assertEqual(Fraction(3, 2), Fraction(3, 4).add(Fraction(3, 4)))

    def test_reduce_negative_fraction_and_reducing(self):
        self.assertEqual(Fraction(1, 2), Fraction(-1, 4).add(Fraction(3, 4)))
        self.assertEqual(Fraction(-1, 8), Fraction(3, 8).add(Fraction(-1, 2)))

    # Ignore that for now
    def negative_signs_everywhere(self):
        self.assertEqual(Fraction(1, 2), Fraction(1, -4).add(Fraction(-3, -4)))
