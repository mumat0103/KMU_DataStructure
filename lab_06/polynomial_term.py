class Term:
    def __init__(self, coef =0, exp =0):
        self.coef = coef
        self.exp = exp
        
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return f"{self.coef, self.exp}"

class Polynomial:
    def __init__(self):
        self.bgn = 0
        self.end = 0
        self.terms = []
        
    def attach(self, coef=0, exp=0):
        self.terms.append(Term(coef, exp))
        return self
    
    def evaluate(self, x):
        return sum((i.coef * (x**i.exp) for i in self.terms))
    
    def find_term(self, exp):
        i = 0
        while i < len(self.terms) and self.terms[i].exp != exp:
            i += 1
            
        return self.terms[i] if i < len(self.terms) else None
                
    def __str__(self):
        ret = ""
        terms = sorted(self.terms, key=lambda x: x.exp, reverse=True)
        for i in terms:
            ret += f"({i.coef})x^{i.exp} + "
        return f"{ret}\b\b\b"
    
    def __add__(self, other):
        poly = Polynomial()
        terms_a = self.terms
        terms_b = other.terms
        
        pos_a, pos_b = 0, 0
        
        while pos_a < len(terms_a) and pos_b < len(terms_b):
            term_a, term_b = terms_a[pos_a], terms_b[pos_b]
            
            if term_a.exp > term_b.exp:
                poly.attach(term_a.coef, term_a.exp)
                pos_a += 1
            elif term_a.exp < term_b.exp:
                poly.attach(term_b.coef, term_b.exp)
                pos_b += 1
            else:
                coef = term_a.coef + term_b.coef
                if coef != 0:
                    poly.attach(coef, term_a.exp)
                pos_a += 1
                pos_b += 1
        while pos_a < len(terms_a):
            term = terms_a[pos_a]
            poly.attach(term.coef, term.exp)
            pos_a += 1
        while pos_b < len(terms_b):
            term = terms_b[pos_b]
            poly.attach(term.coef, term.exp)
            pos_b += 1        
        return poly
    
    def __mul__(self, other): #과제
        poly = Polynomial()

        for i in self.terms:
            for j in other.terms:
                exp = i.exp + j.exp
                coef = i.coef * j.coef
                
                term = poly.find_term(exp)
                if term is None:
                    poly.attach(coef, exp)
                else:
                    term.coef += coef
        
        return poly
    
if __name__ == "__main__":
    poly1 = Polynomial()
    poly1.attach(2, 2).attach(3, 1).attach(1, 0)
    print("poly1 =\n", poly1)
    
    poly2 = Polynomial()
    poly2.attach(3, 1).attach(-2, 0)
    print("poly2 =\n", poly2)
    
    print()
    poly = poly1 + poly2
    print("poly =\n", poly)
    print()
    
    poly3 = Polynomial()
    poly3.attach(1,1).attach(1,0)
    print("poly3 = \n", poly3)
    
    poly4 = Polynomial()
    poly4.attach(1,2).attach(-5,1).attach(-6,0)
    print("poly4 = \n", poly4)
    
    print()
    poly = poly3 * poly4
    print("poly =\n", poly)