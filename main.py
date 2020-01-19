from LexicalStructures import *
from Grammar import *
from LexiconParser import *
from Lexicon import *
from GrammarInteractor import *

def main():
    lexParser = LexiconParser()
    entries = lexParser.parse_file("lexicon.txt")
    lexicon = Lexicon(set(entries))
    print(lexicon)
    grammar = DCGrammar()
    interactor = GrammarInteractor(grammar)
    # z = interactor.possible_combinations(lexicon.entries[0], lexicon.entries[3])
    # print(z[0].operate(lexicon.entries[0], lexicon.entries[3]))
    # interactor.single_layer_possible_combinations(entries)
    # interactor.multi_layer_possible_combinations(entries)
    interactor.populate_lexicon(lexicon)
    print(lexicon)

if __name__ == "__main__":
    main()
