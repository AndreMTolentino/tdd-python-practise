class Fraction:

    def __init__(self, numerator, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    def __eq__(self, other):
        return self.numerator == other.numerator and \
               self.denominator == other.denominator

    def add(self, Number):
        if self.denominator != Number.denominator:
            return Fraction(self.numerator * Number.denominator + Number.numerator * self.denominator,
                            self.denominator * Number.denominator)
        else:
            return Fraction(self.numerator + Number.numerator, self.denominator)

    def hashcode(self):
        return self.numerator * 19 + self.denominator
