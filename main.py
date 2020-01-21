from LexicalStructures import *
from Grammar import *
from LexiconParser import *
from Lexicon import *
from GrammarInteractor import *

def main():
    lexParser = LexiconParser()
    entries = lexParser.parse_file("lexicon.txt")
    lexicon = Lexicon(set(entries))
    # print(entries)
    print(lexicon)
    grammar = DCGrammar()
    interactor = GrammarInteractor(grammar)
    interactor.populate_lexicon(lexicon)
    print("After populating:")
    print(lexicon)

if __name__ == "__main__":
    main()
