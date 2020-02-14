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

def test5():
    a = SemanticIntention(argument="tom")
    b = SemanticIntention(argument="likes")
    c = SemanticIntention(function=b, argument=a) # likes(tom)
    d = SemanticIntention(argument="jane")
    e = SemanticIntention(c, d)
    f = SemanticIntention(argument="happens")
    g = SemanticIntention(function=f, argument=e)
    h = SemanticIntention(function=f, argument=g)
    print(h)

if __name__ == "__main__":
    main()
    # test5()
