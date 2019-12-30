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

    # def test(self, syntactic_category_a, syntactic_category_b):
    #
    #     return self.testfunc(syntactic_category_a, syntactic_category_b)
    #
    # def operate(self, lexical_entry_a, lexical_entry_b):
    #     """
    #     This function takes whole lexical entries
    #     Returns the resulting lexical entry after applying this rule
    #     """
    #     return self.operation(lexical_entry_a, lexical_entry_b)

class Grammar():
    def __init__(self, rules):
        self.rules = rules

class DCGrammar(Grammar):
    def __init__(self):
        rules = []
        # R1a_test = lambda a, b: b.rhs == a.lhs
        # print(R1a_test())
        # rules.append(CombinatoryRule(test=lambda a,b: a == b)

        Grammar.__init__(self, rules)
