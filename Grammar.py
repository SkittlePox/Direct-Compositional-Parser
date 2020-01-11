from GrammarRules import *

class CombinatoryRule():
    def __init__(self, test, operate):
        """
        test takes syntactic grammar categories
        Returns whether or not this rule can operate on the given categories

        operate takes whole lexical entries
        Returns the resulting lexical entry after applying this rule
        """
        self.test = test
        self.operate = operate

class Grammar():
    def __init__(self, rules):
        self.rules = rules

class DCGrammar(Grammar):
    def __init__(self):
        rules = []
        # R1a_test = lambda a, b: b.rhs == a.lhs
        # def R1a_operate(a, b):
        #     newName = f"{a.english} {b.english}"
        #     newCat = b.category.lhs
        #     newSem = b.type.rhs
        #     return LexicalEntry(newName, newCat, newSem)
        rules.append(CombinatoryRule(test=R1a_test, operate=R1a_operate))

        Grammar(self, rules)
