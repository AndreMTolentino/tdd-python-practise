from scripts.numberthoery import NumberTheory

class Fraction:

    def __init__(self, numerator, denominator=1):
        if denominator < 0:
            self.signOfDenominator = -1
        else:
            self.signOfDenominator = 1
        self.gcd = NumberTheory().gcd(numerator, denominator) * self.signOfDenominator
        self.numerator = numerator / self.gcd
        self.denominator = denominator / self.gcd

    def __eq__(self, other):
        return self.numerator == other.numerator and \
               self.denominator == other.denominator

    def add(self, Number):
        return Fraction(self.numerator * Number.denominator + Number.numerator * self.denominator,
                        self.denominator * Number.denominator)

    def hashcode(self):
        return self.numerator * 19 + self.denominator
