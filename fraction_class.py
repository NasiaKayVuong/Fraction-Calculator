class Fraction():
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        if denominator != 0:
            self.denominator = denominator
        else:
            raise ValueError

    def __str__(self):
        return str(self.numerator)+'/' + str(self.denominator)

    def __repr__(self):
        return 'A fraction with numerator {} and denominator {}'.format(self.numerator, self.denominator)

    def is_proper(self):
        if self.numerator > self.denominator:
            return False
        else:
            return True

    def flip_fraction(self):
        num = self.denominator
        denom = self.numerator
        new = Fraction(num, denom)
        return new

    def __add__(self, other):
        if self.denominator == other.denominator:
            new = Fraction(self.numerator+other.numerator, self.denominator)
            return new
        else:
            numer = (self.numerator * other.denominator) + \
                (other.numerator*self.denominator)
            denom = self.denominator * other.denominator
            new = Fraction(numer, denom)
            return new

    def __eq__(self, other):
        if self.numerator == other.numerator and self.denominator == other.denominator:
            return True
        else:
            return False

    def __sub__(self, other):
        new_other = Fraction(-other.numerator, other.denominator)
        return self+new_other  # same as self.__add__(other)

    def __mul__(self, other):
        num = self.numerator * other.numerator
        denom = self.denominator * other.denominator
        return Fraction(num, denom)

    def __truediv__(self, other):
        new_other = other.flip_fraction()
        return self * new_other
