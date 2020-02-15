from LexicalStructures import *

### R-1a

def R1a_test(a, b):
    return a.syntax.slash == SyntacticSlash.R and a.syntax.rhs == b.syntax

def R1a_operate(a, b):
    new_english = f"{a.english} {b.english}"
    new_category = a.syntax.lhs
    new_semantics = a.semantics(b.semantics)
    return LexicalEntry(english=new_english, syntacticEntry=new_category, semanticEntry=new_semantics)

### R-1b

def R1b_test(a, b):
    return b.syntax.slash == SyntacticSlash.L and b.syntax.rhs == a.syntax

def R1b_operate(a, b):
    new_english = f"{a.english} {b.english}"
    new_category = b.syntax.lhs
    new_semantics = b.semantics(a.semantics)
    return LexicalEntry(english=new_english, syntacticEntry=new_category, semanticEntry=new_semantics)

### R-2         This is a unary rule!
# AP = S[A]/NP
AP = SyntacticCategory((SyntacticCategory(SyntacticPrimitive("S"), features=["A"]), SyntacticPrimitive("NP")))
def R2_test(a):
    return a.syntax == AP
