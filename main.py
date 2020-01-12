from LexicalStructures import *
from Grammar import *
from LexiconParser import *
from Lexicon import *
from GrammarInteractor import *

def main():
    lex = LexiconParser()
    entries = lex.parse_file("lexicon.txt")
    lexicon = Lexicon(entries)
    print(lexicon)
    grammar = DCGrammar()
    interactor = GrammarInteractor(grammar)
    # print(interactor.possible_combinations(lexicon.entries[0], lexicon.entries[1]))
    interactor.single_layer_possible_combinations(entries)

if __name__ == "__main__":
    main()
