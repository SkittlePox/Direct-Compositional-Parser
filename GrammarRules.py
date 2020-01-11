def R1a_test(a, b):
    return b.rhs == a.lhs

def R1a_operate(a, b):
    newName = f"{a.english} {b.english}"
    newCat = b.category.lhs
    newSem = b.type.rhs
    return LexicalEntry(newName, newCat, newSem)
