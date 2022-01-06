import unittest
from scripts.main import Fraction


class ReduceFractionTest(unittest.TestCase):

    def test_already_in_lowest_terms(self):
        self.assertEqual(Fraction(3, 4), Fraction(3, 4))

    # ignore for now
    def reduce_to_whole_numbers(self):
        self.assertEqual(Fraction(6, 8), Fraction(3, 4))
