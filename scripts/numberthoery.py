class NumberTheory:

    def gcd(self, a, b):
        while b != 0:
            t = b
            b = a % t
            a = t
        return abs(a)
