class Fraction:

    def __init__(self, numerator, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    def add(self, Number):
        return Fraction(self.numerator + Number.numerator, self.denominator)

    def intValue(self):
        return self.numerator

    def Numerator(self):
        return self.numerator

    def Denominator(self):
        return self.denominator
