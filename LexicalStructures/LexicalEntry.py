import enum
from functools import reduce

SPACING = True
COUNTER = 0

class LexicalEntry:
    def __init__(self, english, syntacticCategory, semanticEntry):
        self.english = english
        self.category = syntacticCategory
        self.semantics = semanticEntry
        global COUNTER
        self.id = COUNTER
        COUNTER += 1

    def __eq__(self, other):
        return isinstance(other, LexicalEntry) \
        and self.english == other.english and self.category == other.category \
        and self.semantics.type == other.semantics.type #and self.semantics.function == other.semantics.function
    def __str__(self):
        cat = str(self.category)
        if SPACING:
            return f"<[{self.id}] \"{self.english}\" ; {cat} ; {str(self.semantics)} >"
        return f"<\"{self.english}\";{cat};{str(self.semantics)}>"
    def __hash__(self):
        return hash(self.english) # LOL easy way out
