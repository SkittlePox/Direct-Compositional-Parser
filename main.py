from LexicalStructures import *
from Grammar import *

def main():
    # feat = (SyntacticFeature.A, SyntacticFeature.V)
    # z = SyntacticPrimitive.S
    # cat = SyntacticCategory((z, z), SyntacticSlash.R, feat)
    # zat = SyntacticCategory((cat, SyntacticPrimitive.NP))
    # print(cat)
    # print(zat)
    #
    # bee =
    # cee = SemanticType((bee, SemanticPrimitive.t))
    # print(bee)
    # print(cee)
    #
    # lex = LexicalEntry("eyy", cee, zat)
    # print(lex)

    walkS = SyntacticCategory((SyntacticPrimitive.S, SyntacticPrimitive.NP))
    z = SemanticType((SemanticPrimitive.e, SemanticPrimitive.t))
    walkSem = SemanticType((z, SemanticPrimitive.t))
    walk = LexicalEntry("walks", walkS, walkSem)
    print(walk)

    jimS = SyntacticCategory(SyntacticPrimitive.NP)
    jimSem = SemanticType(SemanticPrimitive.e)
    jim = LexicalEntry("Jim", jimS, jimSem)
    print(jim)

    # comb = CombinatoryGrammarRule(lambda a,b: a == b)
    # print(comb.test(1, 1))

if __name__ == "__main__":
    main()
