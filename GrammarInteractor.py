from itertools import compress
import copy

class GrammarInteractor():
    def __init__(self, grammar):
        self.grammar = grammar

    def possible_combinations(self, a, b):
        selectors = list(map(lambda x: x.test(a.category, b.category), self.grammar.rules.values()))
        # data = map(lambda x: str(x), self.grammar.rules)
        return list(compress(self.grammar.rules.values(), selectors))

    def populate_lexicon(self, lexicon, layers=4):
        for i in range(layers):
            entries = copy.copy(lexicon.entries)
            for a in entries:
                for b in entries:
                    combinatoryRules = self.possible_combinations(a, b)
                    if len(combinatoryRules) is not 0:
                        newEntries = list(map(lambda x: x(a, b), combinatoryRules))
                        # print(newEntries[0])
                        lexicon.add(newEntries)

        # print(lexicon)

    # def single_layer_possible_combinations(self, entries):
    #     for a in entries:
    #         for b in entries:
    #             combs = self.possible_combinations(a, b)
    #             if len(combs) is not 0:
    #                 print(str(a))
    #                 print(str(b))
    #                 print(str(self.grammar.rules[combs[0]].operate(a, b)) + " by " + combs[0] + "\n")
    #
    # def multi_layer_possible_combinations(self, entries, layers=3):
    #     for i in range(layers):
    #         for a in entries:
    #             for b in entries:
    #                 combs = self.possible_combinations(a, b)
    #                 newEntries = list(map(lambda x: x.operate(a, b), combs))
    #                 print(newEntries)
