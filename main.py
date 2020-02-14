from LexicalStructures import *
from Grammar import *
from LexiconParser import *
from GrammarInteractor import *
from LexicalTree import *

def main():
    lexParser = LexiconParser()
    entries = lexParser.parse_file("lexicon.txt")
    lexicon = Lexicon(list(set(entries)))
    print(lexicon)
    grammar = Grammar()
    interactor = GrammarInteractor(grammar)
    interactor.populate_lexicon(lexicon)
    print("After populating:")
    print(lexicon)

def test():
    lexParser = LexiconParser()
    entries = lexParser.parse_file("lexicon.txt")
    lexicon = Lexicon(list(set(entries)))
    print(lexicon)
    grammar = Grammar()
    r1b = grammar.rules['R-1b']
    r1a = grammar.rules['R-1a']
    mitka = lexicon.retrieve("Mitka")
    walks = lexicon.retrieve("walks")
    # print(mitka, walks)
    # print(r1b.test(mitka, walks))
    print(r1b(mitka, walks))
    ltree = LexicalTree(rule=r1b, a=mitka, b=walks)
    print(ltree.calculate())

    likes = lexicon.retrieve("likes")
    porky = lexicon.retrieve("Porky")
    # print(r1a.test(likes, porky))
    ptree = LexicalTree(rule=r1a, a=likes, b=porky)
    lptree = LexicalTree(rule=r1b, a=mitka, b=ptree)
    likes_porky = r1a(likes, porky)
    mitka_likes_porky = r1b(mitka, likes_porky)
    print(mitka_likes_porky)
    print(lptree.calculate())

if __name__ == "__main__":
    main()
    # test()
