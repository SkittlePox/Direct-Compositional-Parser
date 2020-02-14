from LexicalStructures import *

### R-1a

def R1a_test(a, b):
    return a.slash == SyntacticSlash.R and a.rhs == b

def R1a_operate(a, b):
    new_english = f"{a.english} {b.english}"
    new_category = a.category.lhs
    new_semantics = a.semantics(b.semantics)
    return LexicalEntry(english=new_english, syntacticCategory=new_category, semanticEntry=new_semantics)

### R-1b

def R1b_test(a, b):
    return b.slash == SyntacticSlash.L and b.rhs == a

def R1b_operate(a, b):
    new_english = f"{a.english} {b.english}"
    new_category = b.category.lhs
    new_semantics = b.semantics(a.semantics)
    return LexicalEntry(english=new_english, syntacticCategory=new_category, semanticEntry=new_semantics)
