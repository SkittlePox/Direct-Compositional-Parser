from SyntaxSemantics import *

def main():
    feat = (SyntaxFeature.A, SyntaxFeature.V)
    z = SyntacticPrimitive.S
    cat = SyntacticCategory((z, z), feat)
    zat = SyntacticCategory((cat, SyntacticPrimitive.NP))
    print(cat)
    print(zat)

    bee = SemanticType((SemanticPrimitive.e, SemanticPrimitive.t))
    cee = SemanticType((bee, SemanticPrimitive.t))
    print(bee)
    print(cee)

if __name__ == "__main__":
    main()
