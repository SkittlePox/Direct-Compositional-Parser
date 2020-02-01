from LexicalStructures import *
from Grammar import *
from LexiconParser import *
from GrammarInteractor import *

def main():
    lexParser = LexiconParser()
    entries = lexParser.parse_file("lexicon.txt")
    lexicon = Lexicon(set(entries))
    # print(entries)
    print(lexicon)
    grammar = Grammar()
    interactor = GrammarInteractor(grammar)
    interactor.populate_lexicon(lexicon)
    print("After populating:")
    print(lexicon)

def test():
    dicto = {"a" : 1, "b" : 2}
    dicto2 = {"z" : dicto}
    print(dicto2)
    te = ['z', 'b']
    sem1 = SemanticExpression(dicto2, 'z')
    sem2 = SemanticExpression(sem1, 'a')
    sem3 = SemanticExpression(dicto2, te)
    sem4 = SemanticExpression("hello", te)
    print(sem2, type(sem2))
    print(sem1.evaluate(), type(sem1.evaluate()))
    print(sem2.evaluate(), type(sem2.evaluate()))
    print(sem3.evaluate(), type(sem3.evaluate()))
    print(sem3)
    print(sem4)

def test2():
    lexParser = LexiconParser()
    entries = lexParser.parse_file("lexicon.txt")
    lexicon = Lexicon(set(entries))
    print(lexicon)


if __name__ == "__main__":
    main()
    # test()
    # test2()
