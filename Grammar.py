from GrammarRules import *
from itertools import compress

class CombinatoryRule():
    def __init__(self, name, test, operate):
        """
        test takes syntactic grammar categories
        Returns whether or not this rule can operate on the given categories

        operate takes whole lexical entries
        Returns the resulting lexical entry after applying this rule
        """
        self.name = name
        self.test = test
        self.operate = operate

    def __str__(self):
        return self.name

class Grammar():
    def __init__(self, rules):
        self.rules = rules

    def possible_combinations(self, a, b):
        selectors = list(map(lambda x: x.test(a.category, b.category), self.rules))
        data = map(lambda x: str(x), self.rules)
        return list(compress(data, selectors))

class DCGrammar(Grammar):
    def __init__(self):
        rules = []
        rules.append(CombinatoryRule(name="R-1a", test=R1a_test, operate=R1a_operate))
        rules.append(CombinatoryRule(name="R-1b", test=R1b_test, operate=R1b_operate))
        self.rules = rules
        Grammar(rules)
