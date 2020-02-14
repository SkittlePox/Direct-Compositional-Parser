import enum
from functools import reduce

SPACING = True

class LexicalEntry:
    def __init__(self, english, syntacticCategory, semanticEntry, id=-1):
        self.english = english
        self.category = syntacticCategory
        self.semantics = semanticEntry
        self.id = id

    def __eq__(self, other):
        return isinstance(other, LexicalEntry) \
        and self.english == other.english \
        and self.category == other.category
        # and self.semantics.type == other.semantics.type #and self.semantics.function == other.semantics.function

    def __str__(self):
        category = str(self.category)
        semantics = str(self.semantics)
        if SPACING:
            return f"<[{self.id}] \"{self.english}\" ; {category} ; {semantics} >"
        else:
            return f"<\"{self.english}\";{category};{semantics}>"

    def __hash__(self):
        return hash(self.english) # LOL easy way out
