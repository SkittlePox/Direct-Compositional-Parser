from LexicalStructures import *
from Grammar import *
from LexiconParser import *
from Lexicon import *

def main():
    lex = LexiconParser()
    entries = lex.parse_file("lexicon.txt")
    lexicon = Lexicon(entries)
    print(lexicon)
    grammar = DCGrammar()
    print(grammar.possible_combinations(lexicon.entries[0], lexicon.entries[1]))

if __name__ == "__main__":
    main()
