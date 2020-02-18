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

def test_parser():
    lexParser = LexiconParser()
    entries = lexParser.parse_file("lexicon.txt")
    lexicon = Lexicon(list(set(entries)))
    print(lexicon)

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
    print(ltree.evaluate())
    print(ltree)

    porky = lexicon.getEntry("Porky")
    zinkly = lexicon.getEntry("Zinkly")
    likes = lexicon.getEntry("likes")
    lptree = LexicalTree(rule=r1a, a=likes, b=porky)
    print(lptree.evaluate())
    zlptree = LexicalTree(rule=r1b, a=zinkly, b=lptree)
    print(zlptree.evaluate())   # This evaluates to undefined
    print("The above should be undefined")

    # likes == m=(m=1 p=1) p=(m=0 p=1) z=(m=0)
    # let's add something to make zlptree evaluate to a value
    likes.semantics.update({"p": {"z": "1"}})
    print(likes.semantics)
    print(zlptree.evaluate())   # Now this evaluates to 1
    print("This should now evaluate to 1")

def grammarTest():
    lexParser = LexiconParser()
    entries = lexParser.parse_file("lexicon.txt")
    lexicon = Lexicon(list(set(entries)))
    print(lexicon)
    snp = lexParser.parse_syntactic_category("S/NP")
    # print(snp)
    honest = lexicon.getEntry("honest")
    # print(R2_test(honest))

def semanticTest():
    lexParser = LexiconParser()
    snp = lexParser.parse_syntactic_category("S/NP")
    s = SemTest(snp)
    o1, o2 = s.f("hi")
    print(o1, o2)
    s.var = "Working"
    o1, o2 = s.f("hmm")
    print(o1, o2)

def semanticTest2():
    print("hlo")

if __name__ == "__main__":
    # main()
    # test_parser()
    # example_lexicalTree()
    # grammarTest()
    semanticTest2()
