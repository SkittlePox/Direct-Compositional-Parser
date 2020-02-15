from LexicalStructures import *
from LexiconParser import *

parser = LexiconParser()

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

AP = parser.parse_syntactic_category("S[A]/rNP")

def R2_test(a):
    return a.syntax == AP

def R2_operate(a):
    new_category = parser.parse_syntactic_category("N/N") if " " in a.english else parser.parse_syntactic_category("N/rN")
    new_semantics = None    # Lots of work to implement this
