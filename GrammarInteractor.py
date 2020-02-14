from itertools import compress
import copy

class GrammarInteractor():
    def __init__(self, grammar):
        self.grammar = grammar

    def possible_combinations(self, a, b):
        selectors = list(map(lambda x: x.test(a, b), self.grammar.rules.values()))
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
                        lexicon.add(newEntries)
