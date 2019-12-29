from LexicalStructures import *
from LexicalEntry import *

def main():
    feat = (SyntacticFeature.A, SyntacticFeature.V)
    z = SyntacticPrimitive.S
    cat = SyntacticCategory((z, z), feat)
    zat = SyntacticCategory((cat, SyntacticPrimitive.NP))
    print(cat)
    print(zat)

    bee = SemanticType((SemanticPrimitive.e, SemanticPrimitive.t))
    cee = SemanticType((bee, SemanticPrimitive.t))
    print(bee)
    print(cee)

    lex = LexicalEntry("eyy", cee, zat)
    print(lex)

if __name__ == "__main__":
    main()
