from scripts.main import Fraction


def test_zero_plus_zero():
    result = Fraction(0).add(Fraction(0))
    assert result.intValue() == 0


def test_zero_plus_number():
    result = Fraction(0).add(Fraction(2))
    assert result.intValue() == 2


def test_number_plus_zero():
    result = Fraction(3).add(Fraction(0))
    assert result.intValue() == 3


def test_number_plus_number():
    result = Fraction(1).add(Fraction(6))
    assert result.intValue() == 7


def test_negative_number_plus_number():
    result = Fraction(-3).add(Fraction(1))
    assert result.intValue() == -2


def test_sum_non_trivial_common_denominator():
    result = Fraction(1, 5).add(Fraction(2, 5))
    assert 3 == result.Numerator()
    assert 5 == result.Denominator()
