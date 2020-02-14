class LexicalTree:
    def __init__(self, rule, a, b):
        self.rule = rule
        self.a = a
        self.b = b

    def calculate(self):
        a = self.a.calculate() if isinstance(self.a, LexicalTree) else self.a
        b = self.b.calculate() if isinstance(self.b, LexicalTree) else self.b
        return self.rule(a, b)
