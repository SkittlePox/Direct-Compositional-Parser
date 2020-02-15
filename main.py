from LexicalStructures import *
from Grammar import *
from LexiconParser import *
from GrammarInteractor import *

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
    mitka = lexicon.getEntry("Mitka")
    walks = lexicon.getEntry("walks")
    # print(mitka, walks)
    # print(r1b.test(mitka, walks))
    print(r1b(mitka, walks))
    ltree = LexicalTree(rule=r1b, a=mitka, b=walks)
    print(ltree.calculate())

    likes = lexicon.getEntry("likes")
    porky = lexicon.getEntry("Porky")
    zinkly = lexicon.getEntry("Zinkly")
    # print(r1a.test(likes, porky))
    ptree = LexicalTree(rule=r1a, a=likes, b=porky)
    lptree = LexicalTree(rule=r1b, a=zinkly, b=ptree)
    mlptree = LexicalTree(rule=r1b, a=mitka, b=ptree)
    likes_porky = r1a(likes, porky)
    zinkly_likes_porky = r1b(zinkly, likes_porky)
    print(zinkly_likes_porky)
    print(lptree.calculate())
    print(mlptree.calculate())
    # likes.semantics.extension.update({"z": "1"}, "p")
    likes.semantics.extension.update({"p": {"z": "1"}})
    # likes.semantics.extension.update2({"p": {"z": "1"}})
    print(lptree.calculate())
    print(mlptree.calculate())

def example_lexicalTree():
    lexParser = LexiconParser()
    entries = lexParser.parse_file("lexicon.txt")
    lexicon = Lexicon(list(set(entries)))
    grammar = Grammar()
    r1b = grammar.rules['R-1b']
    r1a = grammar.rules['R-1a']

    mitka = lexicon.getEntry("Mitka")
    walks = lexicon.getEntry("walks")
    ltree = LexicalTree(rule=r1b, a=mitka, b=walks)
    print(ltree())

if __name__ == "__main__":
    main()
    # test()
    example_lexicalTree()
