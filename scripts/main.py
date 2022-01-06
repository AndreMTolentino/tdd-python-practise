class Fraction:

    def __init__(self, intergerValue):
        self.intergerValue = intergerValue

    def add(self, numb):
        return Fraction(self.intergerValue + numb)

    def intValue(self):
        return self.intergerValue
