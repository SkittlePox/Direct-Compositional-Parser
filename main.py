from LexicalStructures import *
from Grammar import *
from LexiconParser import *

def main():
    # feat = (SyntacticFeature.A, SyntacticFeature.V)
    # z = SyntacticPrimitive.S
    # cat = SyntacticCategory((z, z), SyntacticSlash.R, feat)
    # zat = SyntacticCategory((cat, SyntacticPrimitive.NP))
    # print(cat)
    # print(zat)
    #
    # walkS = SyntacticCategory((SyntacticPrimitive.S, SyntacticPrimitive.NP))
    # walkSem = SemanticType((SemanticPrimitive.e, SemanticPrimitive.t))
    # walk = LexicalEntry("walks", walkS, walkSem)
    # print(walk)
    #
    # jimS = SyntacticCategory(SyntacticPrimitive.NP)
    # jimSem = SemanticType(SemanticPrimitive.e)
    # jim = LexicalEntry("Jim", jimS, jimSem)
    # print(jim)
    #
    # comb = CombinatoryGrammarRule(lambda a,b: a == b)
    # print(comb.test(1, 1))
    #
    # R1a_test = lambda a, b: b.rhs == a.lhs
    # def R1a_operate(a, b):
    #     newName = f"{a.english} {b.english}"
    #     newCat = b.category.lhs
    #     newSem = b.type.rhs
    #     return LexicalEntry(newName, newCat, newSem)
    # print(R1a_test(jimS, walkS))
    # print(R1a_operate(jim, walk))
    lex = LexiconParser()
    entries = lex.parseFile("lexicon.txt")
    print(entries[3])

if __name__ == "__main__":
    main()
