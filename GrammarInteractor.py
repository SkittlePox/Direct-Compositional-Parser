from itertools import compress

class GrammarInteractor():
    def __init__(self, grammar):
        self.grammar = grammar

    def possible_combinations(self, a, b):
        selectors = list(map(lambda x: x.test(a.category, b.category), self.grammar.rules.values()))
        data = map(lambda x: str(x), self.grammar.rules.values())
        return list(compress(data, selectors))

    def single_layer_possible_combinations(self, entries):
        for a in entries:
            for b in entries:
                combs = self.possible_combinations(a, b)
                if len(combs) is not 0:
                    print(str(a))
                    print(str(b))
                    print(str(self.grammar.rules[combs[0]].operate(a, b)) + " by " + combs[0] + "\n")
