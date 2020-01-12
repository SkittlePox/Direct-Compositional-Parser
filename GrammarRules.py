from LexicalStructures import *

### R-1a

def R1a_test(a, b):
    return a.slash == SyntacticSlash.R and a.rhs == b

def R1a_operate(a, b):
    newName = f"{a.english} {b.english}"
    newCat = a.category.lhs
    newSem = a.type.rhs
    return LexicalEntry(newName, newCat, newSem)

### R-1b

def R1b_test(a, b):
    return b.slash == SyntacticSlash.L and b.rhs == a

def R1b_operate(a, b):
    newName = f"{a.english} {b.english}"
    newCat = b.category.lhs
    newSem = b.type.rhs
    return LexicalEntry(newName, newCat, newSem)
