class CombinatoryRule():
    def __init__(self, test, operation):
        self.test = test
        self.operation = operation

    def test(self, syntactic_category_a, syntactic_category_b):
        """
        This function takes syntactic grammar categories
        Returns whether or not this rule can operate on the given categories
        """
        return self.func(syntactic_category_a, syntactic_category_b)

    def operate(self, lexical_entry_a, lexical_entry_b):
        """
        This function takes whole lexical entries
        Returns the resulting lexical entry after applying this rule
        """
        return self.operation(lexical_entry_a, lexical_entry_b)

class Grammar():
    def __init__(self, rules):
        self.rules = rules

class DCGrammar(Grammar):
    def __init__(self):
        rules = []
        # R1a_test = lambda a, b: 
        # rules.append(CombinatoryRule(test=lambda a,b: a == b)

        Grammar.__init__(self, rules)
