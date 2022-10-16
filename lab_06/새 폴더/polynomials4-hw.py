import copy

class Polynomial:
    def __init__(self, degree = 0):
        self.degree = degree
        self.coef = [0] * (self.degree + 1)

    def __str__(self):
        ret = ""
        for coef, exp in [
            (self.coef[i], i) for i in range(self.degree + 1) if self.coef[i] != 0
        ] [
            ::-1
        ]:
            ret += f"({coef})x^{exp} + "

        return f"{ret}\b\b"

    def attach(self, coef=0, exp=0):
        self.coef[exp] = coef
        return self

    def get_lead_exp(self):
        i = len(self.coef) - 1
        while i >= 0 and self.coef[i] == 0:
            i -= 1

        if i < 0:
            raise Exception("Failed to get_lead_exp.")
        return i

    def evaluate(self, x):
        return sum(
            (coef * (x**exp) for exp, coef in enumerate(self.coef) if coef != 0)
        )

    def get_coef(self, exp):
        return self.coef[exp]

    def is_zero(self):
        return not any(self.coef)

    def zero(self):
        for i in range(len(self.coef)):
            self.coef[i] = 0

    def remove(self, exp):
        self.coef[exp] = 0

    def __add__(self, other):
        poly = Polynomial(max(self.degree, other.degree))

        while not self.is_zero() or not other.is_zero():
            exp_01 = self.get_lead_exp()
            exp_02 = other.get_lead_exp()

            if exp_01 > exp_02:
                poly.attach(self.get_coef(exp_01), exp_01)
                self.remove(exp_01)
            elif exp_01 < exp_02:
                poly.attach(other.get_coef(exp_02), exp_02)
                other.remove(exp_02)
            else:
                coef = self.get_coef(exp_01) + other.get_coef(exp_02)
                exp = exp_01
                poly.attach(coef, exp)

                self.remove(exp_01)
                other.remove(exp_02)

        return poly

    def __mul__(self, other):

        poly = Polynomial()
        if not self.is_zero() or not other.is_zero():
            poly = Polynomial(self.get_lead_exp() + other.get_lead_exp())
        else:
            poly = Polynomial(max(self.get_lead_exp(), other.get_lead_exp()))

        while not self.is_zero():
            exp_01 = self.get_lead_exp()

            temp = copy.deepcopy(other)
            while not temp.is_zero():
                exp_02 = temp.get_lead_exp()
                poly.attach(self.get_coef(exp_01) * temp.get_coef(exp_02), exp_01 + exp_02)
                temp.remove(exp_02)
            self.remove(exp_01)

        return poly

if __name__ == "__main__":

    poly1 = Polynomial(2)
    poly1.attach(2, 2).attach(3, 1).attach(1, 0)
    print("poly1 =\n", poly1)

    poly2 = Polynomial(1)
    poly2.attach(3, 1).attach(-2, 0)
    print("poly2 =\n", poly2)

    poly = poly1 * poly2
    print()
    print("poly1 * poly2 =\n", poly)